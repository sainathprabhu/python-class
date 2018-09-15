import unittest

class TestStringmethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('kkar'.upper(),'KKAR')

    def test_isupper(self):
        self.assertTrue('KKAR'.isupper())
        #self.assertFalse('KKAR'.isupper())

    def test_split(self):
        s = 'Kkar technologies'
        self.assertEqual(s.split(),['Kkar','technologies'])



