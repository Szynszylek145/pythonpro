import random

password_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

a = int(input("Wpisz długość hasła: "))

password = ""

for i in range(a):
    a = random.choice(password_characters)
    password = password + a

print(password)

