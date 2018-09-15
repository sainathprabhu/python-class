import unittest
#import mylib
import sys
class MyTestCase(unittest.TestCase):
    @unitest.skip("demostrating skipping")
    def test_nothing(self):
        self.fail("Shouldn't happen")

    #@unittest.skip(mylib.__version__ < (1,3),
    #"not supported in 3.7
    #def test format(self):
        #test that work for only the a certain


    @unittest.skipUnless(sys.platform.startswith("win"),"requires windows")

    def test_windows_support(self):
        #windows specific testing code
        pass