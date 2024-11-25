crpto_currency = {
    "Bitcoin": 400000,
    "Ethereum": 7000,
    "Litecoin": 10
}

print(crpto_currency.keys())
print(crpto_currency.values())

for currency in crpto_currency.keys():
    print(f"The next currency is {currency}")

for price in crpto_currency.values():
    print(f"The next price is {price}")

print("Bitcoin" in crpto_currency.keys())