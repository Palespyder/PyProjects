import pandas as pd
from faker import Faker
import random

# Initialize Faker instance
fake = Faker()

# Define the number of rows and columns
num_rows = 100

# Columns for sales data
columns = [
    "Order_ID",         # Unique order identifier
    "Customer_Name",    # Customer's full name
    "Customer_Email",   # Customer's email
    "Product",          # Product sold
    "Quantity",         # Quantity of product sold
    "Price_Per_Unit",   # Price per unit of product
    "Total_Price",      # Total price = Quantity * Price per unit
    "Purchase_Date",    # Date of purchase
    "Payment_Method",   # Payment method (e.g., credit card, PayPal)
    "Country"           # Customer's country
]

# Generate fake sales data
data = []
for _ in range(num_rows):
    quantity = random.randint(1, 10)
    price_per_unit = round(random.uniform(10.0, 1000.0), 2)
    country_list = ['USA', 'Canada', 'Germany', 'France', 'Australia', 'Japan', 'USA', 'Canada']
    name_list = ['John Smith', 'Jane Doe', 'Alice Johnson', 'Robert Brown', 'Emily Davis', 'Michael Wilson', 'Sarah Miller', 'James Clark', 'Jessica Lewis', 'Daniel Walker']
    total_price = quantity * price_per_unit
    data.append([
        fake.unique.uuid4(),          # Order ID
        random.choice(name_list),                  # Customer Name
        fake.email(),                 # Customer Email
        fake.word(ext_word_list=['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse']),  # Product
        quantity,                     # Quantity
        price_per_unit,               # Price per unit
        round(total_price, 2),        # Total price
        fake.date_this_year(),        # Purchase Date
        fake.credit_card_provider(),  # Payment Method
        random.choice(country_list)   # Country
    ])

# Create a DataFrame with the generated data
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to a CSV file (optional)
df.to_csv("fake_sales_data.csv", index=False)

# Display the DataFrame
print(df)