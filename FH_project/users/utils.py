# import smtplib

# def send_email(message, receiver):
#     sender = "foodhelperproject@gmail.com"
#     password = "omep qscs vvaq ifwn"
#     # password = os.getenv("omep qscs vvaq ifwn")

#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()

#     try:
#         server.login(sender, password)
#         msg = MIMEText(message)
#         msg["Subject"] = "ВАШ НОВЫЙ ПАРОЛЬ"
#         server.sendmail(sender, receiver, msg.as_string())

#         # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")

#         return "The message was sent successfully!"
#     except Exception as _ex:
#         return f"{_ex}\nCheck your login or password please!"

