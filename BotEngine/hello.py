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
            "output": [{
                "type": "option",
                "options": [
                    {
                        "label": "버튼1",
                        "value": "value1"
                    },
                    {
                        "label": "버튼2",
                        "value": "value2"
                    },
                    {
                        "label": "버튼3",
                        "value": "value3"
                    }
                ]
            }]
        }
    elif msg == '사진':
        o = {
            "output": [{
                "type": "image",
                "value": "https://miro.medium.com/max/1488/1*9iLNtPqNl9oDCnQimDxYBQ.png"
            }]
        }
    elif msg == '동영상':
        o = {
            "output": [{
                "type": "youtube",
                "value": "IhzxnY7FIvg"
            }]
        }
    elif msg == '링크':
        o = {
            "output": [{
                "type": "html",
                "value": "<a href=\"https://github.com/SEOTAEEYOUL/A-TCL-ChatOps\" target=\"_blank\" >테스트 링크</a> 입니다.",
                "delayMs": 500
            }]
        }
    else:
        o = {"output": [{"type": "text", "value": f"'{msg}'라고 말했어요."}]}
    res = f"{callback}({str(o)})"
    print(res)
    return text(res)

app.add_route(bot_engine, "/engine")
