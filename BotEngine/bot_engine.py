# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
from sanic.response import text, json
from sanic import Blueprint
from sanic.log import logger
from sqlalchemy import select
from sqlalchemy import or_
from .models import ChatbotTrainData
from .find_answer import FindAnswer

bp = Blueprint('bot_engine')


@bp.route("/engine")
async def bot_engine(request):
    session = request.ctx.session
    callback = request.args.get('callback')
    msg = request.args.get('text')
    logger.debug("---------->%r" % callback)
    logger.debug("---------->%r" % msg)
    if msg == '버튼':
        o = {
            "output": [
                {
                    "type": "text",
                    "value": "버튼을 선택하세요."
                },
                {
                    "type": "option",
                    "options": [
                        {
                            "label": "사과",
                            "value": "_btn1_"
                        },
                        {
                            "label": "딸기",
                            "value": "_btn2_"
                        },
                        {
                            "label": "수박",
                            "value": "_btn3_"
                        }
                    ]
                }
            ]
        }
    elif msg == '사진' or msg == '이미지':
        o = {
            "output": [
                {
                    "type": "image",
                    "value": "https://miro.medium.com/max/1488/1*9iLNtPqNl9oDCnQimDxYBQ.png",
                }
            ]
        }
    elif msg == '동영상':
        o = {
            "output": [
                {
                    "type": "youtube",
                    "value": "IhzxnY7FIvg",
                }
            ]
        }
    elif msg == '링크':
        o = {
            "output": [
                {
                    "type": "html",
                    "value": "<a href=\"https://github.com/SEOTAEEYOUL/A-TCL-ChatOps\" target=\"_blank\" >링크 테스트</a> 입니다.",
                }
            ]
        }
    elif msg == '사진링크' or msg == '이미지링크':
        o = {
            "output": [
                {
                    "type": "html",
                    "value": "<a href=\"https://github.com/SEOTAEEYOUL/A-TCL-ChatOps\" target=\"_blank\" ><img src=\"https://miro.medium.com/max/1488/1*9iLNtPqNl9oDCnQimDxYBQ.png\" width=\"200\" alt=\"위의 이미지를 누르면 연결됩니다.\"></a>",
                }
            ]
        }
    elif msg == '사진버튼' or msg == '이미지버튼':
        o = {
            "output": [
                {
                    "type": "text",
                    "value": "버튼을 선택하세요."
                },
                {
                    "type": "image",
                    "value": "https://miro.medium.com/max/1488/1*9iLNtPqNl9oDCnQimDxYBQ.png"
                },
                {
                    "type": "option",
                    "options": [
                        {
                            "label": "사과",
                            "value": "_btn1_"
                        },
                        {
                            "label": "딸기",
                            "value": "_btn2_"
                        },
                        {
                            "label": "수박",
                            "value": "_btn3_"
                        }
                    ]
                }
            ]
        }
    elif msg == '_btn1_' or msg == '_btn2_' or msg == '_btn3_':
        m_map = {'_btn1_': '사과',
                 '_btn2_': '딸기',
                 '_btn3_': '수박'}
        o = {"output": [
            {
                "type": "text", "delayMs": 1000,
                "value": f"'{m_map[msg]}'를 눌렀습니다."
            }
        ]}
    else:
        predict = request.ctx.intent.predict_class(msg)
        intent_name = request.ctx.intent.labels[predict]
        predicts = request.ctx.ner.predict(msg)
        ner_tags = request.ctx.ner.predict_tags(msg)
        logger.debug("의도 파악: %r" % intent_name)
        logger.debug("개체명 인식: %r" % predicts)
        logger.debug("답변 검색에 필요한 NER 태그: %r" % ner_tags)
        try:
            f = FindAnswer(session)
            # answer_text, answer_image = f.search(intent_name, ner_tags)
            row = None
            async with session.begin():
                stmt = select(ChatbotTrainData)
                stmt = stmt.filter(ChatbotTrainData.intent == intent_name)
                if ner_tags is not None:
                    for ne in ner_tags:
                        stmt = stmt.filter(or_(ChatbotTrainData.ner.like("%{}%".format(ne)),))
                logger.debug(str(stmt))
                results = await session.execute(stmt)
                row = results.first()

            if row is None:
                async with session.begin():
                    stmt = select(ChatbotTrainData)
                    stmt = stmt.filter(ChatbotTrainData.intent == intent_name)
                    results = await session.execute(stmt)
                    row = results.first()
            msg = f.tag_to_word(predicts, row['ChatbotTrainData'].answer)
        except Exception as e:
            logger.error("Error: %r" % e)
            msg = "죄송해요, 무슨 말인지 모르겠어요."

        o = {"output": [
            {
                "type": "text",
                "delayMs": 1000,
                "value": f"{msg}"
            }
        ]}
    res = f"{callback}({str(o)})"
    logger.debug(res)

    return text(res)

