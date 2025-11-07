# Task 4: Performance Evaluation
#Internal Evaluation using Silhouette score

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_moons
from sklearn.decomposition import PCA
from collections import defaultdict
from scipy.spatial.distance import pdist, squareform
from scipy.stats import mode

# Fill up the missing codes to implement Silhoutte score evaluation from scratch
from sklearn.metrics import pairwise_distances

def silhouette_score(X, labels):
    """Computes silhouette score for clustering."""
    distances = pairwise_distances(X) #TODO, Hint: Find pairwise distances in X using the function pairwise_distances(...)
    unique_labels = np.unique(labels) # From the labels, find the unique labels using the function np.unique(...)
    
    # Compute intra-cluster distance (a)
    a = []
    for i in range(len(X)):
        same_cluster = labels == labels[i]  # Mask for same cluster points
        intra_distances = distances[i, same_cluster] # TODO, Hint: Get distances to same cluster points
        avg_distance = np.mean(intra_distances) # TODO, Hint:Compute mean value of intra_distances
        a.append(avg_distance) 
    a = np.array(a)
    
    # Compute nearest-cluster distance (b)
    b = []
    for i in range(len(X)):
        other_cluster_distances = []  # Store avg distances to other clusters
        for l in unique_labels:
            if  l != labels[i]: # TODO, Hint: Write a condition to skip same clusters
                # TODO, Hint: Mask for other cluster (like in previous loop)
                other_cluster_mask = labels == l
                cluster_distances = distances[i, other_cluster_mask] # TODO, Hint: Extract distances with other cluster mask
                if cluster_distances.size > 0:  # Ensure it's not empty
                    avg_distance = np.mean(cluster_distances) # TODO, Hint: Compute mean distance
                    other_cluster_distances.append(avg_distance) 
        # Handle the case where other_cluster_distances is empty
        if other_cluster_distances:
            min_distance = min(other_cluster_distances) # TODO, Hint: Compute minimum of other_cluster_distances if the list is not empty
        else:
            min_distance = 0  # Default value when no other clusters exist
        b.append(min_distance)  # Take the minimum avg distance
    b = np.array(b)
    
    return np.mean((b - a) / np.maximum(a, b))

#External Evaluation using purity score
from sklearn import metrics
def purity_score(y_true, y_pred):
    # TODO: Write the code to calculate purity score
    # Hint: Use the exercise in lab class.
    contingency_matrix = metrics.cluster.contingency_matrix(y_true, y_pred)  
    purity = np.sum(np.amax(contingency_matrix, axis=0)) / np.sum(contingency_matrix) 
    return purity
