FROM python:3.9-alpine

WORKDIR .

RUN apk update
RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev librdkafka-dev python3-dev
RUN export C_INCLUDE_PATH=/usr/local/Cellar/librdkafka/2.2.0/include
RUN export LIBRARY_PATH=/usr/local/Cellar/librdkafka/2.2.0/lib
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "app.py"]
