# _*_ coding: utf-8 _*_
from sqlalchemy import Integer, Column, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ChatbotTrainData(Base):
    __tablename__ = "chatbot_train_data"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    intent = Column(String(45), nullable=True)
    ner = Column(String(1024), nullable=True)
    query = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    answer_image = Column(String(2048), nullable=True)

    def __repr__(self):
        return "<ChatbotTrainData(id='%r', intent='%r', ner='%r')>" % (self.id, self.intent, self.ner)
