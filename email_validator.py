"""
file: email_validator.py
author: Emmanuel Griffin
author: Nicole de Moura

description: Checks if a given email address is valid
             Checks if a given password is secure
"""

import requests
import sqlite3


def get_email(email):
    url = "https://mailcheck.p.rapidapi.com/"

    querystring = {"domain": email}

    headers = {
        "X-RapidAPI-Key": "84e3b5a6f6mshfa61e64adee66a3p1c8d48jsn7f6087e0f0cd",
        "X-RapidAPI-Host": "mailcheck.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.text


def secure_password(password):
    specialChar = '[@_!#$%^&*()<>?/\|}{~:]'
    num = False
    special = False
    if len(password) < 8:
        return "Password length must exceed 7 characters"
    for char in password:
        if char.isdigit():
            num = True
        if char in specialChar:
            special = True
    if num is True and special is True:
        return "Secure password"
    elif num is False and special is True:
        return "Needs number in password"
    else:
        return "Needs number and special character in password"


def make_account(email, password):
    conn = sqlite3.connect('accounts.db')

    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS ACCOUNTS")

    sql = '''CREATE TABLE ACCOUNTS(
    EMAIL VARCHAR(255),
    PASSWORD VARCHAR(255)
    )'''
    cursor.execute(sql)

    cursor.execute('''INSERT INTO ACCOUNTS(
    EMAIL, PASSWORD) VALUES 
    (?, ?)''', (email, password))

    conn.commit()
    cursor.execute("SELECT * FROM ACCOUNTS")
    # print(cursor.fetchall())

    conn.close()


def main():
    inpt = input("Email: ")
    print(get_email(inpt))
    print("Secure password requirements: Must be 8 characters or longer, must include one number, and one special character")
    passwordInpt = input("Password: ")
    print(secure_password(passwordInpt))


if __name__ == '__main__':
    # main()
    make_account('email1@gmail.com', 'password')
