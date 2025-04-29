# src/generate_merchants.py

import random
import uuid

MERCHANT_CATEGORIES = [
    "Grocery",
    "Electronics",
    "Restaurant",
    "Clothing",
    "Gas Station",
    "Travel",
    "Health",
    "Entertainment",
    "Home Goods",
    "Automotive",
]

def generate_merchants(n_merchants=500):
    merchants = []
    for _ in range(n_merchants):
        merchant_id = str(uuid.uuid4())
        merchant_name = f"{random.choice(['Sunny', 'Best', 'Happy', 'Quick', 'Super', 'Global'])} {random.choice(['Mart', 'Shop', 'Store', 'Cafe', 'Depot', 'Center'])}"
        merchant_category = random.choice(MERCHANT_CATEGORIES)
        
        merchant = {
            "merchant_id": merchant_id,
            "merchant_name": merchant_name,
            "merchant_category": merchant_category
        }
        merchants.append(merchant)
    return merchants

if __name__ == "__main__":
    merchants = generate_merchants()
    print(merchants[:5])  # Preview the first 5 merchants
