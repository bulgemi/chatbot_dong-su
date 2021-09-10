# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
import os
import sys
import pytest
sys.path.append(os.getenv('CHATBOT_HOME'))
from MlPipeLine.config.config import Config
from MlPipeLine.config.tables import ChatbotTrainData
from MlPipeLine.utils.db_utils import connect_db
from MlPipeLine.utils.db_utils import disconnect_db


@pytest.fixture
def conn():
    session = connect_db(Config.DB_URL, Config.DB_ID, Config.DB_PASSWORD)
    return session


def test_insert(conn):
    from sqlalchemy.exc import IntegrityError

    new_row = ChatbotTrainData(
        id=1,
        intent='인사',
        ner='',
        query='안녕하세요',
        answer='네, 안녕하세요.:D\n반갑습니다. 저는 동수입니다.',
        answer_image='https://i.imgur.com/UluUFMp.jpg'
    )
    try:
        conn.add(new_row)
        conn.commit()
    except IntegrityError as e:
        print(e)
    disconnect_db(conn)


def test_select(conn):
    row = conn.query(ChatbotTrainData).filter_by(id=1).one()
    print(row.id, row.intent)
    disconnect_db(conn)


def test_update(conn):
    row = conn.query(ChatbotTrainData).filter_by(id=1).one()
    row.answer = '네, 안녕하세요.:D\n반갑습니다. 저는 챗봇 동수입니다.',
    conn.commit()
    disconnect_db(conn)


def test_delete(conn):
    row = conn.query(ChatbotTrainData).filter_by(id=1).one()
    conn.delete(row)
    conn.commit()
    disconnect_db(conn)
