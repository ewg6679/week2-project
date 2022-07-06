import unittest
from emailValidator import get_email, secure_password


class TestFileName(unittest.TestCase):
    def test_get_email_valid(self):
        self.assertEqual(get_email("nicole@gmail.com"), "Valid email")
        self.assertEqual(get_email("jacklack@yahoo.com"), "Valid email")
        self.assertEqual(get_email("ndemoura@uw.edu"), "Valid email")

    def test_get_email_unvalid(self):
        self.assertEqual(get_email("nicole@gmail"), "Invalid email")
        self.assertEqual(get_email(""), "Invalid email")
        self.assertEqual(get_email(" "), "Invalid email")
        self.assertEqual(get_email("hghkdnlsdpksl"), "Invalid email")
        self.assertEqual(get_email("jdomkamdkmf@fake.com"), "Invalid email")

    def test_secure_password_valid(self):
        self.assertEqual(secure_password("LamaBeans4$"), "Valid email")
        self.assertEqual(secure_password("-humpdyDumpy27"), "Valid email")
        self.assertEqual(secure_password("yoGurtdreamS8999+"), "Valid email")
    
    def test_secure_password_unvalid(self):
        self.assertEqual(secure_password("W"), "Password length must exceed 7 characters: ")
        self.assertEqual(secure_password("yummyyyyyyyyyy"), "Needs number and special character in password: ")
        self.assertEqual(secure_password("3tiggerrrr"), "Needs special character in password: ")
        


if __name__ == '__main__':
    unittest.main()