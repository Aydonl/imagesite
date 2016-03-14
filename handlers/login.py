#coding:utf-8

import tornado.web

class LoginHandler(tornado.web.RequestHandler):
  def get(self):
    self.render('page_login.html')
  def post(self):
    user =  tornado.escape.xhtml_escape(self.get_argument('username'))
    #passwd = self.get_argument('password')
    passwd = tornado.escape.xhtml_escape(self.get_argument('password'))
    result = user +'</br>'+ passwd
    #self.write(result)
    self.set_secure_cookie("user",user)
    self.redirect("/")
