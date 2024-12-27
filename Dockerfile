# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Mage
RUN pip install mage-ai dbt-core

# Copy the entire project into the container
COPY . .

# Expose the port Mage uses
EXPOSE 6789

# Set the command to start Mage
CMD ["mage", "start", "bike_demand_prediction"]
