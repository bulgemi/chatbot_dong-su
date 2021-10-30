# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
import os
import sys
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
from tensorflow.keras import preprocessing


class NerModel(object):
    """
    개체명 인식 모델 객체
    """
    def __init__(self, model_name, preprocess):
        """
        - BIO 태그 클래스별 레이블
        - 의도 분류 모델 물러오기
        - 챗봇 preprocess 객체
        :param model_name:
        :param preprocess:
        """
        self.index_to_ner = {
            1: 'O',
            2: 'B_DT',
            3: 'B_FOOD',
            4: 'I',
            5: 'B_OG',
            6: 'B_PS',
            7: 'B_LC',
            8: 'NNP',
            9: 'B_TI',
            0: 'PAD',
            10: 'B_NAMESPACE',
            11: 'I_NAMESPACE',
        }
        self.model = load_model(model_name)
        self.p = preprocess

    def predict(self, query):
        """
        개체명 클래스 예측
        :param query:
        :return:
        """
        pos = self.p.pos(query)  # 형태소 분석
        keywords = self.p.get_keywords(pos, without_tag=True)  # 문장 내 키워드 추출(불용어 제거)
        sequences = [self.p.get_wordidx_sequence(keywords)]
        # 패딩 처리
        max_len = 40
        padded_seqs = preprocessing.sequence.pad_sequences(sequences,
                                                           padding='post',
                                                           value=0,
                                                           maxlen=max_len)
        # 키워드별 개체명 예측
        predict = self.model.predict(np.array([padded_seqs[0]]))
        predict_class = tf.math.argmax(predict, axis=-1)
        tags = [self.index_to_ner[i] for i in predict_class.numpy()[0]]
        return list(zip(keywords, tags))

    def predict_tags(self, query):
        """
        태그 예측
        :param query:
        :return:
        """
        pos = self.p.pos(query)  # 형태소 분석
        # 문장 내 키워드 추출(불용어 제거)
        keywords = self.p.get_keywords(pos, without_tag=True)
        sequences = [self.p.get_wordidx_sequence(keywords)]
        # 패딩 처리
        max_len = 40
        padded_seqs = preprocessing.sequence.pad_sequences(sequences,
                                                           padding='post',
                                                           value=0,
                                                           maxlen=max_len)
        predict = self.model.predict(np.array([padded_seqs[0]]))
        predict_class = tf.math.argmax(predict, axis=-1)
        tags = []
        for tag_idx in predict_class.numpy()[0]:
            if tag_idx == 1:
                continue
            tags.append(self.index_to_ner[tag_idx])
        if len(tags) == 0:
            return None
        return tags
