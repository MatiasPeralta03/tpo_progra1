import pandas as pd
import random
from datetime import datetime, timedelta

# List of market products with their specific prices
product_prices = {
    "Producto A": 10000,
    "Producto B": 15000,
    "Producto C": 20000,
    "Producto D": 5000,
    "Producto E": 7500,
    "Producto F": 12000,
    "Producto G": 9000,
    "Producto H": 30000,
    "Producto I": 25000,
    "Producto J": 18000,
    "Producto K": 6000,
    "Producto L": 4500,
    "Producto M": 22000,
    "Producto N": 14000,
    "Producto O": 13000,
    "Producto P": 11000,
    "Producto Q": 9500,
    "Producto R": 8000,
    "Producto S": 16000,
    "Producto T": 17000
}

# Function to generate random dates
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Generate data
data = []
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

for i in range(1000000):  # Adjust the range as needed for more rows
    date = random_date(start_date, end_date).strftime("%d/%m/%Y")
    product = random.choice(list(product_prices.keys()))  # Randomly select from predefined products
    quantity = random.randint(1, 20)
    yes_no = random.choice(["Y", "N"])
    
    # Get the specific price for the selected product
    price_per_unit = product_prices[product]
    
    # Calculate total price
    total_price = round(price_per_unit * quantity, 2)
    
    payment_method = random.choice(["Efectivo", "Transferencia", "Tarjeta"])
    
    # Append the data including the total price
    data.append([i + 1, date, product, quantity, yes_no, total_price, payment_method])

# Create a DataFrame and save to CSV
df = pd.DataFrame(data, columns=["id", "fecha", "producto", "cantidad", "cliente", "precio", "metodo_de_pago"])
df.to_csv("ventas.csv", index=False, sep=';')

print("CSV file 'ventas.csv' has been created.")
