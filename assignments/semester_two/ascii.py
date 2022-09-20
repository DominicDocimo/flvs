# Dominic Docimo
# 09/09/2022
# This program ascii encode a message and make the user guess what it is

message = "hello, world"
encoded_message = []
decoded = ""

for char in message:
    encoded_message.append(ord(char))

print("The encoded message is " + str(encoded_message))
guess = input("Guess what it is!")

for char in encoded_message:
    decoded += chr(char)

if guess == decoded:
    print("You got it!")
else:
    print("Nope... it was", decoded)
