import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    N = data.shape[0]
    eigenvalue, eigenvector = 0, np.random.uniform(-1, 1, N)
    for __ in range(num_steps):
        eigenvector = data@eigenvector / np.linalg.norm(data@eigenvector)
        eigenvalue = eigenvector@data@eigenvector / np.linalg.norm(eigenvector)**2
    return float(eigenvalue), eigenvector