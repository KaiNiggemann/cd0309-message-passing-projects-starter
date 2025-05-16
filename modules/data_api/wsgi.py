import os

from app import create_app


app, bus = create_app(os.getenv("FLASK_ENV") or "test")


if __name__ == "__main__":
    bus.run()
    app.run(debug=True)
