import torch
import time

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Create random matrices for trivial GPU processing
matrix_size = (1000, 1000)

# Allocate matrices on the GPU
matrix1 = torch.randn(matrix_size, device=device)
matrix2 = torch.randn(matrix_size, device=device)

# Function to do trivial processing on GPU
def gpu_process():
    # Perform a matrix multiplication, which is trivial but GPU-intensive
    result = torch.matmul(matrix1, matrix2)
    return result

# Run the GPU process every second
while True:
    start_time = time.time()
    gpu_process()
    end_time = time.time()
    print(f"Processed on GPU in {end_time - start_time:.6f} seconds.")
    time.sleep(0.5)