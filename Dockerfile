FROM python:3.8

RUN apt-get update \
            && apt-get upgrade -y \
            && apt-get autoremove \
            && apt-get autoclean \
            && apt-get -y install postgresql-client \
            && mkdir app

COPY requirements.txt /app/
WORKDIR /app
RUN pip install --upgrade pip \
            && pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "start.py"]