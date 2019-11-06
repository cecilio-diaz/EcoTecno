FROM python:3.6
ENV PYTHONUNBUFFERED 1

# COPIANDO ARCHIVOS.
RUN mkdir -p /django_app
WORKDIR /django_app
COPY . .
RUN pip install -r requirements.txt

# MIGRACIONES
CMD python senddata.py 'http://90.147.184.214'
