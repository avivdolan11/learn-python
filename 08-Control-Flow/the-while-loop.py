# count = 0

# while count <= 5:
#     print(count)
#     count += 1

# print(count)


invalid_number = True

while invalid_number:
    user_value = int(input("Please enter a number above 10: "))
    if user_value > 10:
        print(f"Thanks that works {user_value} is a great choice")
        invalid_number = False
    else:
        print("Doesnt fit, try again")    



def fizzbuzz(final_number):
  current_number = 1
  while current_number <= final_number:
    if current_number % 15 == 0:
      print("FizzBuzz")
    elif current_number % 3 == 0:
      print("Fizz")
    elif current_number % 5 == 0:
      print("Buzz")
    else:
      print(current_number)
    current_number += 1

fizzbuzz(30)