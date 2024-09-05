# Use an official Python runtime as a parent image
FROM python:3.9-slim



ENV PORT=8052
ENV HOST=0.0.0.0
ENV WORKERS=5
ENV SERVER="app:server"


# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8050 to the outside world
EXPOSE ${PORT}

# Run the application using Gunicorn
CMD gunicorn -w ${WORKERS} -b "${HOST}:${PORT}" ${SERVER}