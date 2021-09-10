# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'


class Config(object):
    # 단어 시퀀스 벡터 크기
    MAX_SEQ_LEN = 15
    # Database 설정.
    # db name: chatbot_db, id: chatbot_appl, password: chatbot_appl!
    DB_URL = "mysql+pymysql://{0}:{1}@localhost/chatbot_db?charset=utf8mb4"
    DB_ID = 'chatbot_appl'
    DB_PASSWORD = 'chatbot_appl!'
