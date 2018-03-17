import pika, logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_handler = logging.StreamHandler()
log_handler.setFormatter(logging.Formatter(fmt='%(asctime)s: %(message)s', datefmt='%m.%d.%Y %I:%M:%S %p'))
logger.addHandler(log_handler)


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()


channel.queue_declare(queue='comm_queue')

def callback(ch, method, properties, body):
    logger.info(" [x] Received %r" % body)

channel.basic_consume(
    callback,
    queue='comm_queue',
    no_ack=True
)

logger.info(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()