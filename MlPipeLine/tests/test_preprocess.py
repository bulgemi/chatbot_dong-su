# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
import sys
import os
import pytest
sys.path.append(os.getenv('CHATBOT_HOME'))
from MlPipeLine.utils.Preprocess import Preprocess


@pytest.fixture
def create_object():
    return Preprocess(userdic='../utils/user_dic.tsv')


def test_pos_false(create_object):
    sent = '내일 오전 10시에 탕수육 주문하고 싶어'
    pos = create_object.pos(sent)
    ret = create_object.get_keywords(pos, without_tag=False)
    print(ret)


def test_pos_true(create_object):
    sent = '내일 오전 10시에 탕수육 주문하고 싶어'
    pos = create_object.pos(sent)
    ret = create_object.get_keywords(pos, without_tag=True)
    print(ret)
