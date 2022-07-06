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
        print("Valid email")
        return "Valid email"
    else:
        print("Invalid email, try again")
        return "Invalid email, try again"
        

def secure_password(password):
    specialChar = '[@_!#$%^&*()<>?/\|}{~:]'
    num = False
    special = False
    if len(password) < 8:
        print("Password length must exceed 7 characters: ")
        return "Password length must exceed 7 characters: "
    for char in password:
        if char.isdigit():
            num = True
        if char in specialChar:
            special = True
    if num is True and special is True:
        print("Secure password")
        return "Secure"
    elif num is False and special is True:
        print(secure_password(input("Needs number in password: ")))
        return "Needs number in password: "
    elif num is True and special is False:
        print(secure_password(input("Needs special character in password: ")))
        return "Needs special character in password: "
    else:
        print(secure_password(input("Needs number and special character in password: ")))
        return "Needs number and special character in password: "


def main():
    inpt = input("Email: ") 
    emailValid = get_email(input("Enter your email: ")
    while emailValid != "Valid email":
        emailValid = get_email(input("Enter your email: ")
    print("Secure password requirements: Must be 8 characters or longer, must include one number, and one special character")
    passwordValid = secure_password(input("Password: "))
    while passwordValid != "Secure":
        passwordValid = secure_password(input("Password ")
    

if __name__ == '__main__':
    main()
