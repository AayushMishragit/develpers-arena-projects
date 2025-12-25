import requests
from colorama import Fore,Style,init

print("=====================================================")
init(autoreset=True)
print(Fore.GREEN +Style.BRIGHT + "💱CURRENCY CONVERTOR")


def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][to_currency]

# Example usage
amount = int(input("Enter amount:"))
from_currency = input("From currency (e.g., USD):").upper()
to_currency = input("To currency (e.g., EUR):").upper()
result = convert_currency(amount, from_currency, to_currency)
print(f"{amount}{from_currency} = {result}\t {to_currency}")
print("=====================================================")