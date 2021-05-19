from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea


class ItemsList(QWidget):
    def __init__(self, items, parent=None):
        super(ItemsList, self).__init__(parent)
        self.initWidget(items)
        self.setStyleSheet(open("itemListStyling.qss", "r").read())

    def initWidget(self, items):
        listBox = QVBoxLayout(self)
        self.setLayout(listBox)

        scroll = QScrollArea(self)
        scroll.setStyleSheet(open("scrollBarStyling.qss", "r").read())
        listBox.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scrollContent = QWidget(scroll)

        scrollLayout = QVBoxLayout(scrollContent)
        scrollContent.setLayout(scrollLayout)
        for item in items:
            scrollLayout.addWidget(item)
        scroll.setWidget(scrollContent)