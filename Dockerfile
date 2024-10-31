# Use PyTorch's official CUDA base image
FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install any additional dependencies (numpy and torch are pre-installed with the image)
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "./app.py"]