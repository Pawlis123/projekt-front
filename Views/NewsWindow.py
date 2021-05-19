from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from Views.ArticleList import ItemsList
from Views.RssItem import RssItem
from ArticleFetching.ArticleFetcher import article_fetch


class NewsWindow(QMainWindow):

    def __init__(self):
        super(NewsWindow, self).__init__()
        loadUi("newsWindow.ui", self)
        self.initUI()
        self.pushButton.setStyleSheet(open("buttons.qss", "r").read())
        self.pushButton_2.setStyleSheet(open("buttons.qss", "r").read())

    def initUI(self):
        items = []
        article_dict = article_fetch()
        if not article_dict:
            items.append(RssItem("There was no articles to fetch. Please provide urls.", '', ''))
        for dict_entry in article_dict.items():
            article_list = dict_entry[1]
            for article in article_list:
                items.append(RssItem(article[0], article[1], (article[2])[0:17], 'Source: ' + dict_entry[0]))
        self.containerLayout.addWidget(ItemsList(items))
