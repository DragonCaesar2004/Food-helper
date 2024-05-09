# Food-helper
Web-site with nutrition AI-consultant 

##Установка:

'''
virtualenv venv 
'''

'''
.\venv\Scripts\activate
'''

Заходим в какой-либо .py файл и снизу справа нажимаем на версию python. Далее сверху выбираем интерпретатор из созданного виртуального окружения в Food-helper

'''
pip install django
'''

Миграции (позже)


##Установка PostgreSQL:

https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
(последняя версия)


При установке имя: user
пароль: 141414
порт: 5432 
В конце не ставим галочку


Находим в пуске postgresq и открвыаем pgAdmin4
Выбираем слева login/Group roles (правой кнопкой мыши) -> create ->  login/Group role и вводи в General имя, Definiteion пароль, в Priveleges все галочки кроме предпоследеней и в конце save.

'''
pip install psycopg2
'''

И python manage.py runserver 