"""Example app for the dockerize-python-app template.

Runs on http://localhost:8000 when the container is up.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello from Docker! This Python app runs in a container."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
