class News:
    """ represent a news, you can read it's title, it's content or go to it's web page """

    def __init__(self, url, title, category, subcategory):
        """ constructor for News class """
        self.__url = url
        self.__title = title
        self.__category = category
        self.__subcategory = subcategory
        self.__text = ""

    def scrape_text(self):
        """ go to the webpage of the news and scrape it's content text """

#####----------setter/getter----------#####

    @property
    def text(self):
        return self.__text

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def subcategory(self):
        return self.__subcategory

    @subcategory.setter
    def subcategory(self, value):
        self.__subcategory = value
