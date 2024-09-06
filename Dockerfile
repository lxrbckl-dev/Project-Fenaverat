FROM python:3.9-slim


# environment variables #
ENV PORT=8052
ENV HOST=0.0.0.0
ENV WORKERS=5
ENV SERVER="app:server"


WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE ${PORT}


CMD gunicorn -w ${WORKERS} -b "${HOST}:${PORT}" ${SERVER}