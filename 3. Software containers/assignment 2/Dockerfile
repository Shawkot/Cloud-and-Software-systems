# Use a build-time argument to specify the Python version
ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim

# Set the working directory in the container
WORKDIR /app
COPY . .

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-pip \
    gcc \
    python3-dev && \
    #pip3 install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install pylint pytest nbmake wheel 
#RUN pip install --upgrade pip
