ARG PYTHON_VERSION=3.10-slim-buster

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY . /code

ENV SECRET_KEY "7teaFHspejYuM9Dvqg9MQmwmBtDJogiZcqV5eBklkXAJ52DIES"
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
RUN python manage.py makemigrations

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "My_Portfolio.wsgi"]
