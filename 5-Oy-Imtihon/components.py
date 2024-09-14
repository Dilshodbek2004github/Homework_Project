from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QIntValidator

from database import Database

class Button1(QPushButton):
    def __init__(self, text: str, oyna: QWidget):
        super().__init__(oyna)
        self.setText(text)
        self.resize(300,50)
        self.setStyleSheet("background-color: green; color: white; font-size: 30px;")

class Button2(QPushButton):
    def __init__(self, text: str, oyna: QWidget):
        super().__init__(oyna)
        self.setText(text)
        self.resize(300,50)
        self.setStyleSheet("background-color: blue; color: white; font-size: 30px;")

class Round_Button(QPushButton):
    def __init__(self, text: str, oyna: QWidget):
        super().__init__(oyna)
        self.setText(text)
        self.setFixedSize(50,50)
        self.setStyleSheet("""
QPushButton {
border-radius: 25px;
background-color: white;
color: black;
font-size: 50px;                           
}
QPushButton: hover{
background-color: white;
}
""")

class Label(QLabel):
    def __init__(self, text: str, oyna: QWidget):
        super().__init__(oyna)
        self.setText(text)
        self.resize(300,50)
        self.setStyleSheet("color: black; font-size: 30px;")
        self.adjustSize()

class Text(QLineEdit):
    def __init__(self, text: str, oyna: QWidget):
        super().__init__(oyna)
        self.setPlaceholderText(text)
        self.resize(400,50)
        self.setStyleSheet("background-color: white; color: black; font-size: 30px;")

class LogIn(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(500,600)
        self.setStyleSheet("background-color: lightblue;")
        self.setWindowTitle("Log in")
        self.db = Database()
        self.loginLabel = Label("Tizim ga kirish", self)
        self.loginLabel.move(150,120)
        self.usernameInput = Text("Enter username:", self)
        self.usernameInput.move(50,200)
        self.passwordInput = Text("Enter password:", self)
        self.passwordInput.move(50,280)
        self.backBtn = Round_Button("⇦", self)
        self.backBtn.move(10,10)
        self.backBtn.clicked.connect(self.return_page)
        self.submitBtn = Button2("Yuklash", self)
        self.submitBtn.move(100,350)
        self.submitBtn.clicked.connect(self.submit)
    def return_page(self):
        self.reject()
    def submit(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        msg_box = QMessageBox()
        msg_box.setStyleSheet("""
QMessageBox{
background-color: white;
color: white;                            
}
QLabel{
background-color: white;
color: black;        
}

""")
        if username and password:
            user = self.db.check_user(username, password)
            if user:
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Success")
                msg_box.setText("Logged in successfully!")
                msg_box.exec_()
                self.accept()
            else:
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle("Error")
                msg_box.setText("Incorrect username or password!")
                msg_box.exec_()
        else: 
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please fill in all fields!")
            msg_box.exec_()


class SignUp(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(500,600)
        self.setStyleSheet("background-color: lightblue;")
        self.setWindowTitle("Sign Up")
        self.db = Database()
        self.signupLabel = Label("Ro'yxatdan o'tish", self)
        self.signupLabel.move(140,10)
        self.backBtn = Round_Button("⇦", self)
        self.backBtn.move(10,10)
        self.backBtn.clicked.connect(self.return_page)
        self.nameInput = Text("Enter name:", self)
        self.nameInput.move(50,80)
        self.surnameInput = Text("Enter surname:", self)
        self.surnameInput.move(50,160)
        self.ageInput = Text("Enter age:", self)
        self.ageInput.move(50,240)
        int_validator = QIntValidator(0,99,self)
        self.ageInput.setValidator(int_validator)
        self.usernameInput = Text("Enter username:", self)
        self.usernameInput.move(50,320)
        self.passwordInput = Text("Enter password:", self)
        self.passwordInput.move(50,400)
        self.submitBtn = Button1("Yuklash", self)
        self.submitBtn.move(100,480)
        self.submitBtn.clicked.connect(self.submit)

    def return_page(self):
        self.reject()
    def submit(self):
        name = self.nameInput.text()
        surname = self.surnameInput.text()
        age = self.ageInput.text()
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        msg_box = QMessageBox()
        msg_box.setStyleSheet("""
QMessageBox{
background-color: white;
color: white;                            
}
QLabel{
background-color: white;
color: black;        
}

""")
        if name and surname and age and username and password:
            user = self.db.insert_user(name, surname, age, username, password)
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Success")
            msg_box.setText("Signed up successfully!")
            msg_box.exec_()
            self.accept()
        else: 
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please fill in all fields!")
            msg_box.exec_()

class SecondWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(1400,800)



