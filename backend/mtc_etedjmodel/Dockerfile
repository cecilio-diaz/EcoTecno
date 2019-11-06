FROM python:3.6

# COPIANDO ARCHIVOS.
RUN mkdir -p /django_app
WORKDIR /django_app
COPY . .
RUN pip install -r requirements.txt

# MIGRACIONES
RUN python manage.py  makemigrations --noinput; exit 0
RUN python manage.py  migrate --noinput; exit 0

# CONFIUGURANDO USARIO Y CONTRASENA POR DEFECTO (ADMIN)

# CARGAR DATOS DE BACKUP

# CONFIGURAR DATOS DE CONEXION A LA DB
ARG IP
ARG PUERTO
ARG USER
ARG PASSWORD
ARG DB
#RUN python config.py "${IP}"  "${PUERTO}"   "${USER}"  "${PASSWORD}"   "${DB}"

# EJECUTANO DJANGO.
# CMD python /django_app/backups runserver 0.0.0.0:8000

CMD ${EJECUTAR}
