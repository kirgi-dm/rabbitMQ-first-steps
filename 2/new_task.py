import sys
import pika
from pika.spec import BasicProperties

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or 'Hellow World!'
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=BasicProperties(
                          delivery_mode = pika.DeliveryMode.Persistent
                      ))
print(f' [x] {message}')
connection.close()

