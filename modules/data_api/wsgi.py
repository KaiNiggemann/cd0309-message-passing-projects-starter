import os

from flask_kafka import FlaskKafka
from app import create_app


app = create_app(os.getenv("FLASK_ENV") or "test")
bus = FlaskKafka()
bus.init_app(app)

if __name__ == "__main__":
    bus.run()
    app.run(debug=True)
