'''unit test is a predefined module which is meant for testing the funct or code available with in the program'''

import unittest
class TestStringMethods(unittest.TestCase):
    def multiplication(self,a,b):
        return(a*b)
    def testmycode(self):
        self.assertEqual(self.multiplication(10,3),33)



''' assert equal is a predefined funct which will take two parameter to check the equality of the parameters'''