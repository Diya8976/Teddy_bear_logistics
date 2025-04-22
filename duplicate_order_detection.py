import pandas as pd

# Sample order data (simulated, no Neo4j)
data = {
    'order_id': [1, 2, 3, 4, 5, 6],
    'customer_id': [101, 102, 101, 104, 103, 101],
    'order_amount': [100, 150, 100, 180, 220, 100]
}

df = pd.DataFrame(data)

# Simulate duplicate order detection:
# Same customer placing same amount more than once
duplicate_orders = df.groupby(['customer_id', 'order_amount']).size().reset_index(name='count')
duplicates = duplicate_orders[duplicate_orders['count'] > 1]

print("🔁 Duplicate Orders Found:\n")
if not duplicates.empty:
    for _, row in duplicates.iterrows():
        print(f"Customer ID: {row['customer_id']}, Order Amount: {row['order_amount']}, Count: {row['count']}")
else:
    print("✅ No duplicate orders found.")
