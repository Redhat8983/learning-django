FROM python:3.9.9-slim
WORKDIR /myapp

# set environment variables
# do not place here  in production enviroment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# TODO: Is posible to put create superuser in dokcer-compose ?
ENV DJANGO_DB_NAME=default
ENV DJANGO_SU_NAME=admin
ENV DJANGO_SU_EMAIL=admin@examle.com
ENV DJANGO_SU_PASSWORD=admin

# install dependencies
RUN pip install --upgrade pip 
COPY ./src /myapp
RUN pip install -r requirements.txt

# set run django admin
RUN python -c "import os; os.environ['DJANGO_SETTINGS_MODULE']= 'mb_project.settings'; \
    import django; django.setup(); \
    from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
    get_user_model()._default_manager.db_manager('$DJANGO_DB_NAME').create_superuser( \
    username='$DJANGO_SU_NAME', \
    email='$DJANGO_SU_EMAIL', \
    password='$DJANGO_SU_PASSWORD')"

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000