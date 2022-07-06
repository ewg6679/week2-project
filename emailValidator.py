"""
file: emailValidator.py
author: Emmanuel Griffin
author: Nicole de Moura
description: Checks if a given email address is valid
             Checks if a given password is secure
"""

import requests

def get_email(email):
    url = "https://mailcheck.p.rapidapi.com/"

    querystring = {"domain": email}

    headers = {
        "X-RapidAPI-Key": "84e3b5a6f6mshfa61e64adee66a3p1c8d48jsn7f6087e0f0cd",
        "X-RapidAPI-Host": "mailcheck.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    valid = response.json().get("valid")
    if valid is True:
        return "Valid email"
    else:
        get_email(input("Invalid email try again: "))
        

def secure_password(password):
    specialChar = '[@_!#$%^&*()<>?/\|}{~:]'
    num = False
    special = False
    if len(password) < 8:
        return secure_password(input("Password length must exceed 7 characters: ")
    for char in password:
        if char.isdigit():
            num = True
        if char in specialChar:
            special = True
    if num is True and special is True:
        return "Secure password"
    elif num is False and special is True:
        return secure_password(input("Needs number in password: "))
    else:
        return secure_password(input("Needs number and special character in password: "))


def main():
    inpt = input("Email: ") 
    print(get_email(inpt))
    print("Secure password requirements: Must be 8 characters or longer, must include one number, and one special character")
    passwordInpt = input("Password: ")
    print(secure_password(passwordInpt))
    


if __name__ == '__main__':
    main()
