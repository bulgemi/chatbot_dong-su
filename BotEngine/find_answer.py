# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
from sqlalchemy import select, or_
from sanic.log import logger
from .models import ChatbotTrainData


class FindAnswer(object):
    def __init__(self, session):
        self.session = session

    async def search(self, intent_name, ner_tags):
        logger.debug("intent_name=%r, ner_tags=%r" % (intent_name, ner_tags))
        async with self.session.begin():
            try:
                stmt = select(ChatbotTrainData)
                stmt = stmt.filter_by(ChatbotTrainData.intent == intent_name)
                like_clause = list()
                for ne in ner_tags:
                    like_clause.append(ChatbotTrainData.ner.like("%{}%".format(ne)))
                stmt = stmt.filter_by(or_(tuple(like_clause)))
                results = await self.session.execute(stmt)
                row = results.first()
            except Exception as e:
                logger.error("Error: %r" % e)

        if row is None:
            async with self.session.begin():
                try:
                    stmt = select(ChatbotTrainData)
                    stmt = stmt.filter_by(ChatbotTrainData.intent == intent_name)
                    results = await self.session.execute(stmt)
                    row = results.first()
                except Exception as e:
                    logger.error("Error: %r" % e)

        return row['ChatbotTrainData'].answer, row['ChatbotTrainData'].anser_image

    def tag_to_word(self, ner_predicts, answer):
        for word, tag in ner_predicts:
            if tag == 'B_FOOD':
                answer = answer.replace(tag, word)
        answer = answer.replace('{', '')
        answer = answer.replace('}', '')
        return answer

