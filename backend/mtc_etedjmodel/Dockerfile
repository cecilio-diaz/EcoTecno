FROM python:3.6
ENV PYTHONUNBUFFERED 1

# COPIANDO ARCHIVOS.
RUN mkdir -p /django_app
WORKDIR /django_app
COPY . .
RUN pip install -r requirements.txt

# MIGRACIONES
#RUN python manage.py  makemigrations --noinput; exit 0
#RUN python manage.py  migrate --noinput; exit 0
