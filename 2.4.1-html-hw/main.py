import socket
import json
import urllib.parse
import mimetypes
import pathlib
import datetime
import threading

from http.server import HTTPServer, BaseHTTPRequestHandler


UDP_IP = '127.0.0.1'
UDP_PORT = 5000


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        if pr_url.path == '/':
            self.send_html_file('index.html')
        elif pr_url.path == '/message':
            self.send_html_file('message.html')
        else:
            if pathlib.Path().joinpath(pr_url.path[1:]).exists():
                self.send_static()
            else:
                self.send_html_file('error.html', 404)

    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        client_send_data(UDP_IP, UDP_PORT, data)
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", 'text/plain')
        self.end_headers()
        with open(f'.{self.path}', 'rb') as file:
            self.wfile.write(file.read())


def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ('', 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


def run_socket(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    sock.bind(server)
    try:
        while True:
            data, address = sock.recvfrom(1024)
            data_parse = urllib.parse.unquote_plus(data.decode())
            data_dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
            save_to_json(data_dict)
            resp_text = 'Saved'
            sock.sendto(resp_text.encode(), address)
    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        sock.close()


def client_send_data(ip, port, data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    sock.sendto(data, server)
    response, address = sock.recvfrom(1024)
    print(response.decode())
    sock.close()


def save_to_json(data):
    with open('storage/data.json', 'r') as json_file:
        data_dict = json.load(json_file)

    data_dict[str(datetime.datetime.now())] = data

    with open('storage/data.json', 'w') as storage:
        json.dump(data_dict, storage, indent=4)


if __name__ == '__main__':
    socket_thread = threading.Thread(target=run_socket, args=(UDP_IP, UDP_PORT))
    server_thread = threading.Thread(target=run)

    socket_thread.start()
    server_thread.start()
