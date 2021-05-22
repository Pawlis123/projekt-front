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
        self.refreshButton.clicked.connect(self.refresh)
        self.widgetRef = None

    def initUI(self):
        items = []
        article_dict = article_fetch()
        set_dict(article_dict)
        if not article_dict:
            self.messageBox.setText("There was no articles to fetch. Please provide URLs or refresh.")
        for dict_entry in article_dict.items():
            article_list = dict_entry[1]
            for article in article_list:
                items.append(RssItem(article[0], article[1], (article[2])[0:17], 'Source: ' + dict_entry[0]))
        item_list = ItemsList(items)
        self.widgetRef = item_list
        self.containerLayout.addWidget(item_list)

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

    def refresh(self):
        try:
            self.messageBox.setText("Loading...")
            self.messageBox.repaint()
            self.containerLayout.itemAt(0).widget().deleteLater()
            self.initUI()
            self.messageBox.repaint()
            if self.messageBox.text() == "Loading...":
                self.messageBox.setText("")
                self.messageBox.repaint()
        except Exception as e:
            print(e)
