#This file is run once to generate our public and private key .pem files. publickey.pem is now in the client folder
# while privatekey.pem is now in the server folder

#https://stackoverflow.com/questions/41658258/valueerror-when-reading-rsa-key-from-pem-file-using-importkey
#https://www.dlitz.net/software/pycrypto/api/current/Crypto.PublicKey.RSA-module.html

from Crypto.PublicKey import RSA

#generate key pair
key = RSA.generate(1024)


#write private key to file
f = open('privateKey.pem','wb')
f.write(key.exportKey('PEM'))
f.close()

#To read key:
#print("encrypting")
#f = open('publicKey.pem', 'r')
#key = RSA.importKey(f.read())

#Write public key to file
f = open('publicKey.pem', 'wb')
f.write(key.publickey().exportKey('PEM'))
f.close()

#To read key:
#print("decrypting")
#f = open("privateKey.pem", 'r')
#key = RSA.importKey(f.read())
#m = key.decrypt(enc)
#print(m.decode())