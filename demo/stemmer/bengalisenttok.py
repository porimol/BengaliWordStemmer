# coding=utf-8
from os.path import dirname, realpath
import re


class BengaliSentTok:
    def __init__(self, corpus):
        self._bangla_corpus = corpus

    def bn_corpus(self):
        bn_paragraphs = self._bangla_corpus

        return bn_paragraphs.strip('\n')

    def file_write(self, token_list, file_name):
        with open(file_name, 'w') as file:
            for index, token in enumerate(token_list):
                file.write(str(index + 1) + ') ' + token + '। \n')

    def bn_sentence_tok(self, pattern):
        corpus = self.bn_corpus()
        bn_tokens = re.split(pattern, corpus)

        return bn_tokens

    def bn_word_tok(self, pattern):
        word_tokens = []
        for tokenized_sent in self.bn_sentence_tok(pattern):
            word_list = tokenized_sent.split()
            word_tokens.append([word for word in word_list])

        return word_tokens

    def connecting_word(self, sentences):
        cw_file = 'connecting_words.txt'
        # get the files path
        file_dir_path = dirname(realpath(__file__))
        file = file_dir_path + "/" + cw_file
        with open(file) as cw:
            connecting_words = cw.readlines()

        cw = 0
        for cword in connecting_words:
            if cword.strip() in sentences:
                cw = 1

        return cw


if __name__ == "__main__":

    bangla_corpus = """ আমার দেশের  মাটি সোনার চেয়েও দামি। আমার দেশের  মাটি সোনার চেয়েও দামি"""
    pattern = r'[?|।!]'
    bn_tok = BengaliSentTok(bangla_corpus)
    tokenized_sentences = bn_tok.bn_sentence_tok(pattern)
    tokenized_words = bn_tok.bn_word_tok(pattern)
    print("Sentences Tokens: {}".format(tokenized_sentences))
    print("Words Tokens: {}".format(tokenized_words))
