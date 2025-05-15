FROM python:3.9-alpine

WORKDIR .

RUN sed -i -e 's/v3.4/edge/g' /etc/apk/repositories
RUN apk upgrade --update-cache --available
RUN apk add --no-cache librdkafka-dev python3-dev

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
RUN export C_INCLUDE_PATH=/usr/local/Cellar/librdkafka/2.2.0/include
RUN export LIBRARY_PATH=/usr/local/Cellar/librdkafka/2.2.0/lib
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install --prefer-binary confluent-kafka
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "app.py"]
