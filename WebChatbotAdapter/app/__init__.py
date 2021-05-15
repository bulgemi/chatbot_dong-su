# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
import os
from flask import Flask, render_template


def create_app(test_config=None):
    """
    Create and configure an instance of the WebChatbotAdapter
    :param test_config:
    :return:
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dc45892e-b47a-11eb-8fb8-cb630e6a6f16'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    from .bp import add_bp
    add_bp(app)

    return app
