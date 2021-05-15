# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
from flask import Blueprint, render_template

bp = Blueprint('webchatbot', __name__, url_prefix='/webchatbot')


@bp.route('/example', methods=('GET', 'POST'))
def something():
    """
    webchatbot을 붙일수 있는 그 무엇.
    :return:
    """
    return render_template('example.html')
