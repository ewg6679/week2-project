import unittest
from emailValidator import get_email, secure_password


class TestFileName(unittest.TestCase):
    def test_get_email_valid(self):
        self.assertEqual(get_email("nicole@gmail.com"), True)
        self.assertEqual(get_email("jacklack@yahoo.com"), True)
        self.assertEqual(get_email("ndemoura@uw.edu"), True)

    def test_get_email_unvalid(self):
        self.assertEqual(get_email("nicole@gmail"), False)
        self.assertEqual(get_email(""), False)
        self.assertEqual(get_email(" "), False)
        self.assertEqual(get_email("hghkdnlsdpksl"), False)

    def test_secure_password_valid(self):
        self.assertEqual(secure_password("LamaBeans4$"), True)
        self.assertEqual(secure_password("-humpdyDumpy27"), True)
        self.assertEqual(secure_password("yoGurtdreamS8999+"), True)
    
    def test_secure_password_unvalid(self):
        self.assertEqual(secure_password("W"), False)
        self.assertEqual(secure_password("yummyyyyyyyyyy"), False)
        self.assertEqual(secure_password("3tiggerrrr"), False)
        


if __name__ == '__main__':
    unittest.main()