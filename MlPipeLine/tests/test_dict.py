# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
import os
import sys
import pickle
import pytest
sys.path.append(os.getenv('CHATBOT_HOME'))
from MlPipeLine.utils.Preprocess import Preprocess


def test_dict():
    f = open("../train_tools/dict/chatbot_dict.bin", 'rb')
    word_index = pickle.load(f)
    f.close()

    sent = "내일 오전 10시에 탕수육 주문하고 싶어 ㅋㅋ"

    # 전처리 객체 생성
    p = Preprocess(userdic='../train_tools/dict/user_dic.tsv')
    # 형태소 분석기 실행
    pos = p.pos(sent)
    # 품사 태그 없이 키워드 출력
    keywords = p.get_keywords(pos, without_tag=True)
    for word in keywords:
        try:
            print(word, word_index[word])
        except KeyError:
            # 해당 언어가 사전에 없는 경우 OOV 처리
            print(word, word_index['OOV'])
