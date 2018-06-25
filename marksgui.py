import sys, os
from addmarks import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
QLineEdit, QLabel, QAction, QComboBox, QVBoxLayout, QSpacerItem, \
QStackedWidget, QFormLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot, Qt, QTimer
#from PyQt5.QtCore import Qt
#from PyQt5.QtCore import QTimer
from crypto import *
def view_all_summary(screen):

    title = QLabel("Summary", screen.view_all_summary)
    title.setStyleSheet("QLabel {font: 12pt bold;}")
    
    font = QFont()
    font.setPointSize(12)
    font.setBold(True)
    layout = QVBoxLayout()
    table = QTableWidget()
    screen.update_widgets["view_all_table"] = table
    table.setRowCount(len(screen.all_marks)+1)
    table.setColumnCount(3)
    table.verticalHeader().setVisible(False)
    table.horizontalHeader().setVisible(False)

    course_code = QTableWidgetItem("Course Code")
    course_code.setBackground(QColor(255,128,128))

    mark = QTableWidgetItem("Mark (%)")
    mark.setBackground(QColor(255,128,128))

    completed = QTableWidgetItem("% Completed")
    completed.setBackground(QColor(255,128,128))

    table.setItem(0,0, course_code)
    table.setItem(0,1, mark)
    table.setItem(0,2, completed)
    table.setRowHeight(0, 50)
    table.setMinimumWidth(450)
    table.setMinimumHeight(400) #Will need to set max height as well

    index = 1
    
    for course in screen.all_marks:

        if screen.all_marks == []:
            table.setItem(index, 0, QTableWidgetItem(course))
            table.setItem(index, 1, QTableWidgetItem("0"))
            table.setItem(index, 2, QTableWidgetItem("0"))
            break
        
        else:
            average, worth = average_and_worth(screen.all_marks[course])
            print(average, worth)
            table.setItem(index, 0, QTableWidgetItem(course))
            table.setItem(index, 1, QTableWidgetItem(str(round(average,5))))
            table.setItem(index, 2, QTableWidgetItem(str(round(worth,5))))
            index += 1
        
    
    button = QPushButton("Back")
    button.clicked.connect(screen.back_click)

    #w = verticalHeader()->width() + horizontalHeader()->length() + frameWidth()*2
#h = horizontalHeader()->height() + verticalHeader()->length() + frameWidth()*2
    
    table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    layout.addWidget(title)
    layout.setAlignment(title, Qt.AlignCenter)
    
    layout.addWidget(table)
    layout.addWidget(button)
    

    #layout.addWidget(QLabel("Course"), 0, 0)
    #layout.addWidget(QLabel("Mark"), 0, 1)
    #layout.addWidget(QLabel("Percent of Course Completed"), 0, 2)
    
    #layout.addWidget(QLabel("CSC256"), 1, 0)
    #layout.addWidget(QLabel("CSC%^%").setStyleSheet("QLabel {font: 15pt;}"), 1, 1)

    screen.view_all_summary.setLayout(layout)
    #screen.show()

"""
def update_widgets(screen):
    #screen.enter_marks.update()
    
    if command == "delete course":
        pass
    if command == "add course":
        pass

    if command == "edit
    
    print("here")
    #view_all_summary(screen)
    print("1")
    view_course_marks(screen)
    print("nn")
    addMarkGUI(screen)
    print("2")
    edit_marks(screen)
    add_course(screen)
    delete_course(screen)
    
    # call the functiona to build the widgets
"""
def average_and_worth(course):
    total_average = 0
    worth = 0
    for data in course:
        total_average += (data[1] / data[2]) * data[3]
        worth += data[3]

    return (total_average / worth) * 100, worth

