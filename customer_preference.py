from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# Sample customer preference data
data = {
    'customer_id': [1, 2, 3, 4, 5],
    'teddy_bear_type': [1, 2, 1, 2, 3],  # 1: Teddy Bear A, 2: Teddy Bear B, 3: Teddy Bear C
    'quantity': [2, 1, 3, 2, 1]
}

df = pd.DataFrame(data)

# Apply K-Means Clustering to find customer preferences
kmeans = KMeans(n_clusters=2)  # Assuming 2 clusters for simplicity
df['cluster'] = kmeans.fit_predict(df[['teddy_bear_type', 'quantity']])

# Visualize the clusters
plt.scatter(df['teddy_bear_type'], df['quantity'], c=df['cluster'])
plt.title('Customer Preference Clustering')
plt.xlabel('Teddy Bear Type')
plt.ylabel('Quantity')
plt.show()

# Print cluster results
print(df)
