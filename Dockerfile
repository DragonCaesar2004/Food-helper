FROM python:3.10
COPY . /app/
WORKDIR /app/
RUN pip install -r requirements.txt
WORKDIR /app/FH_project
ENV PYTHONUNBUFFERED=1
RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver","--noreload", "0.0.0.0:8000"]