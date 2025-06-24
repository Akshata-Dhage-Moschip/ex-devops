# Use a lightweight Python image
FROM python:3.10-slim
 
# Set working directory
WORKDIR /app
 
# Copy requirements and install them
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
 
# Copy the app code
COPY . .
 
# Expose the port Flask will run on
EXPOSE 5000
 
# Run the application
CMD ["python", "app.py"]
