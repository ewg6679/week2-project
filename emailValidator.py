"""
file: emailValidator.py
author: Emmanuel Griffin
author: Nicole de Moura

description: Checks if a given email address is valid
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

    return response.text


def main():
    inpt = input("Email: ")
    print(get_email(inpt))
    


if __name__ == '__main__':
    main()
