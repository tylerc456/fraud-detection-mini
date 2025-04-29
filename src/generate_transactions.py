# Standard library imports
import random
import uuid
from datetime import datetime, timedelta

# Third-party imports
from faker import Faker
import pandas as pd

# Local application imports
from generate_customers import generate_customers
from generate_merchants import generate_merchants

fake = Faker()

def generate_transactions(customers, merchants, n_transactions=10000, fraud_rate=0.01):
    transactions = []
    start_time = datetime.now() - timedelta(days=365)  # Transactions within the last year

    for _ in range(n_transactions):
        customer = random.choice(customers)
        merchant = random.choice(merchants)
        transaction_id = str(uuid.uuid4())
        timestamp = start_time + timedelta(seconds=random.randint(0, 365 * 24 * 3600))
        location = fake.city()
        amount = round(random.uniform(1.00, 5000.00), 2)
        fraud = 1 if random.random() < fraud_rate else 0

        transaction = {
            "transaction_id": transaction_id,
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "location": location,
            "amount": amount,
            "customer_id": customer["customer_id"],
            "merchant_id": merchant["merchant_id"],
            "fraud": fraud
        }
        transactions.append(transaction)

    return transactions

def main():
    customers = generate_customers()
    merchants = generate_merchants()
    transactions = generate_transactions(customers, merchants)

    df = pd.DataFrame(transactions)
    df.to_csv("data/transactions.csv", index=False)
    print(f"Generated {len(df)} transactions.")

if __name__ == "__main__":
    main()
