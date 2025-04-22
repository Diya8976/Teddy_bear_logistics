import folium
import pandas as pd

# Sample order data with latitude and longitude
data = {
    'order_id': [1, 2, 3, 4, 5],
    'city': ['Delhi', 'Mumbai', 'Kolkata', 'Bangalore', 'Chennai'],
    'latitude': [28.7041, 19.0760, 22.5726, 12.9716, 13.0827],
    'longitude': [77.1025, 72.8777, 88.3639, 77.5946, 80.2707]
}

df = pd.DataFrame(data)

# Initialize a map centered at India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add markers for each order's location
for index, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"Order ID: {row['order_id']}<br>City: {row['city']}",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Save the map to an HTML file
m.save('orders_map.html')
print("Geospatial order analysis map saved as orders_map.html.")
