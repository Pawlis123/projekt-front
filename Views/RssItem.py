from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class RssItem(QWidget):
    linkStart = '<a style="text-decoration:none; color:#f77062;"href="'
    linkEnd = '">Go to article</a>'

    def __init__(self, title, link, date, source, parent=None):
        super(RssItem, self).__init__(parent)
        self.initWidget(title, link, date, source)
        self.setStyleSheet(open('widgetStyle.css').read())

    def initWidget(self, title, link_to_article, date, source):
        title = QLabel(title)
        date = QLabel(date)
        link = QLabel()
        source = QLabel(source)
        title.setStyleSheet("QLabel{font-weight: bold;}")
        if link_to_article:
            link.linkActivated.connect(self.link)
            link.setText(self.linkStart + link_to_article + self.linkEnd)
            link.setOpenExternalLinks(True)
        titleBox = QVBoxLayout()
        titleBox.addWidget(title)
        titleBox.addWidget(link)
        titleBox.addWidget(date)
        titleBox.addWidget(source)

        self.setLayout(titleBox)

    def link(self, linkstr):
        QDesktopServices.openUrl(linkstr)

        # class RssItem(QWidget):
        #     def __init__(self, title, date, parent=None):
        #         super(RssItem, self).__init__(parent)
        #         self.initWidget(title, date)
        #
        #     def initWidget(self, title, date):
        #         title = QLabel(title)
        #         date = QLabel(date)
        #         titleBox = QHBoxLayout()
        #         titleBox.addWidget(title)
        #         titleBox.addWidget(date)
        #         self.setLayout(titleBox)