def update_summary(table, screen, delete=None):
    table.setRowCount(len(screen.all_marks)+1)
    table.clear()

    course_code = QTableWidgetItem("Course Code")
    course_code.setBackground(QColor(255,128,128))

    mark = QTableWidgetItem("Mark (%)")
    mark.setBackground(QColor(255,128,128))

    completed = QTableWidgetItem("% Worth")
    completed.setBackground(QColor(255,128,128))

    table.setItem(0,0, course_code)
    table.setItem(0,1, mark)
    table.setItem(0,2, completed)
    print("in update summary")
    index = 1
    
    for course in screen.all_marks:
        if delete and course == delete:
            pass
        
        elif screen.all_marks[course] == []:
            table.setItem(index, 0, QTableWidgetItem(course))
            table.setItem(index, 1, QTableWidgetItem("0"))
            table.setItem(index, 2, QTableWidgetItem("0"))
            index += 1
            print("lll")
        
        else:
            average, worth = average_and_worth(screen.all_marks[course])
            print(average, worth)
            table.setItem(index, 0, QTableWidgetItem(course))
            table.setItem(index, 1, QTableWidgetItem(str(round(average,5))))
            table.setItem(index, 2, QTableWidgetItem(str(round(worth,5))))
            index += 1
    
    
def view_course_marks(screen):
    layout = QVBoxLayout()
    
    table = QTableWidget()
    screen.update_widgets["course_marks_table"] = table

    table.setRowCount(len(screen.all_marks) + 1)
    table.setColumnCount(3)

    course_code = QTableWidgetItem("Assignment Name")
    course_code.setBackground(QColor(255,128,128))

    mark = QTableWidgetItem("Mark (%)")
    mark.setBackground(QColor(255,128,128))

    completed = QTableWidgetItem("Worth (%)")
    completed.setBackground(QColor(255,128,128))
    
    table.setItem(0,0, course_code)
    table.setItem(0,1, mark)
    table.setItem(0,2, completed)

    table.verticalHeader().setVisible(False)
    table.horizontalHeader().setVisible(False)
    
    table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    
    course_name = QComboBox(screen.view_course_marks)
    screen.update_widgets["course_marks_combo"] = course_name
    

    for i in screen.all_marks:
        course_name.addItem(i)
        course_name.setStyleSheet("QComboBox {font: 18;}")
    #for course in screen.all_marks:
     #   course_name.addItem(course)

    
    # get course code and then add assignments
    index = 0
    for data in screen.all_marks[course_name.currentText()]:
        index += 1
        table.setItem(index, 0, QTableWidgetItem(data[0]))
        table.setItem(index, 1, QTableWidgetItem(str(data[1]/data[2] * 100)))
        table.setItem(index, 2, QTableWidgetItem(str(data[3])))
    
        
    course_name.currentIndexChanged.connect(lambda: screen.course_combo_changed(table, course_name))
    
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
    screen.update_widgets["enter_mark_combo"] = course_name
    
    for i in screen.all_marks:
        course_name.addItem(i)
        course_name.setStyleSheet("QComboBox {font: 12pt;}")

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

    msg = QLabel("Mark Added!", screen.add_course)
    msg.setStyleSheet("QLabel {font: 12pt;}")
    msg.hide()

    submitButton.clicked.connect(lambda: screen.enter_submit_click(course_name, assign_name, num, denom, worth, msg))

    layout.addWidget(topword)
    layout.addWidget(course_name)
    layout.addRow("Course Code:", course_name)
    layout.addRow("Assignment Name:", assign_name)
    layout.addRow("What you got:", num)
    layout.addRow("What it was out of:", denom)
    layout.addRow("How much it was worth:", worth)
    layout.addWidget(submitButton)
    layout.addWidget(backButton)
    layout.addWidget(msg)
#After entered, clear textboxes
    screen.enter_marks.setLayout(layout)
    
