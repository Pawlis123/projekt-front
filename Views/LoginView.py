from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QSizePolicy
from PyQt5.uic import loadUi
import requests
from Views import widget
from Views.CreateAccountView import CreateAccount
from Views import set_jwt
from Views.NewsWindow import NewsWindow


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("loginpage.ui", self)
        self.loginButton.setStyleSheet(open("buttons.qss", "r").read())
        self.registerButton.setStyleSheet(open("buttons.qss", "r").read())
        self.loginButton.clicked.connect(self.login_function)
        self.registerButton.clicked.connect(self.go_to_create)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def login_function(self):
        login = self.login.text()
        password = self.password.text()
        self.login.setText("")
        self.password.setText("")
        testobj = {'username': login, 'password': password}
        try:
            authorization_content = requests.post('http://127.0.0.1:5000/api/login', json=testobj)
        except:
            self.errorLabel.setText("No internet connection.")
            return
        if authorization_content.status_code != 200:
            self.errorLabel.setText("Incorrect login credentials")
        elif authorization_content:
            token = authorization_content.json()["access_token"]
            set_jwt(token)
            self.go_to_news_window()

    def go_to_create(self):
        create_account = CreateAccount()
        widget.addWidget(create_account)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_to_news_window(self):
        self.errorLabel.setText("Loading...")
        self.errorLabel.repaint()
        test = NewsWindow()
        self.errorLabel.setText("")
        self.errorLabel.repaint()
        widget.addWidget(test)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedHeight(622)
        widget.setFixedWidth(1021)

