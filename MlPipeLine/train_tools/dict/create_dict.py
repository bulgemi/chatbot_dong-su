# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
import sys
import os
import pickle
from tensorflow.keras import preprocessing
sys.path.append(os.getenv('CHATBOT_HOME'))
from MlPipeLine.utils.Preprocess import Preprocess


def read_corpus_data(filename):
    """
    말뭉치 데이터 읽어오기
    :param filename:
    :return:
    """
    with open(filename, 'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]  # 헤더 제거
    return data


# 말뭉치 가져오기
corpus_data = read_corpus_data('./corpus.txt')

# 키워드 사전 리스트 생성
p = Preprocess()
dict = []
for c in corpus_data:
    pos = p.pos(c[1])
    print("pos=%r" % pos)
    for k in pos:
        dict.append(k[0])
# 사전에 사용될 word2index 생성
# 사전의 첫 번째 index에는 OOV 사용
tokenizer = preprocessing.text.Tokenizer(oov_token='OOV')
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index

# 사전 파일 생성
f = open("chatbot_dict.bin", "wb")
try:
    pickle.dump(word_index, f)
except Exception as e:
    print(e)
finally:
    f.close()
