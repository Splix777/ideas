#!/bin/bash

# Wait for the PostgreSQL database to be ready
./wait-for-it.sh db:5432 --timeout=30

# Install python3 virtual environment
python3 -m venv venv

# Turn on python3 virtual environment
source venv/bin/activate

pip install --upgrade pip
python3 -m pip install --upgrade pip setuptools wheel

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt


# Create a Django project
if [ ! -d "$PROJECT_DIR" ]; then
    django-admin startproject server
else
    echo "Project directory '$PROJECT_DIR' already exists. Skipping project creation."
fi

# Print current working directory for debugging
cd server

# Make and Apply database migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Collect static files
# python3 manage.py collectstatic --noinput

# Create a superuser (replace 'your_superuser_password' with the actual environment variable name)
python3 manage.py createsuperuser --username="$POSTGRES_USER" --email=admin@example.com --noinput

# Start the Django development server
python3 manage.py runsslserver 0.0.0.0:8000
