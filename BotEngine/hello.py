# _*_ coding: utf-8 _*_
from sanic import Sanic
from sanic.response import text, json

app = Sanic("My hello, world app")


@app.get("/")
async def hello_world(request):
    return text("Hello, world!")


async def bot_engine(request):
    callback = request.args.get('callback')
    msg = request.args.get('text')
    print("---------->%r" % callback)
    print("---------->%r" % msg)
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
        o = {"output": [
            {
                "type": "text",
                "delayMs": 1000,
                "value": f"'{msg}'라고 말했어요."
            }
        ]}

    res = f"{callback}({str(o)})"
    print(res)

    return text(res)

app.add_route(bot_engine, "/engine")
