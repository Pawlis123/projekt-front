from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from Views import get_dict, widget
from Utils.ArticleManager import url_edit, url_delete


class ManageUrls(QMainWindow):
    new_urls_dict = {}

    def __init__(self):
        super(ManageUrls, self).__init__()
        loadUi("manageUrls.ui", self)
        self.addUrlButton.setStyleSheet(open("buttons.qss", "r").read())
        self.returnButton.setStyleSheet(open("buttons.qss", "r").read())
        self.removeButton.setStyleSheet(open("buttons.qss", "r").read())
        self.saveChangesButton.setStyleSheet(open("buttons.qss", "r").read())
        self.saveChangesButton.clicked.connect(self.save_changes)
        self.addUrlButton.clicked.connect(self.add_url)
        self.removeButton.clicked.connect(self.delete_item)
        self.returnButton.clicked.connect(self.go_back)
        self.init_combo_box()
        self.namesBox.setStyleSheet(open("comboBoxStyling.qss", "r").read())


    def init_combo_box(self):
        for key in get_dict().keys():
            self.namesBox.addItem(key)

    def add_url(self):
        key = self.nameBox.text()
        url = self.urlBox.text()
        if key and url:
            self.new_urls_dict[key] = url
        else:
            self.errorLabel.setText("Missing required information.")
        self.nameBox.setText("")
        self.urlBox.setText("")

    def save_changes(self):

        message = url_edit(self.new_urls_dict)
        self.errorLabel.setText(message)
        for entry in self.new_urls_dict.items():
            if not get_dict().get(entry[0]):
                self.namesBox.addItem(entry[0])
        self.new_urls_dict.clear()

    def delete_item(self):
        key = self.namesBox.currentText()
        index = self.namesBox.currentIndex()
        message = url_delete(key)
        self.errorLabel.setText(message)
        get_dict().pop(key)
        self.namesBox.removeItem(index)

    def go_back(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(self)
        widget.setFixedHeight(616)
        widget.setFixedWidth(1254)







