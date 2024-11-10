# Use the rabbitmq:4.0-management base image
FROM rabbitmq:4.0-management

# Switch to root user to install dependencies
USER root

# Set the working directory
WORKDIR /app

# Install Python and virtual environment support
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    nano \
    && apt-get clean

# Create and activate a virtual environment
RUN python3 -m venv venv

# Copy requirements and install them in the virtual environment
COPY requirements.txt .
RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose ports for RabbitMQ (management UI and message broker)
EXPOSE 15672 5672

# Command to run your Python application using the virtual environment

