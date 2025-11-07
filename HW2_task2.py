# TODO: Implement Kmeans++ algorithm from scratch
# Hint: You can take help from the kmeans++ algorithm implemented in the file "Clustering_Lab_With_Answers.ipynb". 
# The file is uploaded in nextiLearn. The code is a slightly different organization of that done in class. But the basic ideas are same.
# PLEASE DO NOT CHANGE THE NAMES OF FUNCTIONS AND PRESPECIFIED VARIABLES (for automated testing purpose).

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_moons
from sklearn.decomposition import PCA
from collections import defaultdict
from scipy.spatial.distance import pdist, squareform
from scipy.stats import mode

def initialize_centroids(X, k):
    """Initializes centroids using the KMeans++ strategy."""
    np.random.seed(42)
    centroids = []
    first_centroid = X[np.random.randint(X.shape[0])] # Fillup the blank space
    centroids.append(first_centroid)
    
    '''Write your code here'''
    for i in range(k-1):
        # Compute distances from each point to the nearest selected centroid
        distances = np.array([min([np.sqrt(np.sum((x - c) ** 2)) for c in centroids]) for x in X])

        # Compute probabilities proportional to squared distances
        probabilities = distances ** 2 / np.sum(distances ** 2)

        # Select the next centroid based on computed probabilities
        centroids.append(X[np.random.choice(X.shape[0], p=probabilities)])

    return np.array(centroids)

def assign_clusters(X, centroids):
    """Assigns each point to the nearest centroid."""
    distances = []
    for c in centroids:
        dist = np.sqrt(((X - c) ** 2).sum(axis=1))  # Calculate distance
        distances.append(dist)
    
    # TODO: Write the code to get the updated labels
    # Hint: convert distances to an np array, and the use argmin() function to get the labels
    labels = np.argmin(np.array(distances), axis = 0)
    return labels

def update_centroids(X, labels, k):
    """Recomputes centroids as the mean of assigned points."""
    new_centroids = []
    # TODO: Write your code here
    '''Hints: Iterate k times, and for each label (cluster), find the centroid of the cluster using mean() function. 
    Add the new centroid to the list new_centroids'''
    for i in range(k):
        new_centroids.append(X[labels == i].mean(axis = 0))
    return np.array(new_centroids)

def kmeans(X, k, max_iters=100):
    """Performs KMeans clustering."""
    centroids = initialize_centroids(X, k) # TODO: Fill in the missing arguments
    
    # TODO: Write your code here
    for i in range(max_iters):
        labels = assign_clusters(X, centroids)
        new_centroids = update_centroids(X, labels, k)
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    
    return labels
