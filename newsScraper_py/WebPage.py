from typing import List, Any
from News import News


class WebPage:
    """ represent a web page with news you can read
        the news on the current page or navigate to other pages """
    __nav_bar: List["WebPage"]
    __top_news: List[News]

    def __init__(self, url, category, subcategory):
        """ constructor for WebPage class """
        self.__url = url
        self.__category = category
        self.__subcategory = subcategory
        self.__top_news = []
        self.__nav_bar = []

    def scrape_top_news(self):
        """ go to the webpage url and scrape it's top news """

    def scrape_nav_bar(self):
        """ ge to the webpage url and scrape it's navbar """

#####----------setter/getter----------#####

    @property
    def url(self):
        return self.__url
    
    @url.setter
    def url(self, value):
        self.__url = value
    
    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self, value):
        self.__category
    
    @property
    def subcategory(self):
        return self.__subcategory
    
    @subcategory.setter
    def subcategory(self, value):
        self.__subcategory
    
    @property
    def top_news(self):
        return self.__top_news

    @property
    def nav_bar(self):
        return self.__nav_bar
