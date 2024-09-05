# # Use an official Python runtime as a parent image
# FROM python:3.9-slim

# # Environmental variables
# ENV PORT=8059
# ENV HOST=0.0.0.0
# ENV SERVER=app:server
# ENV WORKERS=1

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Expose port 8156 for the Dash app
# EXPOSE ${PORT}

# # Run the Dash app with Gunicorn
# CMD gunicorn -w ${WORKERS} -b "${HOST}:${PORT}" ${SERVER}



# Use an official Python runtime as a parent image
FROM python:3.9-slim



ENV PORT=8052
ENV HOST=0.0.0.0



# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8050 to the outside world
EXPOSE 8052

# Run the application using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8052", "app:server"]
