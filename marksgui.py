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

def view_course_marks(screen):
    layout = QVBoxLayout()
    
    table = QTableWidget()

    table.setRowCount(5)
    table.setColumnCount(3)

    table.setItem(0,0, QTableWidgetItem("Assignment Name"))
    table.setItem(0,1, QTableWidgetItem("Mark (%)"))
    table.setItem(0,2, QTableWidgetItem("Worth (%)"))

    table.verticalHeader().setVisible(False)
    table.horizontalHeader().setVisible(False)
    
    table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    
    course_name = QComboBox(screen.view_course_marks)
    course_name.addItem("CSC263")
    course_name.addItem("CSC343")
    course_name.setStyleSheet("QComboBox {font: 18;}")
    
    topword = QLabel("View Marks for a Course", screen.view_course_marks)
    topword.setStyleSheet("QLabel {font: 12pt bold;}")

    backButton = QPushButton("Back", screen.view_course_marks)
    backButton.setStyleSheet("QLineEdit {font: 8pt;}")
    backButton.clicked.connect(screen.back_click)


    layout.addWidget(topword)
    layout.addWidget(course_name)
    layout.addWidget(table)
    layout.addWidget(backButton)

    screen.view_course_marks.setLayout(layout)

    

    
def addMarkGUI(screen):
    layout = QFormLayout()
   
    topword = QLabel("Enter a Mark", screen.enter_marks)
    topword.setStyleSheet("QLabel {font: 12pt bold;}")

    course_name = QComboBox(screen.enter_marks)
    course_name.addItem("CSC263")
    course_name.addItem("CSC343")
    course_name.setStyleSheet("QComboBox {font: 18;}")

    #drop down
    assign_name = QLineEdit(screen.enter_marks)
    assign_name.setStyleSheet("QLineEdit {font: 12pt bold;}")
    
    num = QLineEdit(screen.enter_marks)
    num.setStyleSheet("QLineEdit {font: 12pt bold;}")
    
    denom= QLineEdit(screen.enter_marks)
    denom.setStyleSheet("QLineEdit {font: 12pt bold;}")
    
    worth = QLineEdit(screen.enter_marks)
    worth.setStyleSheet("QLineEdit {font: 12pt bold;}")

    submitButton = QPushButton("Enter", screen.enter_marks)
    submitButton.setStyleSheet("QPushButton {font: 12pt bold;}")

    backButton = QPushButton("Back", screen.enter_marks)
    backButton.setStyleSheet("QLineEdit {font: 8pt;}")
    backButton.clicked.connect(screen.back_click)

    layout.addWidget(topword)
    layout.addWidget(course_name)
    layout.addRow("Course Code", course_name)
    layout.addRow("Assignment Name:", assign_name)
    layout.addRow("What you got:", num)
    layout.addRow("What it was out of:", denom)
    layout.addRow("How much it was worth:", worth)
    layout.addWidget(submitButton)
    layout.addWidget(backButton)
#After entered, clear textboxes
    #screen.enter_marks.move(40, 70)
    screen.enter_marks.setLayout(layout)
    
def edit_marks(screen):
    layout = QFormLayout()
    topword = QLabel("Edit Marks", screen.edit_marks)
    topword.setStyleSheet("QLabel {font: 12pt bold;}")

    course_name = QComboBox(screen.edit_marks)
    course_name.addItem("CSC263")
    course_name.addItem("CSC343")
    course_name.setStyleSheet("QComboBox {font: 18;}")

    assign_name = QComboBox(screen.edit_marks)
    assign_name.addItem("A1")
    assign_name.addItem("A2")

    num = QLineEdit(screen.enter_marks)
    num.setStyleSheet("QLineEdit {font: 12pt bold;}")
    
    denom= QLineEdit(screen.enter_marks)
    denom.setStyleSheet("QLineEdit {font: 12pt bold;}")
    
    worth = QLineEdit(screen.enter_marks)
    worth.setStyleSheet("QLineEdit {font: 12pt bold;}")

    submitButton = QPushButton("Enter", screen.enter_marks)
    submitButton.setStyleSheet("QPushButton {font: 12pt bold;}")

    backButton = QPushButton("Back", screen.enter_marks)
    backButton.setStyleSheet("QLineEdit {font: 8pt;}")
    backButton.clicked.connect(screen.back_click)

    layout.addWidget(topword)
    layout.addRow("Course Code", course_name)
    layout.addRow("Assignment Name", assign_name)
    layout.addRow("Revised what you got", num)
    layout.addRow("Revised what it was out of", denom)
    layout.addRow("Revised worth", worth)
    layout.addWidget(submitButton)
    layout.addWidget(backButton)

    layout.setSpacing(20)

    screen.edit_marks.move(40, 70)
    screen.edit_marks.setLayout(layout)
    
def hideEnter(screen):
    screen.passwordbox.deleteLater()
    screen.button.deleteLater()
    screen.message.deleteLater()
    screen.error.deleteLater()   

def add_course(screen):
    layout = QVBoxLayout()

    top = QLabel("Add a Course", screen.add_course)
    top.setStyleSheet("QLabel {font: 12pt; }")

    name_label = QLabel("Course Code", screen.add_course)
    name_label.setStyleSheet("QLabel {font: 12pt; }")

    course_name = QLineEdit(screen.add_course)
    course_name.setStyleSheet("QLineEdit {font: 12pt bold;}")

    submitButton = QPushButton("Add", screen.add_course)
    submitButton.setStyleSheet("QPushButton {font: 18pt bold;}")

    backButton = QPushButton("Back", screen.add_course)
    backButton.setStyleSheet("QLineEdit {font: 8pt;}")
    backButton.clicked.connect(screen.back_click)

    layout.addWidget(top)
    layout.addWidget(name_label)
    layout.addWidget(course_name)
    layout.addWidget(submitButton)
    layout.addWidget(backButton)
    layout.setAlignment(Qt.AlignTop)

    layout.setSpacing(20)
    screen.add_course.setLayout(layout)

