# Pull base image
FROM python:3.8.5-slim-buster


# Set environment variables
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Set working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY . /code/


