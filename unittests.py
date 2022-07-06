import unittest
from emailValidator import get_email, secure_password


class TestFileName(unittest.TestCase):
    def test_get_email_true(self):
        self.assertEqual(get_email("nicole@gmail.com"), "Valid email")
        self.assertEqual(get_email("jacklack@yahoo.com"), "Valid email")
        self.assertEqual(get_email("ndemoura@uw.edu"), "Valid email")

    def test_get_email_false(self):
        self.assertEqual(get_email("nicole@gmail"), "Invalid email")
        self.assertEqual(get_email(""), "Invalid email")
        self.assertEqual(get_email(" "), "Invalid email")

    def test_secure_password_true(self):
        self.assertEqual(secure_password("LamaBeans4$"), "Valid email")
        self.assertEqual(secure_password("-humpdyDumpy27"), "Valid email")
        self.assertEqual(secure_password("yoGurtdreamS8999+"), "Valid email")
    
    def test_secure_password_false(self):
        self.assertEqual(secure_password("LamaBeans4$"), "Valid email")
        self.assertEqual(secure_password("-humpdyDumpy27"), "Valid email")
        self.assertEqual(secure_password("yoGurtdreamS8999+"), "Valid email")


if __name__ == '__main__':
    unittest.main()