# Use an official Python 3.12.2 runtime as a parent image
FROM python:3.12.2-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install pytest for running tests (optional, if not already included in requirements.txt)
RUN pip install pytest

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
