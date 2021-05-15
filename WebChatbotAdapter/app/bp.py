# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'


def add_bp(app):
    """
    blueprints 등록
    :param app:
    :return:
    """
    from .adapter import webchatbot
    app.register_blueprint(webchatbot.bp)
