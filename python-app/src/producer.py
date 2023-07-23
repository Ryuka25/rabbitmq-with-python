#!/usr/bin/env python
import os
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(os.environ.get("RABBITMQ_HOST"))
)

channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")

print("[x] Sent 'Hello World!'")

connection.close()
