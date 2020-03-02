import hashlib
import os
from random import randint
"""
    add_user.py - Stores a new username along with salt/password

    CSCI 3403
    Authors: Matt Niemiec and Abigail Fernandes
    The solution contains the same number of lines (plus imports)
"""
print("starting!")
user = input("Enter a username: ")
password = input("Enter a password: ")



# TODO: Create a salt and hash the password
# https://nitratine.net/blog/post/how-to-hash-passwords-in-python/
#Create radnom 16 bit salt
salt = os.urandom(16)
#Append salt to password
passWithSalt = password + str(salt)
#Hash the password
hashed = hashlib.sha1(passWithSalt.encode())
hashed_password = hashed.hexdigest()

try:
    reading = open("passfile.txt", 'r')
    for line in reading.read().split('\n'):
        if line.split('\t')[0] == user:
            print("User already exists!")
            exit(1)
    reading.close()
except FileNotFoundError:
    pass

with open("passfile.txt", 'a+') as writer:
    writer.write("{0}\t{1}\t{2}\n".format(user, salt, hashed_password))
    print("User successfully added!")

print("done!")


