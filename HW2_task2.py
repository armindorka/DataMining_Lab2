import numpy as np

# TODO: Implement Kmeans++ algorithm from scratch
# Hint: You can take help from the kmeans++ algorithm implemented in the file "Clustering_Lab_With_Answers.ipynb". 
# The file is uploaded in nextiLearn. The code is a slightly different organization of that done in class. But the basic ideas are same.
# PLEASE DO NOT CHANGE THE NAMES OF FUNCTIONS AND PRESPECIFIED VARIABLES (for automated testing purpose).

def initialize_centroids(X, k):
    """Initializes centroids using the KMeans++ strategy."""
    np.random.seed(42)
    centroids = []
    first_centroid = _____ # Fillup the blank space
    centroids.append(first_centroid)
    
    '''Write your code here'''
    
    return np.array(centroids)

def assign_clusters(X, centroids):
    """Assigns each point to the nearest centroid."""
    distances = []
    for c in centroids:
        dist = ____ # Calculate distance
        distances.append(dist)
    
    # TODO: Write the code to get the updated labels
    # Hint: convert distances to an np array, and the use argmin() function to get the labels
    return labels

def update_centroids(X, labels, k):
    """Recomputes centroids as the mean of assigned points."""
    new_centroids = []
    # TODO: Write your code here
    '''Hints: Iterate k times, and for each label (cluster), find the centroid of the cluster using mean() function. 
    Add the new centroid to the list new_centroids'''
    return np.array(new_centroids)

def kmeans(X, k, max_iters=100):
    """Performs KMeans clustering."""
    centroids = initialize_centroids(__) # TODO: Fill in the missing arguments
    
    # TODO: Write your code here
    
    return labels