# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
import os
import sys
sys.path.append(os.getenv('CHATBOT_HOME'))
from MlPipeLine.config.config import Config
from MlPipeLine.utils.db_utils import connect_db
from MlPipeLine.utils.db_utils import disconnect_db


def test_conn():
    try:
        session = connect_db(Config.DB_URL, Config.DB_ID, Config.DB_PASSWORD)
        disconnect_db(session)
        assert True
    except Exception as e:
        print(e)
        assert False
