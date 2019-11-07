FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /python-data-faker
WORKDIR /python-data-faker
COPY requirements.txt /python-data-faker/requirements.txt
RUN pip install -r requirements.txt
COPY senddata.py /python-data-faker/senddata.py