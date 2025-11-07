import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_moons

def generate_datasets():
    """Generates two datasets: one spherical and one non-spherical."""
    # TODO: Fill the missing code
    # Hint: Use make_blobs() method imported from sklearn.datasets
    # Both datasets should have 300 samples
    X_spherical, y_spherical = make_blobs() # There should be 3 centers, random_state=42
    X_nonspherical, y_nonspherical = make_moons() # noise=0.05, random_state=42
    return (X_spherical, y_spherical), (X_nonspherical, y_nonspherical)

# Load datasets
spherical_data, spherical_labels = generate_datasets()[0]
nonspherical_data, nonspherical_labels = generate_datasets()[1]
