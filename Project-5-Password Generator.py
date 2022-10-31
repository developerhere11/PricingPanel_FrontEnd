import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
a = int(input("How many letters would you like in your password?\n"))
b = int(input("How many numbers would you like?\n"))
c = int(input("How many symbols would you like?\n"))


# Easy Method
# password = ""
# for letter in range(0, a):
#     random_letters = random.choice(letters)
#     # print(random_letters) 
#     password = password + random_letters
#
# for number in range(0, b):
#     random_numbers = random.choice(numbers)
#     # print(random_numbers)
#     password = password + random_numbers
#
# for symbol in range(0, c):
#     random_symbols = random.choice(symbols)
#     # print(random_symbols)
#     password = password + random_symbols
#
# print(f"Password : {password}")

# Hard method  append and += both works

password_list = []
for letter in range(0, a):
    random_letters = random.choice(letters)
    # print(random_letters)
    password_list.append(random_letters)

for number in range(0, b):
    random_numbers = random.choice(numbers)
    # print(random_numbers)
    password_list.append(random_numbers)

for symbol in range(0, c):
    random_symbols = random.choice(symbols)
    # print(random_symbols)
    password_list += random_symbols

# print(f"Password : {password_list}")
random.shuffle(password_list)      # to reorder shuffle a list contents
# print(f"Password : {password_list}")

password = ""
for char in password_list:
    password = password + char

print(f"Password : {password}")

