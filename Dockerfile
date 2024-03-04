# Use a Python base image
FROM public.ecr.aws/lambda/python:3.9

# Set a working directory
WORKDIR /var/task

# Copy your requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . .

# Set the command to run your application
CMD ["lambda_function.lambda_handler"]