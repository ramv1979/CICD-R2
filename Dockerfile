# Start with a python base image
# Take your pick from https://hub.docker.com/_/python
FROM python:3.11-slim

# Set /app as the main application directory
WORKDIR /cicd-workflows

# Copy the requirements.txt file and required directories into docker image
COPY ./requirements.txt /app/requirements.txt
COPY ./src /app/src
COPY ./model /app/model

# Add /src directory to PYTHONPATH, so that model.py Python module can be found
# To add multiple directories, delimit with colon e.g. /app/src:/app
ENV PYTHONPATH /app/src

# Install python package dependancies, without saving downloaded packages locally
RUN pip install -r /app/requirements.txt --no-cache-dir

# Allow port 80 to be accessed (app)
EXPOSE 80

# Start the app using gunicorn
CMD ["gunicorn", "--bind=0.0.0.0:80", "src.app:app"]
