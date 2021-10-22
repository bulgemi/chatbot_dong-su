# _*_ coding: utf-8 _*_
__author__ = 'kim dong-hun'
from sanic.response import text
from sanic import Blueprint
from sanic.exceptions import NotFound

err_bp = Blueprint('error_handling')


@err_bp.exception(NotFound)
def ignore_404s(request, exception):
    return text("Yep, I totally found the page: {}".format(request.url))
