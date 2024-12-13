import random

from pymsgbox import password

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
         't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L',
         'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']

print("Welcome to the password Generator")
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbol=int(input("How many symbols would you like?\n"))
nr_numbers=int(input("How many numbers would you like?\n"))

# password=""
# for char in range(0,nr_letters):
#     password+=random.choice(letters)
# for char in range(0,nr_numbers):
#     password+=random.choice(numbers)
# for char in range(0,nr_symbol):
#     password+=random.choice(symbols)

# print(password)

passwordList=[]
for char in range(0,nr_letters):
    passwordList.append(random.choice(letters))
for char in range(0,nr_numbers):
    passwordList.append(random.choice(numbers))
for char in range(0,nr_symbol):
    passwordList.append(random.choice(symbols))

random.shuffle(passwordList)
print(passwordList)

password=""
for char in passwordList:
    password+=char

print(f"Your password is : {password}")