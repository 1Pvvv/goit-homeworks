import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 8080
MESSAGE = "Python Web development"

def send_message(msg, sock, server):
    data = msg.encode()
    sock.sendto(data, server)
    print(f'Send data: {data.decode()} to server: {server}')
    response, address = sock.recvfrom(1024)
    print(f'Response data: {response.decode()} from address: {address}')


def run_client(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    while True:
        data = input("Введи запрос: ")
        if data == 'exit':
            sock.sendto(data.encode(), server)
            break
        else:
            send_message(data, sock, server)
    sock.close()


if __name__ == '__main__':
    run_client(UDP_IP, UDP_PORT)