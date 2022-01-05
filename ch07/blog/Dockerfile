# Before django start :
# python manage.py migrate 
# python manage.py createsuperuser
# python manage.py makemigration blog (option)
# python manage.py migrate blog       (option)

FROM python:3.9.9-slim
WORKDIR /myapp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./src /myapp
RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000