# coding=utf-8

from unittest import TestCase
from src.bengalistemmer.stemmer import BengaliStemmer


class TestBengaliStemmer(TestCase):

    def test_verb_stemmer(self):
        bn_stem = BengaliStemmer()
        self.assertEqual(bn_stem.verb_stemmer('বলেছেন'), 'বল')

    def test_noun_stemmer(self):
        bn_stem = BengaliStemmer()
        self.assertEqual(bn_stem.noun_stemmer('আমি'), 'আমি')
        self.assertEqual(bn_stem.noun_stemmer('আমরা'), 'আমরা')

    def test_diacritic_stemmer(self):
        bn_stem = BengaliStemmer()
        self.assertEqual(bn_stem.diacritic_stemmer('বলে'), 'বল')

    def test_special_word(self):
        bn_stem = BengaliStemmer()
        self.assertEqual(bn_stem.special_word('যাও'), 'যাওয়া')
        self.assertEqual(bn_stem.special_word('দেও'), 'দেওয়া')

    def test_stemmer(self):
        bn_stem = BengaliStemmer()
        self.assertEqual(bn_stem.stemmer('বলেছেন'), 'বল')
        self.assertEqual(bn_stem.stemmer('খেয়েছেন'), 'খাওয়া')
