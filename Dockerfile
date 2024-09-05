# Use an official Python runtime as a parent image
FROM python:3.9-slim


# Environmental variables #
ENV PORT=8050
ENV HOST=0.0.0.0


# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8050 for the Dash app
EXPOSE ${PORT}

# Run the Dash app
CMD ["python", "app.py"]
