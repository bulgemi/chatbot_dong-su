# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


def connect_db(db_url, user_id, user_pw, pool_size=1):
    """
    Database 연결.
    :param db_url:
    :param user_id:
    :param user_pw:
    :param pool_size:
    :return:
    """
    db_url = db_url.format(user_id, user_pw)
    try:
        engine = create_engine(db_url, pool_size=pool_size, max_overflow=0,
                               pool_recycle=500, pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        return Session()
    except SQLAlchemyError as e:
        raise e


def disconnect_db(session):
    """
    Database 해제
    :param session:
    :return:
    """
    try:
        session.close()
    except SQLAlchemyError as e:
        raise e
