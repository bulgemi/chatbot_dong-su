# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
import os
import sys
import pytest
sys.path.append(os.getenv('CHATBOT_HOME'))
from MlPipeLine.models.intent.intent_model import IntentModel
from MlPipeLine.utils.Preprocess import Preprocess


def test_intent_model():
    p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
                   userdic='../train_tools/dict/user_dic.tsv')
    intent = IntentModel(model_name='../models/intent/intent_model.h5',
                         preprocess=p)

    query = '네임스페이스 리스트 보여줘?'
    predict = intent.predict_class(query)
    predict_label = intent.labels[predict]

    print(query)
    print('의도 예측 클래스: ', predict)
    print('의도 예측 레이블: ', predict_label)
