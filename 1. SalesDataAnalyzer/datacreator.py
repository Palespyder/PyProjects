import csv
from faker import Faker
import random

# Initialize the Faker library
fake = Faker()

# Number of records to generate
num_records = 10000

# Define product categories and payment methods
products = ['Laptop', 'Smartphone', 'Headphones', 'Keyboard', 'Mouse', 'Monitor', 'Printer', 'Webcam']
payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Cash']
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania']

# Create a CSV file and write the data
with open('large_fake_sales_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Sale ID', 'Date', 'Product', 'Quantity', 'Price', 'Total', 'Customer ID', 'Customer Name', 'Payment Method', 'Region']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for sale_id in range(1, num_records + 1):
        sale_date = fake.date_this_year()
        product = random.choice(products)
        quantity = random.randint(1, 10)
        price = round(random.uniform(10.0, 500.0), 2)
        total = round(quantity * price, 2)
        customer_id = fake.uuid4()  # Unique identifier for the customer
        customer_name = fake.name()  # Customer's full name
        payment_method = random.choice(payment_methods)  # Payment method used
        region = random.choice(regions)  # Region where the sale took place
        
        writer.writerow({
            'Sale ID': sale_id,
            'Date': sale_date,
            'Product': product,
            'Quantity': quantity,
            'Price': price,
            'Total': total,
            'Customer ID': customer_id,
            'Customer Name': customer_name,
            'Payment Method': payment_method,
            'Region': region
        })

print(f"{num_records} records have been written to 'large_fake_sales_data.csv'.")