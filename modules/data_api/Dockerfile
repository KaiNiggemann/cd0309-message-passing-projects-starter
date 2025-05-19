FROM python:3.9-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev librdkafka-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5001
EXPOSE 5005

COPY . .
#CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5001"]
CMD ["python", "wsgi.py"]

