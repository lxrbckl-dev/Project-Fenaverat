FROM python:3.10-slim

# environment variables <
ENV PORT=8058
ENV WORKERS=5
ENV HOST=0.0.0.0
ENV SERVER="app:server"

ENV PROJECT_NAME=${PROJECT_NAME}
ENV GITHUB_EMAIL=${GITHUB_EMAIL}
ENV GITHUB_TOKEN=${GITHUB_TOKEN}
ENV PROJECT_VERSION=${PROJECT_VERSION}

# >

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE ${PORT}

# use Poetry to run gunicorn
CMD gunicorn -w ${WORKERS} -b "${HOST}:${PORT}" ${SERVER}