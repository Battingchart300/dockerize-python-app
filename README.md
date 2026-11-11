# dockerize-python-app

Dockerize any Python app in minutes - Dockerfile, compose setup and a 3-step guide to run it anywhere.

## What is inside

- `Dockerfile` — Python 3.12 slim image, installs requirements, runs the app
- `docker-compose.yml` — one command to build and run, port 8000
- `app.py` — example Flask app (hello page on `/`)
- `requirements.txt` — dependencies for the example app
- `.dockerignore` — keeps cache and git files out of the image

## Quick start

```bash
git clone https://github.com/Battingchart300/dockerize-python-app
cd dockerize-python-app
docker compose up --build
```

Then open http://localhost:8000 — you should see `Hello from Docker!`

Stop with `Ctrl+C`, or `docker compose down`.

## Use it with your own app

1. Replace `app.py` with your app (keep it listening on `0.0.0.0:8000`).
2. Put your dependencies in `requirements.txt`.
3. Run `docker compose up --build`.

That is the whole template — no extra setup.

## Tech

Python 3.12, Flask, Docker, Docker Compose. Everything runs locally.

## License

MIT — see [LICENSE](LICENSE).
