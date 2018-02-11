# coding=utf-8
from flask import Blueprint, render_template, request, make_response, session, redirect, url_for
from src.bengalistemmer.stemmer import BengaliStemmer
from .bengalisenttok import BengaliSentTok
import json
import operator
import math


# bnstemmer = Blueprint("bnstemmer", __name__, url_prefix="/wub/")
bnstemmer = Blueprint("bnstemmer", __name__)

@bnstemmer.route("/", methods=["GET", "POST"])
def stemmer():
    if request.method == "POST":
        document = request.form["bengali_document"]
        response = {}

        if len(document) > 0:
            pattern = r'[?|।!]'
            bn_tok = BengaliSentTok(document)
            bn_stem = BengaliStemmer()
            tokenized_sentences = bn_tok.bn_sentence_tok(pattern)
            tokenized_words = bn_tok.bn_word_tok(pattern)
            stem_words = []
            for sent_tokens in tokenized_words:
                stems = []
                for word in sent_tokens:
                    stems.append(bn_stem.stemmer(word))

                stem_words.append(stems)

            response["original_document"] = document
            response["tokenized_sentences"] = tokenized_sentences
            response["tokenized_words"] = tokenized_words
            response["stem_words"] = stem_words

        print(response)

        return render_template("bnstemmer/home.html", stem_response=response)

    return render_template("bnstemmer/home.html")

@bnstemmer.route("/download/", methods=["POST"])
def word_stem_download():
    if request.method == "POST":
        summery_content = request.form["summery_content"]
        response = make_response(summery_content)
        response.headers['Content-Disposition'] = 'attachment; filename=stem_words.txt'
        response.mimetype = 'text/txt'

        return response