def delete_course(screen):
    layout = QVBoxLayout()

    top = QLabel("Delete a Course", screen.delete_course)
    top.setStyleSheet("QLabel {font: 12pt; }")

    name_label = QLabel("Course Code", screen.delete_course)
    name_label.setStyleSheet("QLabel {font: 12pt; }")

    course_name = QComboBox(screen.delete_course)
    course_name.setStyleSheet("QComboBox {font: 12pt bold;}")

    submitButton = QPushButton("Delete", screen.delete_course)
    submitButton.setStyleSheet("QPushButton {font: 18pt bold;}")

    backButton = QPushButton("Back", screen.delete_course)
    backButton.setStyleSheet("QPushButton {font: 8pt;}")
    backButton.clicked.connect(screen.back_click)

    layout.addWidget(top)
    layout.addWidget(name_label)
    layout.addWidget(course_name)
    layout.addWidget(submitButton)
    layout.addWidget(backButton)

    layout.setAlignment(Qt.AlignTop)
    layout.setSpacing(20)
    screen.delete_course.setLayout(layout)

    
def makeMain(window):
    label = QLabel("Main Menu", window)
    label.setStyleSheet("QLabel {font: 12pt; }")
    
    layout = QVBoxLayout()
    
    viewButton = QPushButton("View Summary of all Marks", window.main_menu)
    viewButton.setStyleSheet("QPushButton {font: 12pt bold;}")
    viewButton.clicked.connect(window.view_all_click)

    course_marks = QPushButton("View Marks for a Course", window.main_menu)
    course_marks.setStyleSheet("QPushButton {font: 12pt bold;}")
    course_marks.clicked.connect(window.view_course_click)
 
    enterMarkButton = QPushButton("Enter a Mark", window.main_menu)
    enterMarkButton.setStyleSheet("QPushButton {font: 12pt bold;}")
    enterMarkButton.clicked.connect(window.enter_marks_click)

    editMarkButton = QPushButton("Edit Course Mark", window.main_menu)
    editMarkButton.setStyleSheet("QPushButton {font: 12pt bold;}")
    editMarkButton.clicked.connect(window.edit_click)

    addCourseButton = QPushButton("Add a Course", window.main_menu)
    addCourseButton.setStyleSheet("QPushButton {font: 12pt bold;}")
    addCourseButton.clicked.connect(window.add_course_click)

    deleteCourseButton = QPushButton("Delete a Course", window.main_menu)
    deleteCourseButton.setStyleSheet("QPushButton {font: 12pt bold;}")
    deleteCourseButton.clicked.connect(window.delete_course_click)

    layout.addWidget(label)
    layout.addWidget(viewButton)
    #layout.addSpacerItem(space) http://www.qtcentre.org/threads/27968-QSpacerItem-constructor-arguments
    layout.addWidget(course_marks)
    layout.addWidget(enterMarkButton)
    layout.addWidget(editMarkButton)
    layout.addWidget(addCourseButton)
    layout.addWidget(deleteCourseButton)

    layout.setSpacing(30)
    #window.main_menu.move(90, 50)
    window.main_menu.setLayout(layout)   
    #window.show()
    #screen.stack.setCurrentIndex(0)

"""
def hideMainButton(screen):
    screen.editMarkButton.hide()
    screen.enterMarkButton.hide()
    screen.viewButton.hide()
    screen.passwordmsg.hide()
"""
class App(QWidget):

    def __init__(self):
        self.first_time = False
        if not os.path.isfile((os.getcwd() + "\marks.txt")):
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
        self.view_course_marks = QWidget()
        self.enter_marks = QWidget()
        self.edit_marks = QWidget()
        self.add_course = QWidget()
        self.delete_course = QWidget()

        makeMain(self)
        view_all_summary(self)
        view_course_marks(self)
        addMarkGUI(self)
        edit_marks(self)
        add_course(self)
        delete_course(self)
        
        
        self.stack.addWidget(self.main_menu)
        self.stack.addWidget(self.view_all_summary)
        self.stack.addWidget(self.view_course_marks)
        self.stack.addWidget(self.enter_marks)
        self.stack.addWidget(self.edit_marks)
        self.stack.addWidget(self.add_course)
        self.stack.addWidget(self.delete_course)

        
        self.show()

    
    def on_click(self):
        if (self.passwordbox.text() == "3331"):
            self.actionExit.setEnabled(False)
            hideEnter(self)
            self.stack.setCurrentWidget(self.main_menu)
            
        else:        
            self.error.show()
            self.passwordbox.setText("")
            

    
    def view_all_click(self):
        self.stack.setCurrentIndex(1)

    def view_course_click(self):
        self.stack.setCurrentWidget(self.view_course_marks)

    def enter_marks_click(self):
        self.stack.setCurrentWidget(self.enter_marks)
        
    def edit_click(self):
        self.stack.setCurrentWidget(self.edit_marks)
        
    def add_course_click(self):
        self.stack.setCurrentWidget(self.add_course)

    def delete_course_click(self):
        self.stack.setCurrentWidget(self.delete_course)
       
    def back_click(self):
        self.stack.setCurrentIndex(0)
        
if __name__ == '__main__':
    app  = QApplication(sys.argv)
    ex = App()
    #sys.exit(0)
