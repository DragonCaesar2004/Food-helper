import pika
from main.utils import get_user_emails

# Установка параметров соединения с RabbitMQ.
# 'localhost' означает, что RabbitMQ работает на локальной машине.
# 5680 - это порт, на котором работает RabbitMQ.
def send_to_rabbitmq():
    # Установка соединения с RabbitMQ с использованием заданных параметров.
    conn_params = pika.ConnectionParameters('localhost', 5672)

    # Создание канала, через который будет происходить взаимодействие с RabbitMQ.
    connection = pika.BlockingConnection(conn_params)

    # Создание канала, через который будет происходить взаимодействие с RabbitMQ.
    channel = connection.channel()

     # Объявление очереди с именем 'first-queue'.
    # Если такая очередь уже существует, то она не будет создана заново.
    channel.queue_declare(queue='first-queue')

    for email_receiver in get_user_emails():
        # Отправка сообщения в очередь 'first-queue'.
        # exchange='' указывает на использование стандартного обменника.
        # routing_key='first-queue' указывает, в какую очередь отправить сообщение.
        # body='Hi, consumer!' - это тело сообщения.
        channel.basic_publish(exchange='',
                              routing_key='first-queue',
                              body=email_receiver)



        # Вывод сообщения в консоль для подтверждения отправки.
    
        # Задержка на 2 секунды перед отправкой следующего сообщения.
    
    # Закрытие соединения с RabbitMQ.
    connection.close()
