from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load Iris dataset
iris = load_iris()

X = iris.data

# Create K-Means model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Train the model
model.fit(X)

# Get cluster labels
clusters = model.labels_

# Get centroids
centroids = model.cluster_centers_

# Print results
print("=" * 40)
print("K-Means Clustering - Iris Dataset")
print("=" * 40)

print("\nCluster Labels:")
print(clusters)

print("\nCentroids:")
print(centroids)

# Visualize clusters
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=clusters
)

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="X",
    s=200
)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering - Iris Dataset")

plt.savefig("images/kmeans_clusters.png", dpi=300)

plt.show()