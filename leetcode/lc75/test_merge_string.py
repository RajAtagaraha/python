import unittest
from python.leetcode.lc75.merge_string_alternately import Solution

class MyTest(unittest.TestCase):
    def test_one(self):
        word1 = "abc"
        word2 = "pqr"
        expected_result = "apbqcr"
        self.assertEqual(Solution().mergeAlternately(word1,word2),expected_result)

    def test_two(self):
        word1 = "abcd"
        word2 = "pq"
        expected_result = "apbqcd"
        self.assertEqual(Solution().mergeAlternately(word1, word2), expected_result)

    def test_three(self):
        word1 = "abcd"
        word2 = "pq"
        expected_result = "aqcd"
        self.assertNotEqual(Solution().mergeAlternately(word1, word2), expected_result)
