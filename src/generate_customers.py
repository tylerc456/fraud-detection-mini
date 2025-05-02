import faker

fake = faker.Faker()

def generate_customers(n_customers=100):
    customers = []
    for _ in range(n_customers):
        customer = {
            "customer_id": fake.uuid4(),
            "address": fake.address().replace('\n', ', ')
        }
        customers.append(customer)
    return customers

if __name__ == "__main__":
    customers = generate_customers(5)
    for c in customers:
        print(c)
