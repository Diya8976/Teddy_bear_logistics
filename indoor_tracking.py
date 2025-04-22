import random
import time

# Simulate RFID-based indoor tracking system
class IndoorTrackingSystem:
    def __init__(self):
        self.areas = ['Entrance', 'Aisle 1', 'Aisle 2', 'Checkout', 'Storage']
        self.current_area = random.choice(self.areas)
    
    def move_teddy_bear(self):
        # Randomly move teddy bear within defined areas
        self.current_area = random.choice(self.areas)
        print(f"Teddy Bear is now in: {self.current_area}")

# Create an instance of the indoor tracking system
tracking_system = IndoorTrackingSystem()

def track_teddy():
    while True:
        tracking_system.move_teddy_bear()
        time.sleep(5)  # Update every 5 seconds

if __name__ == '__main__':
    track_teddy()
