import pandas as pd
import random
from datetime import datetime, timedelta

# List of market products with their specific prices
product_prices = {
    "Producto A": 100.0,
    "Producto B": 150.0,
    "Producto C": 200.0,
    "Producto D": 50.0,
    "Producto E": 75.0,
    "Producto F": 120.0,
    "Producto G": 90.0,
    "Producto H": 300.0,
    "Producto I": 250.0,
    "Producto J": 180.0,
    "Producto K": 60.0,
    "Producto L": 45.0,
    "Producto M": 220.0,
    "Producto N": 140.0,
    "Producto O": 130.0,
    "Producto P": 110.0,
    "Producto Q": 95.0,
    "Producto R": 80.0,
    "Producto S": 160.0,
    "Producto T": 170.0
}

# Function to generate random dates
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Generate data
data = []
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

for i in range(10):  # Adjust the range as needed for more rows
    date = random_date(start_date, end_date).strftime("%d/%m/%Y")
    product = random.choice(list(product_prices.keys()))  # Randomly select from predefined products
    quantity = random.randint(1, 20)
    yes_no = random.choice(["Sí", "No"])
    
    # Get the specific price for the selected product
    price_per_unit = product_prices[product]
    
    # Calculate total price
    total_price = round(price_per_unit * quantity, 2)
    
    payment_method = random.choice(["Efectivo", "Transferencia", "Tarjeta"])
    
    # Append the data including the total price
    data.append([i + 1, date, product, quantity, yes_no, total_price, payment_method])

# Create a DataFrame and save to CSV
df = pd.DataFrame(data, columns=["ID", "Fecha", "Producto", "Cantidad", "Sí/No", "Precio", "Método de Pago"])
df.to_csv("generated_data_top.csv", index=False)

print("CSV file 'generated_data_top.csv' has been created.")
