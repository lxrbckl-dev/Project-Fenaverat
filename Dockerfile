FROM python:3.10-slim

# Runtime configuration (can be overridden at `docker run` time)
ENV PORT=8048
ENV WORKERS=1
ENV HOST="0.0.0.0"
ENV SERVER="app:server"

# Application Configuration
ENV PROJECT_NAME="Project Fenaverat"

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE ${PORT}

CMD gunicorn -w ${WORKERS} -b "${HOST}:${PORT}" ${SERVER}