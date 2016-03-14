#coding:utf-8

import tornado.web
from model.entity import Entity
from base import BaseHandler

class MainHandler(BaseHandler):
  @tornado.web.authenticated
  def get(self):
    #entity = Entity.get('the5fire\'s blog')
    name = tornado.escape.xhtml_escape(self.current_user)
    #self.render('index.html', entity = 'Aydon')
    self.render('index.html', username = name)
