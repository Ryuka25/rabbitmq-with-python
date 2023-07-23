#!/usr/bin/env python
import os
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(os.environ.get("RABBITMQ_HOST"))
)

channel = connection.channel()

channel.queue_declare(queue="hello")

print("Enter your message (Type 'q!' to exit)")
while True:
    message = input("> ")
    if message == "q!":
        break
    channel.basic_publish(exchange="", routing_key="hello", body=f"{message}")

    print(f"[x] Sent '{message}'")

connection.close()
