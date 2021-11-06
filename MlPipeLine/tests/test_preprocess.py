# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
import sys
import os
import pytest
sys.path.append(os.getenv('CHATBOT_HOME'))
from MlPipeLine.utils.Preprocess import Preprocess


@pytest.fixture
def create_object():
    return Preprocess(userdic='../train_tools/dict/user_dic.tsv')


def test_pos_false(create_object):
    sent = '네임스페이스 목록 보여줘'
    print(sent)
    pos = create_object.pos(sent)
    ret = create_object.get_keywords(pos, without_tag=False)
    print(ret)


def test_pos_true(create_object):
    sent = '네임스페이스 목록 보여줘'
    pos = create_object.pos(sent)
    ret = create_object.get_keywords(pos, without_tag=True)
    print(ret)
