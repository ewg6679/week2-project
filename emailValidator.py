"""
file: email_validator.py
author: Emmanuel Griffin
author: Nicole de Moura
description: Checks if a given email address is valid
             Checks if a given password is secure
"""

import requests
import sqlite3

"""
email - the email the user wants to sign up with
get_email - returns true if the email given is valid and false otherwise
"""
def get_email(email):
    url = "https://mailcheck.p.rapidapi.com/"

    querystring = {"domain": email}

    headers = {
        "X-RapidAPI-Key": "84e3b5a6f6mshfa61e64adee66a3p1c8d48jsn7f6087e0f0cd",
        "X-RapidAPI-Host": "mailcheck.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    valid = response.json().get("valid")
    if valid is True:
        print("Valid email")
        return True
    else:
        print("Invalid email, try again")
        return False

"""
password - the password the user wants to use
secure_password - returns true if the password is secure and false otherwise 
"""
def secure_password(password):
    special_char = '[@_!#$%^&*()<>?/\|}{~:]'
    num = False
    special = False
    if len(password) < 8:
        print("Password length must exceed 7 characters: ")
        return False
    for char in password:
        if char.isdigit():
            num = True
        if char in special_char:
            special = True
    if num is True and special is True:
        print("Secure password")
        return True
    elif num is False and special is True:
        print("Needs number in password")
        return False
    elif num is True and special is False:
        print("Needs special character in password")
        return False
    else:
        print("Needs number and special character in password")
        return False

"""
email - the email the user wants to make an account with
password - the password the user wants to make an account with
make_account - creates an account for a user and holds that data
"""
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

"""

"""
def main():
    email_valid = get_email(input("Email: "))
    while not email_valid:
        email_valid = get_email(input("Email: "))
    print("Secure password requirements: Must be 8 characters or longer, must include one number, and one special character")
    password_valid = secure_password(input("Password: "))
    while not password_valid:
        password_valid = secure_password(input("Password: "))


if __name__ == '__main__':
    main()
