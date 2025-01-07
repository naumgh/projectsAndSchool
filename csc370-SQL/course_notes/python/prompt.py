#!/usr/bin/env python3

import sys


def get_name_age(lang):
    if lang == "en":
        name = input("What is your name? ")
        age = input("What is your age? ")
    elif lang == "de":
        name = input("Wie heisst Du? ")
        age  = input("Was ist dein Alter? ")
    elif lang == "fr":
        name = input("Comment t'appelle tu? ")
        age  = input("Quel age a tu? ")
    else:
        name = "<dunno>"
        age = "0"

    try:
        age = int(age)
    except ValueError as verr:
        print("ERROR: Age cannot be converted to an integer.")
        print("ERROR: An age of zero is used instead.")
        age = 0     # Age provided by user cannot be converted to an int

    return (name, age)


def main():
    if len(sys.argv) > 1:
        language = sys.argv[1]
    else:
        language = "en"

    (n, a) = get_name_age(language)

    if language == "en":
        response = "Hello " + n + ". You are " + str(a) + " years old."
    elif language == "de":
        response = "Gruß Dich, " + n + ". Du bist " + \
            str(a) + " Jahre alt."
    elif language == "fr":
        response = "Salut " + n  + ". Tu as " + str(a) + " ans."
    else:
        response = "Ellohay " + n + ". Youhay arehay " + str(a) + "oldhay."

    print(response)


if __name__ == "__main__":
    main()
