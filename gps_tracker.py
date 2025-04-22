import requests
import time
import pandas as pd
from datetime import datetime

# Your Google Maps API Key
API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

# Function to get current location based on coordinates (simulating GPS tracking)
def get_location(latitude, longitude):
    params = {
        'latlng': f'{latitude},{longitude}',
        'key': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if data['status'] == 'OK':
        return data['results'][0]['formatted_address']
    else:
        return "Location not found"

# Simulated GPS Coordinates (For real-world implementation, get real GPS data)
coordinates = [(28.7041, 77.1025), (28.5355, 77.3910), (28.4089, 77.3178)]  # Delhi, Gurgaon, Noida

def track_delivery():
    delivery_data = []
    
    for lat, lon in coordinates:
        # Get location from GPS coordinates
        location = get_location(lat, lon)
        
        # Record the delivery information
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        delivery_data.append({
            'Teddy_ID': 'TB001',  # Example Teddy ID
            'Latitude': lat,
            'Longitude': lon,
            'Location': location,
            'Timestamp': current_time
        })
        
        print(f"Delivery Update: {location} at {current_time}")
        
        # Save delivery data every 3 seconds (simulated)
        if len(delivery_data) >= 3:
            df = pd.DataFrame(delivery_data)
            df.to_csv('delivery_updates.csv', index=False)
            print("Delivery data saved to delivery_updates.csv")
            delivery_data = []
        
        time.sleep(3)

if __name__ == '__main__':
    track_delivery()
