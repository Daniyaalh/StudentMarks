import sys, os
#import addmarks
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
QLineEdit, QLabel, QAction, QComboBox, QVBoxLayout, QSpacerItem, \
QStackedWidget, QFormLayout, QTableWidget, QTableWidgetItem
#from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt

def view_all_summary(screen):

    font = QFont()
    font.setPointSize(12)
    font.setBold(True)
    layout = QVBoxLayout()
    table = QTableWidget()
    table.setRowCount(5)
    table.setColumnCount(3)
    table.verticalHeader().setVisible(False)
    table.horizontalHeader().setVisible(False)

    table.setItem(0,0, QTableWidgetItem("Course Code"))
    table.setItem(0,1, QTableWidgetItem("Mark (%)"))
    table.setItem(0,2, QTableWidgetItem("% Completed").setFont(font))
    table.setRowHeight(0, 50)
    table.setMinimumWidth(450)
    table.setMinimumHeight(400) #Will need to set max height as well

    table.setItem(1,0, QTableWidgetItem("CSC456"))

    button = QPushButton("Back")
    button.clicked.connect(screen.back_click)

    #w = verticalHeader()->width() + horizontalHeader()->length() + frameWidth()*2
#h = horizontalHeader()->height() + verticalHeader()->length() + frameWidth()*2
    
    table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    layout.addWidget(table)
    layout.addWidget(button)
    

    #layout.addWidget(QLabel("Course"), 0, 0)
    #layout.addWidget(QLabel("Mark"), 0, 1)
    #layout.addWidget(QLabel("Percent of Course Completed"), 0, 2)
    
    #layout.addWidget(QLabel("CSC256"), 1, 0)
    #layout.addWidget(QLabel("CSC%^%").setStyleSheet("QLabel {font: 15pt;}"), 1, 1)

    screen.view_all_summary.setLayout(layout)
    #screen.show()

def addMarkGUI(screen):
    #screen.QLabel

    screen.course = QLineEdit(screen)
    screen.course.setStyleSheet("QLineEdit {font: 18;}")
# move it to right place

    screen.assignment_name = QLineEdit(screen)
    screen.assignment_name.setStyleSheet("QLineEdit {font: 12;}")
    screen.assignment_name.move(200, 100) #y axis the same
    screen.assignment_name.show()

    screen.styleChoice = QLabel("Windows Vista", screen)
    screen.styleChoice.move(50, 150)

    
    screen.select_course = QComboBox(screen)
    screen.select_course.addItem("CSC263")
    screen.select_course.addItem("MAT223")
    screen.select_course.move(500, 500)

    screen.select_course.show()
    #screen.select_course.activated[str].connect(screen.styleChoice)

    
    screen.mark = QLineEdit(screen)
    screen.mark.setStyleSheet("QLineEdit {font: 12;}")
    screen.mark.move(150, 100)
    screen.mark.show()

    screen.outof = QLineEdit(screen)
    screen.outof.setStyleSheet("QLineEdit {font: 12;}")
    screen.outof.move(150, 150)
    screen.outof.show()

    screen.worth = QLineEdit(screen)
    screen.worth.setStyleSheet("QLineEdit {font: 12;} ")
    screen.worth.move(150, 200)
    screen.worth.show()

def hideEnter(screen):
    screen.passwordbox.deleteLater()
    screen.button.deleteLater()
    screen.message.deleteLater()
    screen.error.deleteLater()   

def makeMain(window): #enter marks, edit marks
    label = QLabel("Main Menu", window)
    label.setStyleSheet("QLabel {font: 12pt; }")
    
   # window = QWidget(screen)
    layout = QVBoxLayout()
    
    viewButton = QPushButton("View Summary of all Marks", window.main_menu)
    viewButton.setStyleSheet("QPushButton {font: 12pt bold;}")
    viewButton.clicked.connect(window.view_all_click)

    course_marks = QPushButton("View Marks for a Course", window.main_menu)
    course_marks.setStyleSheet("QPushButton {font: 12pt bold;}")
    #course_marks.clicked.connect(screen.view_click)
 
    enterMarkButton = QPushButton("Enter a Mark", window.main_menu)
    enterMarkButton.setStyleSheet("QPushButton {font: 12pt bold;}")
    #enterMarkButton.clicked.connect(screen.enter_click)

    editMarkButton = QPushButton("Edit Course Mark", window.main_menu)
    editMarkButton.setStyleSheet("QPushButton {font: 12pt bold;}")
    #editMarkButton.clicked.connect(screen.edit_click)

    addCourseButton = QPushButton("Add a Course", window.main_menu)
    addCourseButton.setStyleSheet("QPushButton {font: 12pt bold;}")
    # connect

    deleteCourseButton = QPushButton("Delete a Course", window.main_menu)
    deleteCourseButton.setStyleSheet("QPushButton {font: 12pt bold;}")
    #connect

    layout.addWidget(label)
    layout.addWidget(viewButton)
    #layout.addSpacerItem(space) http://www.qtcentre.org/threads/27968-QSpacerItem-constructor-arguments
    layout.addWidget(course_marks)
    layout.addWidget(enterMarkButton)
    layout.addWidget(editMarkButton)
    layout.addWidget(addCourseButton)
    layout.addWidget(deleteCourseButton)

    layout.setSpacing(30)
    #window.move(90, 50)
    window.main_menu.setLayout(layout)
    print("8")    
    #window.show()
    print("ki")
    #screen.stack.setCurrentIndex(0)
    print("ji")

