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
    valid = response.json().get("valid")
    if valid:
        print("Valid email")
        return email
    else:
        print("Invalid email, try again")
        return False


def secure_password(password):
    special_char = '[@_!#$%^&*()<>?/\|}{~:]'
    num = False
    special = False
    if len(password) < 8:
        print("Password length must exceed 7 characters")
        return False
    for char in password:
        if char.isdigit():
            num = True
        if char in special_char:
            special = True
    if num is True and special is True:
        print("Secure password")
        return password
    elif num is False and special is True:
        print("Needs number in password")
        return False
    elif num is True and special is False:
        print("Needs special character in password")
        return False
    else:
        print("Needs number and special character in password")
        return False


def make_account(email, password):
    conn = sqlite3.connect('accounts.db')

    cursor = conn.cursor()

    sql = '''CREATE TABLE IF NOT EXISTS ACCOUNTS(
    EMAIL VARCHAR(255),
    PASSWORD VARCHAR(255)
    )'''
    cursor.execute(sql)

    cursor.execute("SELECT EMAIL FROM ACCOUNTS WHERE EMAIL = ?", (email,))
    exists = cursor.fetchone()

    if exists:
        print("An account with this email already exists")
        conn.close()
        return False
    else:
        cursor.execute('''INSERT INTO ACCOUNTS(
        EMAIL, PASSWORD) VALUES 
        (?, ?)''', (email, password))

    conn.commit()
    cursor.execute("SELECT * FROM ACCOUNTS")
    print("Welcome! You can now log in using your credentials",
          cursor.fetchall()[-1])

    conn.close()
    return True


def log_in():
    conn = sqlite3.connect('accounts.db')

    cursor = conn.cursor()

    while True:
        email = input("Email: ")
        if email.isdigit() and int(email) == 2:
            print("Signing up . . .")
            sign_up()
            break
        try:
            cursor.execute(
                "SELECT EMAIL FROM ACCOUNTS WHERE EMAIL = ?", (email,))
            if len(cursor.fetchall()) < 1:
                raise Exception()
            else:
                print("Login success")
            break
        except:
            print("Please enter an existing email address, or type 2 to sign up")

    conn.close()


def sign_up():
    while True:
        email = input("Email: ")
        email_valid = get_email(email)
        while not email_valid:
            email = input("Email: ")
            email_valid = get_email(email)

        print("Secure password requirements: Must be 8 characters or longer, must include one number, and one special character")
        password_valid = secure_password(input("Password: "))
        while not password_valid:
            password_valid = secure_password(input("Password: "))

        if make_account(email_valid, password_valid):
            break


def main():
    print("Type 1 to log in and 2 to sign up")
    action = None
    while action not in (1, 2):
        action = input("> ")
        if action.isdigit() and int(action) == 1:
            log_in()
            break
        elif action.isdigit() and int(action) == 2:
            sign_up()
            break
        else:
            print("Please type a valid option")


if __name__ == '__main__':
    main()
