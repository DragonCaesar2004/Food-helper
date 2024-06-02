FROM python:latest
COPY . /app/
WORKDIR /app/
RUN pip install -r requirements.txt
WORKDIR /app/FH_project
EXPOSE 8000
ENV PYTHONUNBUFFERED=1
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]