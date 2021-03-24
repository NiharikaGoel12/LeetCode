import unittest

from python.valid_anagram_242 import SolutionAnagram


class TestAnagram(unittest.TestCase):
    def setUp(self):
        self.sol = SolutionAnagram()

    def tearDown(self):
        self.sol = None

    def test_valid_anagram(self):
        assert self.sol.isAnagram(s = "rat", t = "car") == False
        assert self.sol.isAnagram(s = "tar", t = "rat") == True






