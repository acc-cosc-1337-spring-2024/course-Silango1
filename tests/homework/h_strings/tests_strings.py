# /tests/homework/h_strings/test_strings.py

import unittest
from homework.h_strings.tests_strings import get_hamming_distance, get_dna_complement

class TestStrings(unittest.TestCase):

    def test_get_hamming_distance(self):
        """
        Test case for get_hamming_distance function.
        """
        dna1 = "GAGCCTACTAACGGGAT"
        dna2 = "CATCGTAATGACGGCCT"
        expected_distance = 7
        self.assertEqual(get_hamming_distance(dna1, dna2), expected_distance)

    def test_get_dna_complement(self):
        """
        Test case for get_dna_complement function.
        """
        dna = "AAAACCCGGT"
        expected_complement = "ACCGGGTTTT"
        self.assertEqual(get_dna_complement(dna), expected_complement)

if __name__ == '__main__':
    unittest.main()
