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

#IF EXITING WITH CTRL+C AND GET ERROR (137)

# A Docker container that exits with a status code of 137 usually indicates that the process running in the
# container was terminated by a signal. The number 137 specifically corresponds to signal 9 (SIGKILL).
# This signal is often sent forcefully to terminate a process.

# When you use Ctrl+C to stop a Docker container in the terminal, it sends a SIGINT signal to the main process running in the container,
# giving it a chance to perform cleanup operations. If the process doesn't handle SIGINT gracefully and doesn't exit in a
# reasonable amount of time, Docker may resort to sending a SIGKILL signal to forcefully terminate the process.

# Here are a few reasons why this might happen:

# Process not handling SIGINT: The main process running in your container might not be handling the SIGINT signal correctly.
# It's a good practice for processes to catch this signal and perform any necessary cleanup before exiting.

# Long cleanup time: If the cleanup operation takes a long time to complete, Docker might resort to sending a SIGKILL.
# Ensure that your cleanup operations are efficient.

# Potential resource constraints: If the container is running out of resources (memory, for example), it might be terminated
# forcefully.