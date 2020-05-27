import unittest
from reverse_words import reverse_words

class TestCalc(unittest.TestCase):

    def test_reverse_words(self):
        result = reverse_words.reverse_words('The quick brown fox jumps over the lazy dog.')
        self.assertEqual(result, 'ehT kciuq nworb xof spmuj revo eht yzal .god')
