from playwright.sync_api import Page
from actors.actor import Actor

class Navigate:
    def navigate(self,page,url):
        Actor.goto(url)