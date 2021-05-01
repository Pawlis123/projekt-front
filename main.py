import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
import requests


class CreateAccount(QDialog):
    def __init__(self):
        super(CreateAccount, self).__init__()
        loadUi("registerpage.ui", self)
        self.createAccountButton.clicked.connect(self.register_function)
        self.returnButton.clicked.connect(self.return_function)


    def register_function(self):
        username = self.username.toPlainText()
        password = self.password.text()
        confirm_password = self.repeatPassword.text()
        if password != confirm_password:
            print("wrooong")
        else:
            print("correct")

    def return_function(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("loginpage.ui", self)
        self.loginButton.clicked.connect(self.login_function)
        self.registerButton.clicked.connect(self.go_to_create)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def login_function(self):
        login = self.login.toPlainText()
        password = self.password.text()
        self.login.setPlainText("")
        self.password.setText("")
        testobj = {'username': login, 'password': password}
        x = requests.post('http://127.0.0.1:5000/api/login', json=testobj)
        if x.status_code != 200:
            self.errorLabel.setText("Incorrect login credentials")
        else:
            print(x.text)

    def go_to_create(self):
        createacc = CreateAccount()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
main_window = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_window)
widget.setFixedWidth(445)
widget.setFixedHeight(554)
widget.show()
app.exec_()
