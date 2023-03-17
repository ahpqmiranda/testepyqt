import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QMessageBox
from PyQt6.QtCore import Qt, QEvent, QSize

import main
from login_form import Ui_login_form


class login(QWidget):
    def __init__(self):
        super().__init__()
        # set up the UI
        self.ui = Ui_login_form()
        self.ui.setupUi(self)
        # connect the button to the function on_click
        self.ui.btn_login.clicked.connect(self.authenticate)

        self.show()

    def authenticate(self):
        email = self.ui.email_line_edit.text()
        password = self.ui.password_line_edit.text()

        if email == "admin" and password == "admin":
            QMessageBox.information(self, "Sucess", "Login Successful")
            main.main_window = main.MainWindow()
            main.main_window.show()

            self.close()

        else:
            QMessageBox.information(self, "Error", "Login Failed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = login()
    sys.exit(app.exec())

