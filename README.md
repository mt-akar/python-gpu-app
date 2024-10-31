# Intro
This is a simple python program that uses GPU to make dumb compute operations.

It is created to test cuda operations and collect GPU usage metrics.

# Prerequisites
- Install Docker
- Install Python

# Run the image
```bash
docker --version
python3 --version

pip install numpy
pip install torch

git clone https://github.com/mt-akar/python-gpu-app.git
sudo docker build -t python-gpu-app .
sudo docker run --gpus all python-gpu-app
```