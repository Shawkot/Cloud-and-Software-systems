# Use a build-time argument to specify the Python version
ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies and tools in a single RUN command
RUN apt-get update && \
    apt-get install -y gcc python3-dev && \
    pip install --no-cache-dir -r requirements.txt 

RUN pip install --upgrade pip

#RUN apt-get update && apt-get install -y python3-pip


# Copy the rest of the application code into the container
COPY . .

# Syntax check
#RUN python3 -m compileall .

# Linting
#RUN pylint your_script.py

# Unit testing
#RUN pytest && pytest --nbmake

# Build the wheel package
#RUN python setup.py bdist_wheel

# Specify the command to run on container start
#CMD ["python", "your_script.py"]
