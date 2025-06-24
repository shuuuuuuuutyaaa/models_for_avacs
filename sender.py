import pika

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters(host='localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='test_queue', durable=True)

for i in range(5):
    message = f"Сообщение #{i+1}"
    channel.basic_publish(
        exchange='',
        routing_key='test_queue',
        body=message,
        properties=pika.BasicProperties(delivery_mode=2)
    )
    print(f"[x] Отправлено: {message}")

connection.close()
