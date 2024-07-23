# Use an official Python image as a base
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY /Users/ilabetaev/RSMU_bot/RSMU_bot/requirements.txt /app

RUN pip install --upgrade pip
# Install dependencies
RUN pip install -r /app/requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8000