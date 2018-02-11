# coding=utf-8
import operator


class BengaliStemmer:

    def verb_stemmer(self, word):
        temp_stem = ''
        verb_suffixes = [
            'ছে', 'ছি', 'চ্ছি', 'ছিলা', 'ছিলাম', 'ছিলেন',
            'ছেন', 'লাম', 'ভাবে', 'ন', 'না', 'নো', 'নি', 'তে', 'তা',
            'তম', 'তিস', 'লি', 'য়া', 'কা', 'টা', 'ও', 'র'
        ]  # 'লেন', 'ন', 'নে',
        verb_suffixes_dict = {suffix: len(suffix) for index, suffix in enumerate(verb_suffixes)}
        verb_sorted_suffixes = sorted(verb_suffixes_dict.items(), key=operator.itemgetter(1), reverse=True)

        for verb_suffix in verb_sorted_suffixes:
            if len(temp_stem) > 4 and word.endswith(verb_suffix[0]):
                # print(verb_suffix[0])
                word = word.strip(verb_suffix[0])
                temp_stem = word
            else:
                temp_stem = word

        return temp_stem

    def noun_stemmer(self, word):
        noun_suffixes = [
            'ের', 'দেরকে', 'য়েদের', 'য়েদেরকে', 'দের', 'বাদীদের', 'বাদীদেরকে', 'ভাবে',
            'গত', 'গণ', 'য়ের', 'য়েরা', 'গুলো', 'গুলোতে', 'গুলোকে',
            'গুলি', 'টির', 'র', 'জন', 'টি', 'টির', 'কে', 'ই', 'খান', 'য়োন',
        ]
        noun_suffixes_dict = {suffix: len(suffix) for index, suffix in enumerate(noun_suffixes)}
        noun_sorted_suffixes = sorted(noun_suffixes_dict.items(), key=operator.itemgetter(1), reverse=True)

        for noun_suffix in noun_sorted_suffixes:
            if len(word) > 4 and word.endswith(noun_suffix[0]):
                word = word.strip(noun_suffix[0])

        return word

    def diacritic_stemmer(self, word):
        diacritic_suffixes = ['া', 'ি', 'ী', 'ু', 'ূ', 'ে', 'ৈ', 'ো', 'ৌ']
        diacritic_suffixes_dict = {suffix: len(suffix) for index, suffix in enumerate(diacritic_suffixes)}
        diacritic_sorted_suffixes = sorted(diacritic_suffixes_dict.items(), key=operator.itemgetter(1), reverse=True)

        # if len(word) < 4:
        for diacritic_suffix in diacritic_sorted_suffixes:
            if word.endswith(diacritic_suffix[0]):
                word = word.strip(diacritic_suffix[0])

        return word

    def special_word(self, word):
        special_word_dic = {
            'এগি': 'যাওয়া',
            'এগ': 'যাওয়া',
            'গিয়ে': 'যাওয়া',
            'খাই': 'খাওয়া',
            'যা': 'যাওয়া',
            'খা': 'খাওয়া',
            'দে': 'দেওয়া',
            'খাও': 'খাওয়া',
            'যাও': 'যাওয়া',
            'দেও': 'দেওয়া',
            'খেয়': 'খাওয়া',
            'চেয়': 'চাওয়া',
        }

        if word in special_word_dic:
            word = special_word_dic[word]

        return word

    def stemmer(self, word):

        if len(word) < 3:
            return word

        temp_verb_stem = self.verb_stemmer(word)
        temp_noun_stem = self.noun_stemmer(temp_verb_stem)
        temp_diacritic_stem = self.diacritic_stemmer(temp_noun_stem)
        temp_stem = self.special_word(temp_diacritic_stem)

        # if temp_stem word length 3 and endwith ও
        if len(temp_stem) == 3 and temp_stem.endswith('ও'):
            root = temp_stem.replace('ও', 'ওয়া')
        else:
            root = temp_stem

        return root