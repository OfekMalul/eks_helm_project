# Author: Ofek Malul
# Date: 3/12/2023
# Reviewer: Idan

# urllib is a package that has modules that works with urls
# request - open and read urls
from urllib.request import urlopen
import unittest


def checkWebsite(url):
    try:
        urlopen(url)
        return True
    except Exception as e:
        print("Error was found: ",e)
        return False

class TestWebsite(unittest.TestCase):
    def testWebsiteReachable(self):
        self.assertTrue(checkWebsite('http://localhost:9090'))

if __name__ == "__main__":
    unittest.main()
