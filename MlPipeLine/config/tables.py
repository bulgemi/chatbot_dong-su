# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

Base = declarative_base()


class ChatbotTrainData(Base):
    __tablename__ = 'chatbot_train_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    intent = Column(String(45))
    ner = Column(String(1024))
    query = Column(Text)
    answer = Column(Text)
    answer_image = Column(String(2048))
    restful_url = Column(String(1024))
    res_type = Column(String(1))

    def __repr__(self):
        return "<ChatbotTrainData(id='%s', intent='%s', ner='%s')>" % (self.id, self.intent, self.ner)
