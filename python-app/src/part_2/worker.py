import os
import sys
import time

import pika


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(os.environ.get("RABBITMQ_HOST"))
    )
    channel = connection.channel()

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        time.sleep(body.count(b"."))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # queue is durable between rabbitmq node restart
    channel.queue_declare(queue="task_queue", durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue="task_queue",
        on_message_callback=callback,
    )

    print(" [x] Waiting for messages. To exit press CTRL+C")

    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
