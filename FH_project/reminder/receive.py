import pika
import traceback
import sys
import os
import ssl
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

def get_elems():
    load_dotenv()

    email_sender = "foodhelperproject@gmail.com"
    email_password = os.getenv('EMAIL_HOST_PASSWORD')
    email_subject = "Не забудьте правильно питаться!"
    email_text = 'http://127.0.0.1:8000/'
    context = ssl.create_default_context()

    def send_email(email_receiver):
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = email_subject
        em.set_content(email_text)

        with smtplib.SMTP_SSL('smtp.gmail.com', port=465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        print(f"Email sent successfully to {email_receiver}")

    def callback(ch, method, properties, body):
        email_receiver = body.decode()
        send_email(email_receiver)

    conn_params = pika.ConnectionParameters('localhost', 5672)
    connection = pika.BlockingConnection(conn_params)
    channel = connection.channel()
    channel.queue_declare(queue='first-queue')
    channel.basic_consume(queue='first-queue', on_message_callback=callback, auto_ack=True)

    try:
        print('Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Interrupted')
        connection.close()
    except Exception:
        connection.close()
        traceback.print_exc(file=sys.stdout)
