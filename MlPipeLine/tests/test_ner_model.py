# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
import os
import sys
sys.path.append(os.getenv('CHATBOT_HOME'))
from MlPipeLine.utils.Preprocess import Preprocess
from MlPipeLine.models.ner.ner_model import NerModel


def test_ner_model():
    p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
                   userdic='../train_tools/dict/user_dic.tsv')
    ner = NerModel(model_name='../models/ner/ner_model.h5', preprocess=p)
    query = '오늘 오후 1시 2분에 탕수육 주문하고 싶어요'
    predicts = ner.predict(query)
    print(predicts)
