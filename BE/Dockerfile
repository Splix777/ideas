# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install additional dependencies, including django-sslserver
RUN pip install django-sslserver

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the port that Daphne will run on
EXPOSE 8000

# Copy the Django project into the container
COPY . /app/

# Copy the entrypoint script into the container
COPY entrypoint.sh /app/entrypoint.sh
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/entrypoint.sh
RUN chmod +x /app/wait-for-it.sh


# Run the entrypoint script when the container starts
ENTRYPOINT ["/app/entrypoint.sh"]
