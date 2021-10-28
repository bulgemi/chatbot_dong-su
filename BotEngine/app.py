# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
import os, sys
from sanic import Sanic
from sanic.log import logger
from contextvars import ContextVar
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
sys.path.append(os.getenv('CHATBOT_HOME'))
from BotEngine.bot_engine import bp
from BotEngine.error_handling import err_bp
from MlPipeLine.utils.Preprocess import Preprocess
from MlPipeLine.models.intent.intent_model import IntentModel
from MlPipeLine.models.ner.ner_model import NerModel

app = Sanic(__name__)
app.blueprint(bp)
app.blueprint(err_bp)
bind = create_async_engine("mysql+aiomysql://chatbot_appl:chatbot_appl!@localhost/chatbot_db?charset=utf8mb4",
                           echo=True, pool_recycle=500)
_base_model_session_ctx = ContextVar('session')


@app.listener("before_server_start")
async def setup_ml_db(app, loop):
    logger.debug("call listener")
    p = Preprocess(word2index_dic='../MlPipeLine/train_tools/dict/chatbot_dict.bin',
                   userdic='../MlPipeLine/train_tools/dict/user_dic.tsv')
    app.ctx.intent = IntentModel(model_name='../MlPipeLine/models/intent/intent_model.h5',
                                 preprocess=p)
    app.ctx.ner = NerModel(model_name='../MlPipeLine/models/ner/ner_model.h5',
                           preprocess=p)
    # app.ctx.session = sessionmaker(bind, AsyncSession, expire_on_commit=False)()
    # app.ctx.session_ctx_token = _base_model_session_ctx.set(app.ctx.session)


# @app.listener("after_server_stop")
# async def setup_ml_db(app, loop):
#     if hasattr(app.ctx, "session_ctx_token"):
#         _base_model_session_ctx.reset(app.ctx.session_ctx_token)
#         await app.ctx.session.close()


@app.middleware('request')
async def inject_session(request):
    request.ctx.session = sessionmaker(bind, AsyncSession, expire_on_commit=False)()
    request.ctx.session_ctx_token = _base_model_session_ctx.set(request.ctx.session)


@app.middleware('response')
async def close_session(request, response):
    if hasattr(request.ctx, "session_ctx_token"):
        _base_model_session_ctx.reset(request.ctx.session_ctx_token)
        await request.ctx.session.close()

if __name__ == '__main__':
    app.run(debug=True, access_log=True)
