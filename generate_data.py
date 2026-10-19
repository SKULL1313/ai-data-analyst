import random
from pathlib import Path

import pandas as pd
from faker import Faker

fake = Faker()

# Make the generated data reproducible
Faker.seed(42)
random.seed(42)

# Possible products and prices
products = {
    "Laptop": 1200,
    "Monitor": 300,
    "keyboard": 75,
    "Mouse": 35,
    "Headphones": 150,
    "Webcam": 90,
}

transactions = []

# Generate 1,000 fictional transactions
for transaction_id in range(1,1001):
    product = random.choice(list(products.keys()))
    quantity = random.randint(1, 5)
    unit_price = products[product]
    
    transactions.append({
        "transaction_id": transaction_id,
        "date": fake.date_between(
            start_date="-1y",
            end_date="today"
        ),
        "customer": fake.name(),
        "city": fake.city(),
        "product": product,
        "quantity": quantity,
        "unit_price": unit_price,
        "revenue": quantity * unit_price,
    })
    
    # Convert the transactions into a tble
    df = pd.DataFrame(transactions)
    
    # Save the CSV in the project's data folder
    output_folder = Path("data")
    output_folder.mkdir(exist_ok=True)
    
    output_file = output_folder / "transactions.csv"
    df.to_csv(output_file, index=False)
    
    print("Transaction data generated successfully!")
    print(f"Number of transactions: {len(df)}")
    print(f"Total revenue: ${df['revenue'].sum():,.2f}")
    print(f"Saved to: {output_file}")