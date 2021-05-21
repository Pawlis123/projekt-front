from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from Views import get_dict , add_entries
from Utils.UrlEdit import url_edit


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
        for key in self.new_urls_dict.keys():
            if not get_dict()[key]:
                self.namesBox.addItem(key)
        self.new_urls_dict.clear()
        self.namesBox.repaint()





