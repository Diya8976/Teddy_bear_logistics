import time
import json

# Simulated delivery data
delivery_data = {
    'delivery_id': 1,
    'order_id': 1001,
    'delivery_status': 'Delivered',
    'timestamp': int(time.time())
}

# Simulated Blockchain Logger
def record_delivery_on_blockchain(data):
    print("⛓️ Simulating Blockchain Transaction...\n")
    print("📦 Delivery Data Logged:")
    print(json.dumps(data, indent=4))
    print("✅ Transaction simulated successfully (not real blockchain).")

# Run it
if __name__ == "__main__":
    record_delivery_on_blockchain(delivery_data)