def edit_marks(screen):
    layout = QFormLayout()
    topword = QLabel("Edit Marks", screen.edit_marks)
    topword.setStyleSheet("QLabel {font: 12pt bold;}")

    course_name = QComboBox(screen.edit_marks)
    screen.update_widgets["edit_course_combo"] = course_name
    
    for course in screen.all_marks:
        course_name.addItem(course)
        course_name.setStyleSheet("QComboBox {font: 12pt;}")

    assign_name = QComboBox(screen.edit_marks)
    screen.update_widgets["edit_assignment_combo"] = assign_name

    for assignments in screen.all_marks[course_name.itemText(0)]:
        assign_name.addItem(assignments[0])
        assign_name.setStyleSheet("QComboBox {font: 12pt;}")

        
    course_name.currentIndexChanged.connect(lambda: screen.edit_marks_change(assign_name, course_name.currentText()))

    num = QLineEdit(screen.edit_marks)
    num.setStyleSheet("QLineEdit {font: 12pt bold;}")
    
    denom= QLineEdit(screen.edit_marks)
    denom.setStyleSheet("QLineEdit {font: 12pt bold;}")
    
    worth = QLineEdit(screen.edit_marks)
    worth.setStyleSheet("QLineEdit {font: 12pt bold;}")

    submitButton = QPushButton("Enter", screen.edit_marks)
    submitButton.setStyleSheet("QPushButton {font: 12pt bold;}")

    msg = QLabel("Mark Edited!", screen.edit_marks)
    msg.setStyleSheet("QLabel {font: 12pt;}")
    msg.hide()
    
    submitButton.clicked.connect(lambda: screen.edit_mark_click(course_name, assign_name, num, denom, worth, msg))

    backButton = QPushButton("Back", screen.enter_marks)
    backButton.setStyleSheet("QLineEdit {font: 8pt;}")
    backButton.clicked.connect(screen.back_click)
    
    layout.addRow("Course Code", course_name)
    layout.addRow("Assignment Name", assign_name)
    layout.addRow("Revised what you got", num)
    layout.addRow("Revised what it was out of", denom)
    layout.addRow("Revised worth", worth)
    layout.addWidget(submitButton)
    layout.addWidget(backButton)
    layout.addWidget(msg)

    layout.setSpacing(20)

    screen.edit_marks.move(40, 70)
    screen.edit_marks.setLayout(layout)
    
def hideEnter(screen):
    screen.logo.deleteLater()
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

    msg = QLabel("Mark Added!", screen.add_course)
    msg.setStyleSheet("QLabel {font: 8pt;}")
    msg.hide()

    layout.addWidget(top)
    layout.setAlignment(top, Qt.AlignCenter)
    layout.addWidget(name_label)
    layout.addWidget(course_name)
    layout.addWidget(submitButton)
    layout.addWidget(backButton)
    layout.addWidget(msg)
    layout.setAlignment(Qt.AlignTop)

    layout.setSpacing(20)
    submitButton.clicked.connect(lambda: screen.add_a_course_click(course_name, msg))
    screen.add_course.setLayout(layout)

