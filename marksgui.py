import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
QLineEdit, QLabel, QAction
#from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Marks Keeper"
        self.left = 500
        self.top = 500
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setMinimumSize(500, 500)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.actionExit = QAction(("&Exit"), self)
        self.actionExit.setShortcut(QKeySequence(Qt.Key_Return)) #Ctrl+Q
        self.addAction(self.actionExit)
        self.actionExit.triggered.connect(self.on_click)
        
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        self.message = QLabel("Enter password", self)
        self.message.setStyleSheet("QLabel {font: 12pt;}")
        self.message.move(170, 35)
        
        self.passwordbox = QLineEdit(self)
        self.passwordbox.hasSelectedText
        self.passwordbox.setStyleSheet("QLineEdit {font: 18;}")
        self.passwordbox.move(125,100)
        self.passwordbox.setEchoMode(QLineEdit.Password)
        self.passwordbox.resize(250, 100)
        
        self.button = QPushButton("Submit", self)
        self.button.setAutoFillBackground(Qt.white)
        #self.button.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        self.button.setStyleSheet("QPushButton {font: 12pt bold;}")
        self.button.setToolTip("Enter password and then click this button")
        self.button.move(200, 300)
        self.button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print(type(self.passwordbox.text))
        if (self.passwordbox.text == "3331"):
            print("password correct")
        else:
            print(self.passwordbox.text())
        #self.message.deleteLater()

if __name__ == '__main__':
    app  = QApplication(sys.argv)
    ex = App()
    #sys.exit(0)
