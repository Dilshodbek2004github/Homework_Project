from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QIcon
from components import *
from database import Database

class Kasalxona(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500,600)
        self.setWindowTitle("Kasalxona boshqaruv tizimi")
        self.setWindowIcon(QIcon("logo.jpg"))
        self.setStyleSheet("background-color: lightblue;")
        self.signupBtn = Button1("Ro'yxatdan o'tish", self)
        self.signupBtn.move(100,180)
        self.signupBtn.clicked.connect(self.show_signup_page)
        self.loginBtn = Button2("Tizim ga kirish", self)
        self.loginBtn.move(100,260)
        self.loginBtn.clicked.connect(self.show_login_page)
        self.label = Label("Kasalxona boshqaruv tizimi", self)
        self.label.move(70,100)

    def show_login_page(self):
        login_Page = LogIn()
        if login_Page.exec_() == QDialog.Accepted:
            self.show_second_window()
    def show_signup_page(self):
        signup_Page = SignUp()
        if signup_Page.exec_() == QDialog.Accepted:
            self.show_second_window()
    def show_second_window(self):
        self.second_Window = SecondWindow()
        self.second_Window.show()
        




app = QApplication([])
oyna = Kasalxona()
oyna.show()
app.exec()
