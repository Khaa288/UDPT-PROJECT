from flask import json
import pika
from src.models import db_reward

def callback(ch, method, properties, body):
    data = json.loads(body)

    if properties.content_type == 'EmployeeUpdated':
        print(properties.content_type)

        db_reward.update_many(
            { 'Employee.EmployeeId': int(data['EmployeeId']) },
            { '$set':  {
                'Employee': {
                    'EmployeeId': int(data['EmployeeId']),
                    'EmployeeName': f'{data["FirstName"]} {data["MiddleName"]} {data["LastName"]}'
                }
            }},
        )

        print(" Received %s" % body.decode())
        print(" Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)

def subscribe_message():
    try:
        credentials = pika.PlainCredentials('guest', 'guest')
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials))
        print("Connected to RabbitMq service")
    except pika.exceptions.AMQPConnectionError as exc:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")
        return

    channel = connection.channel()

    subcribe_queue = channel.queue_declare(queue='Reward_EmployeeUpdatedQueue', exclusive=True)

    channel.queue_bind(exchange='EmployeeUpdated', queue=subcribe_queue.method.queue)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=subcribe_queue.method.queue, on_message_callback=callback)
    channel.start_consuming()
    
    connection.close()