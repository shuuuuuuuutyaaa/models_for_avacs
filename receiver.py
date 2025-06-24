import pika

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters(host='localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='test_queue', durable=True)

def callback(ch, method, properties, body):
    print(f"[x] Получено сообщение: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='test_queue', on_message_callback=callback)

print('[*] Ожидание сообщений. Для выхода нажмите CTRL+C')
channel.start_consuming()
