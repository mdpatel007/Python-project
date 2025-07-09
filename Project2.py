#Create a random password generator
#This code generates a random password of length 12 using letters, digits, and punctuation.
import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("Your random password is : ",password)