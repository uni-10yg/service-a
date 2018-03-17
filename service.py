import pika, json
from logger import root_logger
from db import Database


logger = root_logger.getChild(__name__)

db = Database()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()


channel.queue_declare(queue='comm_queue')

def callback(ch, method, properties, body):
    logger.info(" [x] Received %r" % body)
    body_dict = json.loads(body.decode())
    db.insert(body_dict.get('hash'), body_dict.get('salt'))
    logger.debug(db.selectAll())

channel.basic_consume(
    callback,
    queue='comm_queue',
    no_ack=True
)

channel.start_consuming()