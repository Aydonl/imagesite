#coding:utf-8

from handlers.index import MainHandler
from handlers.login import LoginHandler

urls = [
(r'/', MainHandler),
(r'/login', LoginHandler),
]
