FROM python:3.8-alpine

WORKDIR /app

COPY . .

RUN apk update && \
    apk add sqlite && \
    pip install Flask Flask-SQLAlchemy

CMD [ "python", "app.py" ]
