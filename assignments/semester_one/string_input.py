# Dominic Docimo
# 6/21/22
# This program will simulate a chatbot conversation


def main():
    first_name = input("Hello, my name is Dave! What's your first name?")
    print("Your first name has a length of " + str(len(first_name)) + " and the third letter is " + first_name[2])

    last_name = input("Well " + first_name + ", what's your last name?")
    print("That means your name is " + first_name + last_name.rjust(len(last_name)+1))

    language = input("What is your favorite programming language?")

    if language.lower() in ["c++", "javascript", "c", "rust"]:
        print("I don't like that language :(")
    else:
        print("I like that language :)")

    print("That's all from me. Have a nice day " + first_name)


main()
