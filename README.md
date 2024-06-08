# Food-helper
Web-site with nutrition AI-consultant 

## Установка:

``` python -m venv venv ``` 

``` .\venv\Scripts\activate ```


Создайте файл .env в корневой папке FH_project, и запишите там переменные окружения:

EMAIL_HOST_PASSWORD = 'Ваш пароль от почты' 
PASSWORD='Ваш пароль от PostgreSQL'


Заходим в какой-либо .py файл и сверху в поиске набираем: >select

Выбираем интерпретатор Python из виртуального окружения в FH_project


``` pip install -r requirements.txt ```


Миграции:
Удалить все файлы кроме __init__.py в папке users/migratitons.py

```python manage.py makemigrations```

```python manage.py migrate```

Запуск:

```python manage.py runserver ```


## Установка PostgreSQL:

https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
(последняя версия)


При установке имя: user
пароль: находится в .env
порт: 5432 
В конце не ставим галочку

прописать построчно в SQL Shell (psql)

```CREATE DATABASE fh_db; ```

```CREATE ROLE django_admin with password '141414';```

```ALTER ROLE "django_admin" WITH LOGIN;```

```GRANT ALL PRIVILEGES ON DATABASE "fh_db" to django_admin;```

```ALTER USER django_admin CREATEDB;```

```\c fh_db```

```GRANT ALL ON schema public TO django_admin;```

## Установка RabbitMQ:

Для запуска на вашем устройстве нужно установить ErLang (https://www.erlang.org/downloads) и RabbitMQ (https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.13.2/rabbitmq-server-3.13.2.exe) (ссылка для Windows) 

После установки нужно прописать 
 ```rabbitmq-plugins enable rabbitmq_management```
В командной строке администратора, по адресу: 
```место установки rabbitmq\RabbitMQ Server\rabbitmq_server-3.13.2\sbin```

Чтобы проверить, что rabbitMQ корректно работает можете в браузере в поисковой строке написать
 http://localhost:15672

логин: guest
пароль: guest
заходить необязательно, главное, чтобы загрузилась страница
