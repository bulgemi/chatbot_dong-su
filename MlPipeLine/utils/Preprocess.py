# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
from konlpy.tag import Komoran
import pickle


class Preprocess(object):
    def __init__(self, word2index_dic='', userdic=None):
        """
        형태소 분석기 초기화
        제외할 품사 정의
        :param word2index:
        :param userdic:
        """
        # 단어 인덱스 사전 불러오기
        self.word_index = None
        if word2index_dic != '':
            f = open(word2index_dic, 'rb')
            self.word_index = pickle.load(f)
            f.close()
        self.komoran = Komoran(userdic=userdic)
        self.exclusion_tags = [
            'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ', 'JX', 'JC',
            'SF', 'SP', 'SS', 'SE', 'SO',
            'EP', 'EF', 'EC', 'ETN', 'ETM',
            'XSN', 'XSV', 'XSA'
        ]

    def pos(self, sentence):
        """
        형태소 분석기 POS Tag
        :param sentence:
        :return:
        """
        return self.komoran.pos(sentence)

    def get_keywords(self, pos, without_tag=False):
        """
        불용어 제거 후 필요한 품사 정보만 가져오기
        :param pos:
        :param without_tag:
        :return:
        """
        f = lambda x: x in self.exclusion_tags
        word_list = list()
        for p in pos:
            if f(p[1]) is False:
                word_list.append(p if without_tag is False else p[0])
        return word_list

    def get_wordidx_sequence(self, keywords):
        """
        키워드로 단어 인덱스 시퀀스 변환
        :param keywords:
        :return:
        """
        if self.word_index is None:
            return []
        w2i = []
        for word in keywords:
            try:
                w2i.append(self.word_index[word])
            except KeyError:
                # 해당 단어가 없을 경우 OOV 처리
                w2i.append(self.word_index['OOV'])
        return w2i
