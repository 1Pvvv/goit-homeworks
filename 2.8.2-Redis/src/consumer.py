import pika
import time
import connect
from bson import ObjectId
from models import Contact

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()

channel.queue_declare(queue="emails", durable=True)
print(" [*] Waiting for tasks. To exit press CTRL+C")


def send_message(obj):
    contact = Contact.objects(id=obj).first()
    if contact:
        contact.update(sent=True)
        time.sleep(1)
        contact.save()
    else:
        print("\nThere is no contact\n")


def callback(ch, method, properties, body):
    pk = ObjectId(body.decode())
    print(f" [x] Received {pk}")
    send_message(pk)
    print(f" [x] Sent: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="emails", on_message_callback=callback)


if __name__ == "__main__":
    channel.start_consuming()
