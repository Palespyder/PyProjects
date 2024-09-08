import requests
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar, DoubleVar

# Your currency dictionary
currencies = {
    "EUR": "Euro",
    "USD": "US Dollar",
    "JPY": "Japanese Yen",
    "BGN": "Bulgarian Lev",
    "CZK": "Czech Republic Koruna",
    "DKK": "Danish Krone",
    "GBP": "British Pound Sterling",
    "HUF": "Hungarian Forint",
    "PLN": "Polish Zloty",
    "RON": "Romanian Leu",
    "SEK": "Swedish Krona",
    "CHF": "Swiss Franc",
    "ISK": "Icelandic Króna",
    "NOK": "Norwegian Krone",
    "HRK": "Croatian Kuna",
    "RUB": "Russian Ruble",
    "TRY": "Turkish Lira",
    "AUD": "Australian Dollar",
    "BRL": "Brazilian Real",
    "CAD": "Canadian Dollar",
    "CNY": "Chinese Yuan",
    "HKD": "Hong Kong Dollar",
    "IDR": "Indonesian Rupiah",
    "ILS": "Israeli New Sheqel",
    "INR": "Indian Rupee",
    "KRW": "South Korean Won",
    "MXN": "Mexican Peso",
    "MYR": "Malaysian Ringgit",
    "NZD": "New Zealand Dollar",
    "PHP": "Philippine Peso",
    "SGD": "Singapore Dollar",
    "THB": "Thai Baht",
    "ZAR": "South African Rand"
}

KEY = ''
URL_BASE = 'https://api.freecurrencyapi.com/v1/latest?apikey='


# Fetch conversion rates
def get_currency_conversion(currency):
    url = f'{URL_BASE}{KEY}&currencies={currency}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        conversion = data['data'][currency]
        return conversion
    else:
        return None


# Function to perform conversion
def convert_currency():
    try:
        amount = float(amount_var.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        # Get conversion rate for both currencies
        conversion_from = get_currency_conversion(from_currency)
        conversion_to = get_currency_conversion(to_currency)

        if conversion_from and conversion_to:
            usd_amount = amount / conversion_from  # Convert to USD first
            converted_amount = usd_amount * conversion_to  # Convert from USD to target currency
            result_var.set(f"{amount} {from_currency} = {round(converted_amount, 2)} {to_currency}")
        else:
            result_var.set("Conversion failed, please check the API.")
    except Exception as e:
        result_var.set(f"Error: {e}")


# Initialize the GUI app
app = ttk.Window(themename="darkly")  # or any theme you prefer
app.title("Currency Converter")
app.geometry("400x300")

# GUI Variables
amount_var = DoubleVar()
from_currency_var = StringVar(value='USD')
to_currency_var = StringVar(value='EUR')
result_var = StringVar()

# Labels and Inputs
ttk.Label(app, text="Amount:", font=("Arial", 14)).pack(pady=10)
ttk.Entry(app, textvariable=amount_var, font=("Arial", 12)).pack(pady=10)

ttk.Label(app, text="From Currency:", font=("Arial", 14)).pack(pady=10)
ttk.Combobox(app, textvariable=from_currency_var, values=list(currencies.keys()), font=("Arial", 12)).pack(pady=10)

ttk.Label(app, text="To Currency:", font=("Arial", 14)).pack(pady=10)
ttk.Combobox(app, textvariable=to_currency_var, values=list(currencies.keys()), font=("Arial", 12)).pack(pady=10)

# Convert Button
ttk.Button(app, text="Convert", command=convert_currency, bootstyle=SUCCESS).pack(pady=20)

# Result Label
ttk.Label(app, textvariable=result_var, font=("Arial", 12), wraplength=300).pack(pady=20)

# Start the GUI loop
app.mainloop()
