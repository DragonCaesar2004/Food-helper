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


Находим в пуске postgresq и открвыаем pgAdmin4
Выбираем слева login/Group roles (правой кнопкой мыши) -> create ->  login/Group role и вводи в General имя, Definiteion пароль, в Priveleges все галочки кроме предпоследеней и в конце save.

