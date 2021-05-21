from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from Views.ArticleList import ItemsList
from Views.RssItem import RssItem
from ArticleFetching.ArticleFetcher import article_fetch
from Views import widget, set_jwt, set_dict
from Views.ManageUrlsView import ManageUrls


class NewsWindow(QMainWindow):

    def __init__(self):
        super(NewsWindow, self).__init__()
        loadUi("newsWindow.ui", self)
        self.initUI()
        self.pushButton.setStyleSheet(open("buttons.qss", "r").read())
        self.pushButton_2.setStyleSheet(open("buttons.qss", "r").read())
        self.refreshButton.setStyleSheet(open("buttons.qss", "r").read())
        self.pushButton.clicked.connect(self.logging_out)
        self.pushButton_2.clicked.connect(self.go_to_manage)

    def initUI(self):
        items = []
        article_dict = article_fetch()
        set_dict(article_dict)
        if not article_dict:
            self.messageBox.setText("There was no articles to fetch. Please provide URLs.")
        for dict_entry in article_dict.items():
            article_list = dict_entry[1]
            for article in article_list:
                items.append(RssItem(article[0], article[1], (article[2])[0:17], 'Source: ' + dict_entry[0]))
        self.containerLayout.addWidget(ItemsList(items))

    def logging_out(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(self)
        widget.setFixedWidth(445)
        widget.setFixedHeight(554)
        set_jwt("")

    def go_to_manage(self):
        manage_view = ManageUrls()
        widget.addWidget(manage_view)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(445)
        widget.setFixedHeight(759)