"""
def hideMainButton(screen):
    screen.editMarkButton.hide()
    screen.enterMarkButton.hide()
    screen.viewButton.hide()
    screen.passwordmsg.hide()
"""
class App(QWidget):

    def __init__(self):
        if not os.path.isdir((os.getcwd() + "\marks.txt")):
            file = open("marks.txt", "w")
            file.close()
            self.first_time = True
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

        testWidget = QWidget()
        self.actionExit = QAction(("&Exit"), self)
        self.actionExit.setShortcut(QKeySequence(Qt.Key_Return)) #Ctrl+Q
        self.addAction(self.actionExit)
        self.actionExit.triggered.connect(self.on_click)
        
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        vbox = QVBoxLayout(self)
        
        self.passwordmsg = "Enter password" if not self.first_time else "Enter a Password"
        self.message = QLabel(self.passwordmsg, self)
        self.message.setStyleSheet("QLabel {font: 12pt;}")
        #self.message.move(170, 35)
        
        self.passwordbox = QLineEdit(self)
        self.passwordbox.hasSelectedText
        self.passwordbox.setStyleSheet("QLineEdit {font: 18;}")
        #self.passwordbox.move(125,100)

        if not self.first_time:
            self.passwordbox.setEchoMode(QLineEdit.Password)
        self.passwordbox.resize(250, 100)
        
        self.button = QPushButton("Submit", self)
        self.button.setAutoFillBackground(Qt.white)     
        self.button.setStyleSheet("QPushButton {font: 12pt bold;}")
        self.button.setToolTip("Enter password and then click this button or press the ENTER key")
        #self.button.move(200, 300)
        self.button.clicked.connect(self.on_click)
        
        self.error = QLabel("Incorrect Password", self)
        self.error.setStyleSheet("QLabel {font: 12pt; color:red; }")
        self.error.hide()
        #self.error.move(160,250)

        self.stack = QStackedWidget(self)

        vbox.addWidget(self.message)
        vbox.addWidget(self.passwordbox)
        vbox.addWidget(self.button)
        vbox.addWidget(self.error)
        vbox.addWidget(self.stack)

        vbox.setSpacing(80)

        vbox.addWidget(self.stack)
        self.setLayout(vbox)

        self.main_menu = QWidget()
        self.view_all_summary = QWidget()
        self.enter_marks = QWidget()
        self.edit_marks = QWidget()
        self.add_course = QWidget()
        self.delete_marks = QWidget()

        makeMain(self)
        view_all_summary(self)
        
        
        self.stack.addWidget(self.main_menu)
        self.stack.addWidget(self.view_all_summary)
        self.stack.addWidget(self.enter_marks)
        self.stack.addWidget(self.edit_marks)
        self.stack.addWidget(self.add_course)
        self.stack.addWidget(self.delete_marks)

        
        self.show()

    
    def on_click(self):
        if (self.passwordbox.text() == "3331"):
            self.actionExit.setEnabled(False)
            hideEnter(self)
            self.stack.setCurrentWidget(self.main_menu)
            #Make a QWidget for each button section and do the same thing as above
        else:        
            self.error.show()
            self.passwordbox.setText("")
            

    
    def view_all_click(self):
        self.stack.setCurrentIndex(1)

    def view_course(self):
        self.stack.setCurrentIndex(2)

    def enter_marks_click(self):

        addMarkGUI(self)
        self.stack.setCurrentIndex(3)
        
    def edit_click(self):
        self.stack.setCurrentIndex(4)
        
    def add_course_click(self):
        self.stack.setCurrentIndex(5)

    def delete_course_click(self):
        self.stack.setCurrentIndex(6)
       
    def back_click(self):
        self.stack.setCurrentIndex(0)
        
if __name__ == '__main__':
    app  = QApplication(sys.argv)
    ex = App()
    #sys.exit(0)
