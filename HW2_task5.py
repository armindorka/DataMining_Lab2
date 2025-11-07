## Task 5
# Run the clustering algorithms
# TODO: Run both the clustering algortihms for both spherical and non-sperical data (so in total 4 function calls)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_moons
from sklearn.decomposition import PCA
from collections import defaultdict
from scipy.spatial.distance import pdist, squareform
from scipy.stats import mode

kmeans_spherical = kmeans(spherical_data, 3, max_iters=100)
kmeans_nonspherical = kmeans(nonspherical_data, 3, max_iters=100)

agglomarative_spherical = agglomerative_clustering(spherical_data, 3)
agglomarative_nonspherical = agglomerative_clustering(nonspherical_data, 3)

# Compute and print the evaluation metrics
# TODO: Compute both the silhoutte scores and purity scores - each for both kmeans++ algorithm and aglomerative algorithm, for both datasets.
# So in total, 8 function calls. 
# Print all the 8 values.

print(f"KMeans Sil score, spherichal data: {silhouette_score(spherical_data, kmeans_spherical)}\nKMeans Sil score, nonspherichal data: {silhouette_score(nonspherical_data, kmeans_nonspherical)}")
print(f"Agglomarative Sil score, spherichal data: {silhouette_score(spherical_data, agglomarative_spherical)}\nAgglomarative Sil score, nonspherichal data: {silhouette_score(nonspherical_data, agglomarative_nonspherical)}")

print(f"KMeans Purity score, spherichal data: {purity_score(spherical_labels, kmeans_spherical)}\nKMeans Purity score, nonspherichal data: {purity_score(nonspherical_labels, kmeans_nonspherical)}")
print(f"Agglomarative Purity score, spherichal data: {purity_score(spherical_labels, agglomarative_spherical)}\nAgglomarative Purity score, nonspherichal data: {purity_score(nonspherical_labels, agglomarative_nonspherical)}")
