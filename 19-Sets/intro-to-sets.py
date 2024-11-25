stocks = {"MSFT", "FB", "IBM", "FB"}

print(stocks)
print(type(stocks))

prices = {1,2,3,4,5,6,7,1,2,5}
print(prices)

lottery_numbers = {(1,2,3), (4,5,6), (1,2,3)}
print(lottery_numbers)

print(len(stocks))

print(2 in prices)

for number in prices:
    print(number)

for numbers in lottery_numbers:
    for number in numbers:
        print(number)


squares = {number ** 2 for number in [-5, -4, -3, 3, 4, 5] }
print(squares)
