#Random Password Generator
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# First make a list of the letters, numbers and symbols

# Initialize a variable for password
pwd=""
# Start with the total characters in pw and loop for letters number and symbols indvidually
total=nr_letters+nr_numbers+nr_symbols
(letter_count,number_count,symbol_count)=(0,0,0)
# Make a random selection from pool
# if len(pwd)<total:
while len(pwd)<total:
  for j in range(1,total+1):

    a=random.choice(letters)
    c=random.choice(symbols)
    b=random.choice(numbers)

    pool=[a,b,c]

    i=random.choice(pool)

    if i in letters and letter_count<nr_letters:
      pwd=pwd+i
      letter_count=letter_count+1
    elif i in symbols and symbol_count<nr_symbols:
      pwd=pwd+i
      symbol_count=symbol_count+1
    elif i in numbers and number_count<nr_numbers:
      pwd=pwd+i
      number_count=number_count+1

print(f"j is {j}")
print(pwd)


print(letter_count)
print(symbol_count)
print(number_count)
