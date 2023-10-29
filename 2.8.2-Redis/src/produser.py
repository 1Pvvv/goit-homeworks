import pika
import connect
from faker import Faker
from models import Contact

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()

channel.exchange_declare(exchange="task_mock", exchange_type="direct")
channel.queue_declare(queue="emails", durable=True)
channel.queue_bind(exchange="task_mock", queue="emails")


def main():
    faker = Faker()
    for _ in range(9):
        contact = Contact(fullname=faker.name(), email=faker.email()).save()
        pk = str(contact.id).encode()

        channel.basic_publish(
            exchange="task_mock",
            routing_key="emails",
            body=pk,
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
        print(" [x] Sent %r" % pk)
    connection.close()


if __name__ == "__main__":
    main()
