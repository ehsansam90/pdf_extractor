# Use an official Python 3.11.2 slim image
FROM python:3.11.2-slim

# Set the working directory inside the container
WORKDIR /app

# Copy required files
COPY requirements.txt ./
COPY app.py extractor.py model.py ./
COPY templates/ templates/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask app port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
