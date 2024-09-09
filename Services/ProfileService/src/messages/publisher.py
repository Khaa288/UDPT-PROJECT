import pika

def publish_message(message, event):
    try:
        credentials = pika.PlainCredentials('guest', 'guest')
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials))
    except pika.exceptions.AMQPConnectionError as exc:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")
        return

    channel = connection.channel()

    properties = pika.BasicProperties(event)

    channel.basic_publish(
        exchange=event,
        routing_key='',
        body=message,
        properties=properties
    )
   
    connection.close()
    
    print ("Message sent: ", message)
