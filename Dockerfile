FROM python:3.10-slim

# Environment variables
ENV PORT=8058
ENV WORKERS=5
ENV HOST=0.0.0.0
ENV SERVER="app:server"

WORKDIR /app
COPY . /app

RUN pip install pipenv
RUN pipenv install

EXPOSE ${PORT}

# Use Poetry to run gunicorn
CMD pipenv run gunicorn -w ${WORKERS} -b "${HOST}:${PORT}" ${SERVER}
