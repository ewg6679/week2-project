import unittest
from email_validator import get_email, secure_password, make_account, log_in, sign_up


class TestFileName(unittest.TestCase):
    def test_get_email_valid(self):
        self.assertEqual(get_email("nicoledemoura4@gmail.com"), True)
        self.assertEqual(get_email("jacklack@yahoo.com"), True)
        self.assertEqual(get_email("ndemoura@uw.edu"), True)

    def test_get_email_unvalid(self):
        self.assertEqual(get_email("nicole@gmail"), False)
        self.assertEqual(get_email(""), False)
        self.assertEqual(get_email(" "), False)
        self.assertEqual(get_email("hghkdnlsdpksl"), False)

    def test_secure_password_valid(self):
        self.assertEqual(secure_password("-humpdyDumpy27"), True)
        self.assertEqual(secure_password("yoGurtdreamS8999+"), True)
        self.assertEqual(secure_password("tommorowis89^"), True)
    
    def test_secure_password_unvalid(self):
        self.assertEqual(secure_password("W"), False)
        self.assertEqual(secure_password("yummyyyyyyyyyy"), False)
        self.assertEqual(secure_password("3tiggerrrr"), False)

    def test_make_account_true(self):
        self.assertEqual(make_account("nicolesmithh@gmail.com", "Rockstar5#@"), True)
        self.assertEqual(make_account("nicolesmith123@gmail.com", "Rockstar5#@"), True)
        self.assertEqual(make_account("nicolesmith321@gmail.com", "Rockstar5#@"), True)

    def test_make_account_false(self):
        self.assertEqual(make_account("ndemoura@uw.edu", "Rockstar5#@"), False)
        self.assertEqual(make_account("ndemoura@cs.washington.edu", "Rockstar5#@"), False)
        self.assertEqual(make_account("nicoledemoura4@gmail.com", "Rockstar5#@"), False)
    
    def test_log_in_true(self):
        self.assertEqual(log_in("nicolerock@gmail.com"), True)
        self.assertEqual(log_in("nicolebrown@gmail.com"), True)
        self.assertEqual(log_in("nickrock@gmail.com"), True)

    def test_log_in_false(self):
        self.assertEqual(log_in("ndemoura@uw.edu"), False)
        self.assertEqual(log_in("ndemoura@cs.washington.edu"), False)
        self.assertEqual(log_in("nicoledemoura4@gmail.com"), False)

    def test_sign_up_true(self):
        self.assertEqual(sign_up("nick@gmail.com"), True)
        self.assertEqual(sign_up("kesley@gmail.com"), True)
        self.assertEqual(log_in("bellinello@gmail.com"), True)
    
    def test_sign_up_false(self):
        self.assertEqual(sign_up("ndemoura@uw.edu"), False)
        self.assertEqual(sign_up("ndemoura@cs.washington.edu"), False)
        self.assertEqual(sign_up("nicoledemoura4@gmail.com"), False)

if __name__ == '__main__':
    unittest.main()