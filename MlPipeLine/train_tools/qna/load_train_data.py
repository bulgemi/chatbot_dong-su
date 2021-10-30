# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
import os
import sys
import math
import pandas as pd
sys.path.append(os.getenv('CHATBOT_HOME'))
from MlPipeLine.config.config import Config
from MlPipeLine.config.tables import ChatbotTrainData
from MlPipeLine.utils.db_utils import connect_db
from MlPipeLine.utils.db_utils import disconnect_db


def all_clear_train_data(session):
    """
    기존 학습 데이터 삭제
    :param session:
    :return:
    """
    try:
        session.query(ChatbotTrainData).delete()
        session.execute("ALTER TABLE chatbot_train_data AUTO_INCREMENT=1")
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise e


def insert_data(session, xls_row):
    """
    DB에 데이터 저장
    :param session:
    :param xls_row:
    :return:
    """
    intent = str(xls_row['의도(Intent)']) if str(xls_row['의도(Intent)']) != 'nan' else ''
    ner = str(xls_row['개체명(NER)']) if str(xls_row['개체명(NER)']) != 'nan' else ''
    query = str(xls_row['질문(Query)']) if str(xls_row['질문(Query)']) != 'nan' else ''
    answer = str(xls_row['답변(Answer)']) if str(xls_row['답변(Answer)']) != 'nan' else ''
    answer_image = str(xls_row['답변 이미지']) if str(xls_row['답변 이미지']) != 'nan' else ''
    restful_url = str(xls_row['RESTFul_URL']) if str(xls_row['RESTFul_URL']) != 'nan' else ''
    res_type = str(xls_row['RES_TYPE']) if str(xls_row['RES_TYPE']) != 'nan' else ''

    try:
        new_row = ChatbotTrainData(
            intent=intent,
            ner=ner,
            query=query,
            answer=answer,
            answer_image=answer_image,
            restful_url=restful_url,
            res_type=res_type
        )
        session.add(new_row)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise e


train_file = './train_data.xlsx'
session = connect_db(Config.DB_URL, Config.DB_ID, Config.DB_PASSWORD)
all_clear_train_data(session)
excel = pd.read_excel(train_file, sheet_name='Sheet1')
print(excel)
for idx, row in excel.iterrows():
    insert_data(session, row)
disconnect_db(session)
