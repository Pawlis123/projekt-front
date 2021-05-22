from PyQt5.QtCore import Qt

from Views import widget, app
from Views.LoginView import Login

main_window = Login()
widget.addWidget(main_window)
widget.setFixedWidth(445)  #445
widget.setFixedHeight(554) #554
# widget.setWindowFlag(Qt.FramelessWindowHint)
widget.show()
app.exec_()
