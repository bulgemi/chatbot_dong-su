# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
import pytest
from gensim.models import Word2Vec


@pytest.fixture
def load_model():
    return Word2Vec.load('../train_tools/word2vec/nvmc.model')


def test_corpus_total_words(load_model):
    model = load_model
    print('corpus_total_words: ', model.corpus_total_words)


def test_word2vec(load_model):
    model = load_model
    print('사랑: ', model.wv['사랑'])


def test_similarity(load_model):
    model = load_model
    print('일요일 == 월요일\t', model.wv.similarity(w1='일요일', w2='월요일'))
    print('안성기 == 배우\t', model.wv.similarity(w1='안성기', w2='배우'))
    print('대기업 == 삼성\t', model.wv.similarity(w1='대기업', w2='삼성'))
    print('일요일 != 삼성\t', model.wv.similarity(w1='일요일', w2='삼성'))
    print('히어로 != 삼성\t', model.wv.similarity(w1='히어로', w2='삼성'))


def test_most_similar(load_model):
    model = load_model
    print(model.wv.most_similar('안성기', topn=5))
    print(model.wv.most_similar('시리즈', topn=5))
