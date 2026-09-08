import random
import string



print("=" * 45)
print("         🔐 PY PASSWORD GENERATOR")
print("=" * 45)
print("Create a strong and secure password!")
print("-> total max characters = 24.\n")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

avaible_symbols = list(string.punctuation)
avaible_letters = list(string.ascii_lowercase + string.ascii_uppercase)
avaible_numbers = list(string.digits)
# ou eu poderia fazer : available_letters = list(string.ascii_letters)

password = []


if letters <= 8:
    for letter in range(letters):
        randomization_letter = random.choice(avaible_letters)
        # print(randomization_letter, end="")
        password.append(randomization_letter)
else:
    print("Too much letters, try a lower value.")




if symbols <= 8:
      for symbol in range(symbols):
          randomization_symbol = random.choice(avaible_symbols)
          # print(randomization_symbol, end="")
          password.append(randomization_symbol)
else:
    print("Too much letters, try a lower value.")



if numbers <= 8:
    for number in range(numbers):
        randomization_number = random.choice(avaible_numbers)
        # print(randomization_number, end="")
        password.append(randomization_number)
else:
    print("Too much letters, try a lower value.")




random.shuffle(password)

final_password = "".join(password)




print("\n" + "=" * 45)
print("        🔐 YOUR PASSWORD IS READY!")
print("=" * 45)
print("Here is your generated password:\n")

print(final_password)