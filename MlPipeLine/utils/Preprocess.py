# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
from konlpy.tag import Komoran


class Preprocess(object):
    def __init__(self, userdic=None):
        """
        형태소 분석기 초기화
        제외할 품사 정의
        :param userdic:
        """
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
