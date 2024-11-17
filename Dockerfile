FROM python:3.10-slim


# environment variables #
ENV PORT=8052
ENV WORKERS=5
ENV HOST=0.0.0.0
ENV SERVER="app:server"


WORKDIR /app
COPY . /app

RUN pip install poetry
RUN poetry install

EXPOSE ${PORT}


CMD gunicorn -w ${WORKERS} -b "${HOST}:${PORT}" ${SERVER}