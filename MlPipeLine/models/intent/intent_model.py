# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
import os
import sys
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
from tensorflow.keras import preprocessing
sys.path.append(os.getenv('CHATBOT_HOME'))
from MlPipeLine.config.config import Config


class IntentModel(object):
    """
    의도 분류 모델 모듈
    """
    def __init__(self, model_name, preprocess):
        """
        -의도 클래스별 레이블
        -의도 분류 모델 불러오기
        -chatbot preprocess 객체
        :param model_name:
        :param preprocess:
        """
        self.labels = {
            0: '인사',
            1: '욕설',
            2: '주문',
            3: '예약',
            4: '기타'
        }
        self.model = load_model(model_name)
        self.p = preprocess

    def predict_class(self, query):
        """
        의도 클래스 예측
        :param query:
        :return:
        """
        # 형태소 분석
        pos = self.p.pos(query)
        # 문장 내 키워드 추출(불용어 제거)
        keywords = self.p.get_keywords(pos, without_tag=True)
        sequences = [self.p.get_wordidx_sequence(keywords)]
        # 패딩 처리
        padded_seqs = preprocessing.sequence.pad_sequences(sequences,
                                                           maxlen=Config.MAX_SEQ_LEN,
                                                           padding='post')
        predict = self.model.predict(padded_seqs)
        predict_class = tf.math.argmax(predict, axis=1)
        return predict_class.numpy()[0]
