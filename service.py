import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()


channel.queue_declare(queue='comm_queue')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(
    callback,
    queue='comm_queue',
    no_ack=True
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()