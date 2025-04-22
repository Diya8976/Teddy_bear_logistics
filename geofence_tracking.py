from geopy.distance import geodesic
import folium

# --- Predefined Geofence Settings ---
geofence_center = (28.7041, 77.1025)  # Warehouse (Delhi)
geofence_radius = 0.05  # Radius in kilometers (50 meters)

# --- Simulated Teddy Bear GPS Coordinates ---
teddy_bear_location = (28.7051, 77.1028)  # Example test coordinates

# --- Check if Inside Geofence ---
def is_inside_geofence(current_location):
    distance = geodesic(geofence_center, current_location).km
    return distance <= geofence_radius, distance

# --- Run the Check ---
inside_status, actual_distance = is_inside_geofence(teddy_bear_location)

print(f"Teddy Bear Coordinates: {teddy_bear_location}")
print(f"Distance to Warehouse: {actual_distance:.4f} km")
print(f"Inside Geofence: {'Yes ✅' if inside_status else 'No ❌'}")

# --- Optional Map Output ---
def generate_map():
    map_obj = folium.Map(location=geofence_center, zoom_start=17)
    
    folium.Circle(
        location=geofence_center,
        radius=geofence_radius * 1000,  # Convert km to meters
        color='green',
        fill=True,
        fill_opacity=0.2,
        tooltip="Geofence Area"
    ).add_to(map_obj)

    folium.Marker(
        location=teddy_bear_location,
        popup="Teddy Bear",
        icon=folium.Icon(color="blue", icon="paw")
    ).add_to(map_obj)

    map_obj.save("geofence_map.html")
    print("[✔] Map saved as geofence_map.html")

generate_map()
