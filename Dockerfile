
FROM python:3.9 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.9

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./migrations /code/migrations

COPY ./alembic.ini /code/alembic.ini

COPY ./app /code/app

CMD uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port $PORT