def delete_course(screen):
    layout = QVBoxLayout()

    top = QLabel("Delete a Course", screen.delete_course)
    top.setStyleSheet("QLabel {font: 12pt; }")

    name_label = QLabel("Course Code", screen.delete_course)
    name_label.setStyleSheet("QLabel {font: 12pt; }")

    course_name = QComboBox(screen.delete_course)
    screen.update_widgets["delete_course_combo"] = course_name
    course_name.setStyleSheet("QComboBox {font: 12pt bold;}")

    for course in screen.all_marks:
        course_name.addItem(course)


    submitButton = QPushButton("Delete", screen.delete_course)
    submitButton.setStyleSheet("QPushButton {font: 18pt bold;}")

    backButton = QPushButton("Back", screen.delete_course)
    backButton.setStyleSheet("QPushButton {font: 8pt;}")
    backButton.clicked.connect(screen.back_click)

    msg = QLabel("Course Deleted!", screen.delete_course)
    msg.setStyleSheet("QLabel {font: 12pt;}")
    msg.hide()

    submitButton.clicked.connect(lambda: screen.delete_a_course_click(course_name, msg))

    layout.addWidget(top)
    layout.setAlignment(top, Qt.AlignCenter)
    layout.addWidget(name_label)
    layout.addWidget(course_name)
    layout.addWidget(submitButton)
    layout.addWidget(backButton)
    layout.addWidget(msg)

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

    exitButton = QPushButton("Save and Exit", window.main_menu)
    exitButton.setStyleSheet("QPushButton {font: 12pt bold;}")
    exitButton.clicked.connect(window.exit)

    layout.addWidget(label)
    layout.addWidget(viewButton)
    layout.addWidget(course_marks)
    layout.addWidget(enterMarkButton)
    layout.addWidget(editMarkButton)
    layout.addWidget(addCourseButton)
    layout.addWidget(deleteCourseButton)
    layout.addWidget(exitButton)

    layout.setSpacing(25)
    window.main_menu.setLayout(layout)   

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
        self.all_marks = {"csc456":[["a1",45,45,67], ["a2", 34,67,2]], "csc234":[["prog",56,67,12]]}
        self.update_widgets = {}
        
        if not self.first_time:
            file = open("marks.txt")
            self.password = file.readline().strip()
                   
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

        self.logo = QLabel("Marks Keeper", self)
        self.logo.setStyleSheet("QLabel {font: 18pt;}")
        
        self.passwordmsg = "Enter password" if not self.first_time else "Enter a Password"
        self.message = QLabel(self.passwordmsg, self)
        self.message.setStyleSheet("QLabel {font: 12pt;}")
        
        self.passwordbox = QLineEdit(self)
        self.passwordbox.hasSelectedText
        self.passwordbox.setStyleSheet("QLineEdit {font: 18;}")

        if not self.first_time:
            self.passwordbox.setEchoMode(QLineEdit.Password)
        
        self.button = QPushButton("Submit", self)
        self.button.setAutoFillBackground(Qt.white)     
        self.button.setStyleSheet("QPushButton {font: 12pt bold;}")
        self.button.setToolTip("Enter password and then click this button or press the ENTER key")

        self.button.clicked.connect(self.on_click)
        
        self.error = QLabel("Incorrect Password", self)
        self.error.setStyleSheet("QLabel {font: 12pt; color:red; }")
        self.error.hide()

        self.stack = QStackedWidget(self)

        vbox.addWidget(self.logo)
        vbox.addWidget(self.message)
        vbox.addWidget(self.passwordbox)
        vbox.addWidget(self.button)
        vbox.addWidget(self.error)
        vbox.addWidget(self.stack)

        vbox.setSpacing(40)

        vbox.addWidget(self.stack)
        vbox.setAlignment(self.message,Qt.AlignCenter)
        vbox.setAlignment(self.logo, Qt.AlignCenter)
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
        if not self.first_time:
            try:
                if self.passwordbox.text() == decode(self.passwordbox.text(), self.password):
                    self.actionExit.setEnabled(False)
                    hideEnter(self)
                    self.actual_password = self.passwordbox.text()
                    self.stack.setCurrentWidget(self.main_menu)
                    
                else:        
                    self.error.show()
                    self.passwordbox.setText("")
            except:
                self.error.show()
                self.passwordbox.setText("")

        else:
            self.actionExit.setEnabled(False)
            hideEnter(self)
            self.actual_password = self.passwordbox.text()
            self.stack.setCurrentWidget(self.main_menu)
            
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

    def enter_submit_click(self, course, name, num, denom, worth, msg):
        course_s = course.currentText()
        name_s = name.text()
        num_s = num.text()
        denom_s = denom.text()
        worth_s = worth.text()
        
        name.setText("")
        num.setText("")
        denom.setText("")
        worth.setText("")

        to_display = add_mark(course_s, name_s, num_s, denom_s, worth_s, self.all_marks[course_s])
        
        if to_display == "Success":
            msg.setText(to_display)
            msg.setStyleSheet("QLabel {font: 12pt; color:green;}")
            msg.show()
            self.all_marks[course_s].insert(0,[name_s,int(num_s), int(denom_s), int(worth_s)])
            update_summary(self.update_widgets["view_all_table"], self)
            self.course_combo_changed(self.update_widgets["course_marks_table"], course)
            print(self.update_widgets)
            self.update_widgets["course_marks_combo"].setCurrentIndex(self.update_widgets["course_marks_combo"].findText(course_s))
            QTimer.singleShot(2000, msg.hide)

        else:
            msg.setText(to_display)
            msg.setStyleSheet("QLabel {font: 8pt; color:red;}")
            msg.show()
            QTimer.singleShot(2000, msg.hide)


    def exit(self):
        file = open("marks.txt", "w")
        write_password = str(encode(self.actual_password, self.actual_password)) + "\n"
        to_write = encode(self.actual_password, str(self.all_marks))
        file.write(write_password)
        file.write(to_write)
        file.close()        
        sys.exit(0)

    def add_a_course_click(self, course, msg):
        course_s = course.text()
        course.setText("")
        if course_s not in self.all_marks:
            self.all_marks[course_s] = []
            print(self.all_marks)
            msg.hide()
            msg.setText("Course Added!")
            msg.setStyleSheet("QLabel {font: 12pt; color: green;}")
            msg.show()

            self.update_widgets["course_marks_combo"].addItem(course_s)
            self.update_widgets["edit_course_combo"].addItem(course_s)
            self.update_widgets["delete_course_combo"].addItem(course_s)
            self.update_widgets["enter_mark_combo"].addItem(course_s)

            update_summary(self.update_widgets["view_all_table"], self)
            self.edit_marks_change(self.update_widgets["course_marks_combo"], course_s)
            
            QTimer.singleShot(2000, msg.hide)

        else:
            msg.setText("Course not Added")
            msg.setStyleSheet("QLabel {font: 12pt; color: red;}")
            msg.show()
            QTimer.singleShot(2000, msg.hide)
            

    def delete_a_course_click(self, course, msg):
        course_s = course.currentText()
        
        try:
            del self.all_marks[course_s]
            msg.setText("Course Deleted")
            msg.setStyleSheet("QLabel {font: 12pt; color: green;}")
            msg.show()
            self.stack.update()
            self.update_widgets["course_marks_combo"].removeItem(self.update_widgets["course_marks_combo"].findText(course_s, Qt.MatchFixedString))
            self.update_widgets["edit_course_combo"].removeItem(self.update_widgets["edit_course_combo"].findText(course_s, Qt.MatchFixedString))
            self.update_widgets["enter_mark_combo"].removeItem(self.update_widgets["enter_mark_combo"].findText(course_s, Qt.MatchFixedString))

            update_summary(self.update_widgets["view_all_table"], self, course_s)
            course.removeItem(course.currentIndex())
            QTimer.singleShot(2000, msg.hide)
            
        except:
            msg.setText("Course Not Deleted")
            msg.setStyleSheet("QLabel {font: 12pt; color: red;}")
            msg.show()
            QTimer.singleShot(2000, msg.hide)

    def edit_mark_click(self, course, name, num, denom, worth, msg):
        course_s = course.currentText()
        name_s = name.currentText()
        num_s = num.text()
        denom_s = denom.text()
        worth_s = worth.text()

        num.setText("")
        denom.setText("")
        worth.setText("")
        print("before display")
        to_display = edit_marks_func(course_s, name_s, num_s, denom_s, worth_s)
        print("after display")
        msg.setText(to_display)
        print("after real display")
        for assign in self.all_marks[course_s]:
            print("assign", assign, "course_s is", course_s, "name is", name_s)
            if assign[0] == name_s:
                assign[1] = int(num_s)
                assign[2] = int(denom_s)
                assign[3] = int(worth_s)
                print("CHANGEDDDD", assign)
                break

        update_summary(self.update_widgets["view_all_table"], self)
        index = self.update_widgets["course_marks_combo"].findText(course_s, Qt.MatchFixedString)
        self.update_widgets["course_marks_combo"].setCurrentIndex(index)
        self.course_combo_changed(self.update_widgets["course_marks_table"], self.update_widgets["course_marks_combo"])
        

    def edit_marks_change(self, combo, course):
        combo.clear()
        
        for assign in self.all_marks[course]:
            print(assign)
            combo.addItem(assign[0])
        
    def course_combo_changed(self, table, combo): #get the table and the new course code
        print(table, combo)
        course = combo.currentText()
        index = 1
        table.clear()
        print("here in changed")
        table.setRowCount(len(self.all_marks[course])+1)
        course_code = QTableWidgetItem("Course Code")
        course_code.setBackground(QColor(255,128,128))

        mark = QTableWidgetItem("Mark (%)")
        mark.setBackground(QColor(255,128,128))

        completed = QTableWidgetItem("% Worth")
        completed.setBackground(QColor(255,128,128))

        table.setItem(0,0, course_code)
        table.setItem(0,1, mark)
        table.setItem(0,2, completed)
        
        for assignment in self.all_marks[course]:
            print(assignment)
            mark = round(assignment[1] / assignment[2] *100, 5)
            print("after mark")
            
            table.setItem(index, 0, QTableWidgetItem(assignment[0]))
            table.setItem(index, 1, QTableWidgetItem(str(mark)))
            table.setItem(index, 2, QTableWidgetItem(str(assignment[3])))
            index += 1
                                   
        
        
if __name__ == '__main__':
    app  = QApplication(sys.argv)
    ex = App()
    #sys.exit(0)
