# Use an official Python runtime as a parent image
FROM python:3.11.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# RUN apt-get update && apt-get install -y \
#     gcc \
#     python3-dev \
#     && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install flask flask_cors gunicorn requests pymongo

# Make port 5000 available to the world outside this container
EXPOSE 5001

# Use gunicorn as the production server
CMD ["gunicorn", "-b", "0.0.0.0:5001", "server:app"]

