# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def destroy(self):
        self.wd.quit()