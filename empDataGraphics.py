from PyQt5 import QtCore, QtGui, QtWidgets
import Resources_rc

class Ui_MainWindow(object):
    
    def disableTooltips(self):
        self.closeSideBar_toolButton.setToolTip("")
        self.collapse_toolButton.setToolTip("")
        self.search_lineEdit.setToolTip("")
        self.searchField_comboBox.setToolTip("")
        self.search_toolButton.setToolTip("")
        self.newEmp_toolButton.setToolTip("")
        self.report_toolButton.setToolTip("")
        self.info_toolButton.setToolTip("")
        self.userManual_toolButton.setToolTip("")
        self.signOut_toolButton.setToolTip("")
        self.hamburger_toolButton.setToolTip("")
        self.signOutTopBar_toolButton.setToolTip("")
        return 0
    
    def enableTooltips(self):
        self.closeSideBar_toolButton.setToolTip("Close the side bar")
        self.collapse_toolButton.setToolTip("Colapse the side bar")
        self.search_lineEdit.setToolTip("Type employee information for search here")
        self.searchField_comboBox.setToolTip("Select the empoloyee information type")
        self.search_toolButton.setToolTip("Click to search for the employee information entered above")
        self.newEmp_toolButton.setToolTip("Create a new employee")
        self.report_toolButton.setToolTip("This is the report_toolButton ToolTip")
        self.info_toolButton.setToolTip("Click to view your employee information")
        self.userManual_toolButton.setToolTip("Click to view the program manual")
        self.signOut_toolButton.setToolTip("Log out of your account")
        self.hamburger_toolButton.setToolTip("Reopen the side bar")
        self.signOutTopBar_toolButton.setToolTip("Sign out of your account")
        return 0
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1401, 950)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color: rgb(41, 46, 50);\n"
"}\n"
"\n"
"QCalendar {\n"
"    background-color: white;\n"
"    color: black;\n"
"}\n"
"\n"
"QCalendarWidget QTableView QLabel \n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"    background-color: #222b2e;\n"
"    color: #d3dae3;\n"
"}\n"
"QPlainTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"    background-color: #222b2e;\n"
"    color: #d3dae3;\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #151a1e;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    background-color: #151a1e;;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #1c1f1f;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #2c2f2f;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    selection-background-color: rgb(120, 190, 72);\n"
"    border-width: 2px solid;\n"
"    border-color: rgb(120, 190, 72);\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QLineEdit QMenu {\n"
"background-color: white;\n"
"}\n"
"\n"
"QLineEdit QMenu::item {\n"
"color: black;\n"
"}\n"
"\n"
"QLineEdit QMenu::item::selected { \n"
"background-color: rgb(36, 93, 56)\n"
"}\n"
"QLabel {\n"
"    color: #d3dae3;\n"
"}\n"
"QLCDNumber {\n"
"    color: #4d9b87;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: #d3dae3;\n"
"    border-radius: 10px;\n"
"    border-color: transparent;\n"
"    border-style: solid;\n"
"    background-color: #52595d;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #214037    ;\n"
"    border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: #151a1e;\n"
"}\n"
"QMenuBar::item {\n"
"    color: #d3dae3;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"    background-color: #151a1e;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background-color: #252a2e;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu {\n"
"    background-color: #151a1e;\n"
"}\n"
"QMenu::item:selected {\n"
"    background-color: #252a2e;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item {\n"
"    color: #d3dae3;\n"
"    background-color: #151a1e;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(120, 190, 72);\n"
"        background-color: #1e282c;\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"}\n"
"QTabBar::tab:first {\n"
"    border-style: solid;\n"
"    border-left-width:1px;\n"
"    border-right-width:0px;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:0px;\n"
"    border-color:  rgb(120, 190, 72);\n"
"    border-top-left-radius: 4px;\n"
"    color: #d3dae3;\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    margin-left:0px;\n"
"    background-color: #151a1e;\n"
"}\n"
"QTabBar::tab:last {\n"
"    border-style: solid;\n"
"    border-top-width:1px;\n"
"    border-left-width:1px;\n"
"    border-right-width:1px;\n"
"    border-bottom-width:0px;\n"
"    border-color:  rgb(120, 190, 72);\n"
"    border-top-right-radius: 4px;\n"
"    color: #d3dae3;\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    margin-left: 0px;\n"
"    background-color: #151a1e;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:0px;\n"
"    border-left-width:1px;\n"
"    border-color:  rgb(120, 190, 72);\n"
"    color: #d3dae3;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: #151a1e;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-right-width: 2px;\n"
"    border-top-width: 2px;\n"
"    border-left-width: 2px;\n"
"    border-color: rgb(120, 190, 72);\n"
"    color: black;\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    margin-left:0px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-right-width: 2px;\n"
"    border-top-width: 2px;\n"
"    border-left-width: 2px;\n"
"    border-color: rgb(120, 190, 72);\n"
"    color: black;\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    margin-left:0px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(120, 190, 72);;\n"
"    color: #000000;\n"
"    background-color: rgb(120, 190, 72);\n"
"    padding: 0.2;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(120, 190, 72);;\n"
"    color: #000000;\n"
"}\n"
"QRadioButton {\n"
"    color: #d3dae3;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(120, 190, 72);\n"
"    color: #a9b7c6;\n"
"    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.4,fx:0.5, fy:0.5, stop:0 #4fa08b, stop:1 rgb(120, 190, 72));\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(120, 190, 72);\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    color: #d3dae3;\n"
"    background-color: #222b2e;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color: #d3dae3;\n"
"    background-color: #222b2e;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"}\n"
"QTimeEdit {\n"
"    color: #d3dae3;\n"
"    background-color: #222b2e;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"}\n"
"QDateTimeEdit {\n"
"    color: #d3dae3;\n"
"    background-color: #222b2e;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"}\n"
"QDateEdit {\n"
"    color: #d3dae3;\n"
"    background-color: #222b2e;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"}\n"
"QFontComboBox {\n"
"    color: #d3dae3;\n"
"    background-color: #222b2e;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"}\n"
"QComboBox {\n"
"    color: #d3dae3;\n"
"    background-color: #222b2e;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(120, 190, 72);\n"
"}\n"
"\n"
"QDial {\n"
"    background: #16a085;\n"
"}\n"
"\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color: #222b2e;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color:#222b2e;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color:#222b2e;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color:#222b2e;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background-color: #52595d;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background-color: #52595d;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #1a2224;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: #1a2224;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: #52595d;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: #52595d;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #15433a;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: #15433a;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 10px;\n"
"    border: 1px transparent grey;\n"
"    margin: 0px 20px 0px 20px;\n"
"    background: transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
"    max-width: 10px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"    background: transparent;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #52595d;\n"
"    border-style: transparent;\n"
"    border-radius: 4px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #58a492;\n"
"    border-style: transparent;\n"
"    border-radius: 4px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #52595d;\n"
"    border-style: transparent;\n"
"    border-radius: 4px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #58a492;\n"
"    border-style: transparent;\n"
"    border-radius: 4px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: #15433a;\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: #15433a;\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-bottom-left-radius: 4px;\n"
"   background: #15433a;\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-bottom-left-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-top-right-radius: 4px;\n"
"   background: #15433a;\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-top-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"   background: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(41, 46, 50);\n"
"\n"
"QCalendar {\n"
"    background-color: white;\n"
"}\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"    background-color: #222b2e;\n"
"    color: #d3dae3;\n"
"}\n"
"QPlainTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"    background-color: #222b2e;\n"
"    color: #d3dae3;\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #151a1e;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    background-color: #151a1e;;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #1c1f1f;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #2c2f2f;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    selection-background-color: rgb(120, 190, 72);\n"
"    border-width: 2px solid;\n"
"    border-color: rgb(120, 190, 72);\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QLineEdit QMenu {\n"
"background-color: white;\n"
"}\n"
"\n"
"QLineEdit QMenu::item {\n"
"color: black;\n"
"}\n"
"\n"
"QLineEdit QMenu::item::selected { \n"
"background-color: rgb(36, 93, 56)\n"
"}\n"
"QLabel {\n"
"    color: #d3dae3;\n"
"}\n"
"QLCDNumber {\n"
"    color: #4d9b87;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: #d3dae3;\n"
"    border-radius: 10px;\n"
"    border-color: transparent;\n"
"    border-style: solid;\n"
"    background-color: #52595d;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #214037    ;\n"
"    border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: #151a1e;\n"
"}\n"
"QMenuBar::item {\n"
"    color: #d3dae3;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"    background-color: #151a1e;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background-color: #252a2e;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu {\n"
"    background-color: #151a1e;\n"
"}\n"
"QMenu::item:selected {\n"
"    background-color: #252a2e;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item {\n"
"    color: #d3dae3;\n"
"    background-color: #151a1e;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(120, 190, 72);\n"
"        background-color: #1e282c;\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"}\n"
"QTabBar::tab:first {\n"
"    border-style: solid;\n"
"    border-left-width:1px;\n"
"    border-right-width:0px;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:0px;\n"
"    border-color:  rgb(120, 190, 72);\n"
"    border-top-left-radius: 4px;\n"
"    color: #d3dae3;\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    margin-left:0px;\n"
"    background-color: #151a1e;\n"
"}\n"
"QTabBar::tab:last {\n"
"    border-style: solid;\n"
"    border-top-width:1px;\n"
"    border-left-width:1px;\n"
"    border-right-width:1px;\n"
"    border-bottom-width:0px;\n"
"    border-color:  rgb(120, 190, 72);\n"
"    border-top-right-radius: 4px;\n"
"    color: #d3dae3;\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    margin-left: 0px;\n"
"    background-color: #151a1e;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:0px;\n"
"    border-left-width:1px;\n"
"    border-color:  rgb(120, 190, 72);\n"
"    color: #d3dae3;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: #151a1e;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-right-width: 2px;\n"
"    border-top-width: 2px;\n"
"    border-left-width: 2px;\n"
"    border-color: rgb(120, 190, 72);\n"
"    color: black;\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    margin-left:0px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-right-width: 2px;\n"
"    border-top-width: 2px;\n"
"    border-left-width: 2px;\n"
"    border-color: rgb(120, 190, 72);\n"
"    color: black;\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    margin-left:0px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(120, 190, 72);;\n"
"    color: #000000;\n"
"    background-color: rgb(120, 190, 72);\n"
"    padding: 0.2;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(120, 190, 72);;\n"
"    color: #000000;\n"
"}\n"
"QRadioButton {\n"
"    color: #d3dae3;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(120, 190, 72);\n"
"    color: #a9b7c6;\n"
"    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.4,fx:0.5, fy:0.5, stop:0 #4fa08b, stop:1 rgb(120, 190, 72));\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: rgb(120, 190, 72);\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    color: #d3dae3;\n"
"    background-color: #222b2e;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color: #d3dae3;\n"
"    background-color: #222b2e;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"}\n"
"QTimeEdit {\n"
"    color: #d3dae3;\n"
"    background-color: #222b2e;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"}\n"
"QDateTimeEdit {\n"
"    color: #d3dae3;\n"
"    background-color: #222b2e;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"}\n"
"QDateEdit {\n"
"    color: #d3dae3;\n"
"    background-color: #222b2e;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"}\n"
"QFontComboBox {\n"
"    color: #d3dae3;\n"
"    background-color: #222b2e;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #4fa08b;\n"
"}\n"
"QComboBox {\n"
"    color: #d3dae3;\n"
"    background-color: #222b2e;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(120, 190, 72);\n"
"}\n"
"\n"
"QDial {\n"
"    background: #16a085;\n"
"}\n"
"\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color: #222b2e;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color:#222b2e;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color:#222b2e;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color:#222b2e;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background-color: #52595d;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background-color: #52595d;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #1a2224;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: #1a2224;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: #52595d;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: #52595d;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #15433a;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: #15433a;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 10px;\n"
"    border: 1px transparent grey;\n"
"    margin: 0px 20px 0px 20px;\n"
"    background: transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
"    max-width: 10px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"    background: transparent;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #52595d;\n"
"    border-style: transparent;\n"
"    border-radius: 4px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #58a492;\n"
"    border-style: transparent;\n"
"    border-radius: 4px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #52595d;\n"
"    border-style: transparent;\n"
"    border-radius: 4px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #58a492;\n"
"    border-style: transparent;\n"
"    border-radius: 4px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: #15433a;\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: #15433a;\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-bottom-left-radius: 4px;\n"
"   background: #15433a;\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-bottom-left-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-top-right-radius: 4px;\n"
"   background: #15433a;\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 4px;\n"
"   border-top-right-radius: 4px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"   background: none;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sideBar_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sideBar_frame.sizePolicy().hasHeightForWidth())
        self.sideBar_frame.setSizePolicy(sizePolicy)
        self.sideBar_frame.setMinimumSize(QtCore.QSize(350, 0))
        self.sideBar_frame.setStyleSheet("background-color: rgb(22, 24, 25);\n"
"\n"
"QLineEdit QMenu {\n"
"background-color: white;\n"
"}\n"
"\n"
"QLineEdit QMenu::item {\n"
"color: black;\n"
"}\n"
"\n"
"QLineEdit QMenu::item::selected { \n"
"color: rgb(255, 0, 0)\n"
"}\n"
"\n"
"")
        self.sideBar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sideBar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideBar_frame.setObjectName("sideBar_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sideBar_frame)
        self.verticalLayout.setContentsMargins(0, 20, 0, 30)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.collapse_horizontalLayout = QtWidgets.QHBoxLayout()
        self.collapse_horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.collapse_horizontalLayout.setSpacing(0)
        self.collapse_horizontalLayout.setObjectName("collapse_horizontalLayout")
        self.closeSideBar_toolButton = QtWidgets.QToolButton(self.sideBar_frame)
        self.closeSideBar_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeSideBar_toolButton.setStyleSheet("QToolButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: transparent;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"border-width: 2px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-width: 4px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/png/icons8-macos-close-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeSideBar_toolButton.setIcon(icon)
        self.closeSideBar_toolButton.setIconSize(QtCore.QSize(25, 25))
        self.closeSideBar_toolButton.setObjectName("closeSideBar_toolButton")
        self.collapse_horizontalLayout.addWidget(self.closeSideBar_toolButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.collapse_horizontalLayout.addItem(spacerItem)
        self.collapse_toolButton = QtWidgets.QToolButton(self.sideBar_frame)
        self.collapse_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.collapse_toolButton.setStyleSheet("QToolButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: transparent;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"border-width: 2px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-width: 4px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/assets/png/arrow-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.collapse_toolButton.setIcon(icon1)
        self.collapse_toolButton.setIconSize(QtCore.QSize(25, 25))
        self.collapse_toolButton.setObjectName("collapse_toolButton")
        self.collapse_horizontalLayout.addWidget(self.collapse_toolButton)
        self.verticalLayout.addLayout(self.collapse_horizontalLayout)
        self.frame_13 = QtWidgets.QFrame(self.sideBar_frame)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_13.setAutoFillBackground(False)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.search_lineEdit = QtWidgets.QLineEdit(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_lineEdit.sizePolicy().hasHeightForWidth())
        self.search_lineEdit.setSizePolicy(sizePolicy)
        self.search_lineEdit.setMinimumSize(QtCore.QSize(230, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.search_lineEdit.setFont(font)
        self.search_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: white;\n"
"color: white;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 5px;")
        self.search_lineEdit.setInputMask("")
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.verticalLayout_7.addWidget(self.search_lineEdit)
        self.verticalLayout.addWidget(self.frame_13)
        self.searchField_gridLayout = QtWidgets.QGridLayout()
        self.searchField_gridLayout.setContentsMargins(-1, 10, -1, 15)
        self.searchField_gridLayout.setSpacing(0)
        self.searchField_gridLayout.setObjectName("searchField_gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.searchField_gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.searchField_comboBox = QtWidgets.QComboBox(self.sideBar_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchField_comboBox.sizePolicy().hasHeightForWidth())
        self.searchField_comboBox.setSizePolicy(sizePolicy)
        self.searchField_comboBox.setMinimumSize(QtCore.QSize(150, 30))
        self.searchField_comboBox.setMaximumSize(QtCore.QSize(220, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.searchField_comboBox.setFont(font)
        self.searchField_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchField_comboBox.setStyleSheet("QComboBox {\n"
"border-style: outset;\n"
"border: 3px solid rgb(120, 190, 72);\n"
"padding-left: 7px\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(:/icons/assets/png/icons8-sort-down-96.png);\n"
"    width: 22px;\n"
"    height: 35px;\n"
"    padding-right: 6px;\n"
"    padding-top: 2px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin:margin;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"     width: 25px;\n"
"    height: 38px;\n"
"}\n"
"\n"
"QComboBox::drop-down:pressed {\n"
"   padding-top: 5px;\n"
"     width: 22px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"\n"
"")
        self.searchField_comboBox.setEditable(False)
        self.searchField_comboBox.setObjectName("searchField_comboBox")
        self.searchField_comboBox.addItem("")
        self.searchField_comboBox.addItem("")
        self.searchField_comboBox.addItem("")
        self.searchField_comboBox.addItem("")
        self.searchField_gridLayout.addWidget(self.searchField_comboBox, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.searchField_gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.search_toolButton = QtWidgets.QToolButton(self.sideBar_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_toolButton.sizePolicy().hasHeightForWidth())
        self.search_toolButton.setSizePolicy(sizePolicy)
        self.search_toolButton.setMinimumSize(QtCore.QSize(50, 50))
        self.search_toolButton.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_toolButton.setFont(font)
        self.search_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_toolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.search_toolButton.setStyleSheet("QToolButton {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 25px;\n"
"border-color: rgb(120, 190, 72);\n"
"padding: 2px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"background-color: rgb(120, 190, 72)\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-width: 4px;\n"
"background-color: rgb(120, 190, 72);\n"
"border-color: white;\n"
"}")
        self.search_toolButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/assets/png/magnify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_toolButton.setIcon(icon2)
        self.search_toolButton.setIconSize(QtCore.QSize(25, 25))
        self.search_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.search_toolButton.setObjectName("search_toolButton")
        self.searchField_gridLayout.addWidget(self.search_toolButton, 0, 3, 1, 1, QtCore.Qt.AlignVCenter)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.searchField_gridLayout.addItem(spacerItem3, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.searchField_gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.newEmp_toolButton = QtWidgets.QToolButton(self.sideBar_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newEmp_toolButton.sizePolicy().hasHeightForWidth())
        self.newEmp_toolButton.setSizePolicy(sizePolicy)
        self.newEmp_toolButton.setMinimumSize(QtCore.QSize(300, 60))
        self.newEmp_toolButton.setMaximumSize(QtCore.QSize(1000, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.newEmp_toolButton.setFont(font)
        self.newEmp_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newEmp_toolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.newEmp_toolButton.setStyleSheet("QToolButton {\n"
"border-style: none;\n"
"color: white;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: white;\n"
"background-color: rgb(120, 190, 72);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: white;\n"
"background-color: rgb(120, 190, 72);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/assets/png/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newEmp_toolButton.setIcon(icon3)
        self.newEmp_toolButton.setIconSize(QtCore.QSize(25, 25))
        self.newEmp_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.newEmp_toolButton.setObjectName("newEmp_toolButton")
        self.verticalLayout.addWidget(self.newEmp_toolButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.report_toolButton = QtWidgets.QToolButton(self.sideBar_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.report_toolButton.sizePolicy().hasHeightForWidth())
        self.report_toolButton.setSizePolicy(sizePolicy)
        self.report_toolButton.setMinimumSize(QtCore.QSize(300, 60))
        self.report_toolButton.setMaximumSize(QtCore.QSize(1000, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.report_toolButton.setFont(font)
        self.report_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.report_toolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.report_toolButton.setStyleSheet("QToolButton {\n"
"border-style: none;\n"
"color: white;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: white;\n"
"background-color: rgb(120, 190, 72);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: white;\n"
"background-color: rgb(120, 190, 72);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/assets/png/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.report_toolButton.setIcon(icon4)
        self.report_toolButton.setIconSize(QtCore.QSize(25, 25))
        self.report_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.report_toolButton.setObjectName("report_toolButton")
        self.verticalLayout.addWidget(self.report_toolButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.info_toolButton = QtWidgets.QToolButton(self.sideBar_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_toolButton.sizePolicy().hasHeightForWidth())
        self.info_toolButton.setSizePolicy(sizePolicy)
        self.info_toolButton.setMinimumSize(QtCore.QSize(300, 60))
        self.info_toolButton.setMaximumSize(QtCore.QSize(1000, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.info_toolButton.setFont(font)
        self.info_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.info_toolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.info_toolButton.setStyleSheet("QToolButton {\n"
"border-style: none;\n"
"color: white;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: white;\n"
"background-color: rgb(120, 190, 72);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: white;\n"
"background-color: rgb(120, 190, 72);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/assets/png/user-info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_toolButton.setIcon(icon5)
        self.info_toolButton.setIconSize(QtCore.QSize(25, 25))
        self.info_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.info_toolButton.setObjectName("info_toolButton")
        self.verticalLayout.addWidget(self.info_toolButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.userManual_toolButton = QtWidgets.QToolButton(self.sideBar_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userManual_toolButton.sizePolicy().hasHeightForWidth())
        self.userManual_toolButton.setSizePolicy(sizePolicy)
        self.userManual_toolButton.setMinimumSize(QtCore.QSize(300, 60))
        self.userManual_toolButton.setMaximumSize(QtCore.QSize(1000, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.userManual_toolButton.setFont(font)
        self.userManual_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.userManual_toolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.userManual_toolButton.setStyleSheet("QToolButton {\n"
"border-style: none;\n"
"color: white;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: white;\n"
"background-color: rgb(120, 190, 72);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: white;\n"
"background-color: rgb(120, 190, 72);\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/assets/png/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userManual_toolButton.setIcon(icon6)
        self.userManual_toolButton.setIconSize(QtCore.QSize(25, 25))
        self.userManual_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.userManual_toolButton.setObjectName("userManual_toolButton")
        self.verticalLayout.addWidget(self.userManual_toolButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem7)
        self.signOut_toolButton = QtWidgets.QToolButton(self.sideBar_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signOut_toolButton.sizePolicy().hasHeightForWidth())
        self.signOut_toolButton.setSizePolicy(sizePolicy)
        self.signOut_toolButton.setMinimumSize(QtCore.QSize(150, 40))
        self.signOut_toolButton.setMaximumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.signOut_toolButton.setFont(font)
        self.signOut_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signOut_toolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.signOut_toolButton.setStyleSheet("QToolButton {\n"
"border-style: none;\n"
"color: white;\n"
"border-radius: 20px;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"    background-color: rgb(45, 96, 114);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"border-width: 2px;\n"
"border-color: purple;\n"
"background-color: rgb(90, 160, 42)\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: white;\n"
"background-color: rgb(60, 130, 12)\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/assets/png/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.signOut_toolButton.setIcon(icon7)
        self.signOut_toolButton.setIconSize(QtCore.QSize(25, 25))
        self.signOut_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.signOut_toolButton.setObjectName("signOut_toolButton")
        self.verticalLayout.addWidget(self.signOut_toolButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 1)
        self.verticalLayout.setStretch(9, 1)
        self.verticalLayout.setStretch(10, 1)
        self.horizontalLayout_3.addWidget(self.sideBar_frame)
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setMinimumSize(QtCore.QSize(1040, 0))
        self.main_frame.setStyleSheet("")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topBar_frame = QtWidgets.QFrame(self.main_frame)
        self.topBar_frame.setMinimumSize(QtCore.QSize(0, 30))
        self.topBar_frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.topBar_frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.topBar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topBar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topBar_frame.setObjectName("topBar_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.topBar_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hamburger_toolButton = QtWidgets.QToolButton(self.topBar_frame)
        self.hamburger_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hamburger_toolButton.setStyleSheet("QToolButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: transparent;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"border-width: 2px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-width: 4px;\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/assets/png/icons8-menu-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hamburger_toolButton.setIcon(icon8)
        self.hamburger_toolButton.setIconSize(QtCore.QSize(25, 25))
        self.hamburger_toolButton.setObjectName("hamburger_toolButton")
        self.horizontalLayout_2.addWidget(self.hamburger_toolButton)
        spacerItem8 = QtWidgets.QSpacerItem(876, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.signOutTopBar_toolButton = QtWidgets.QToolButton(self.topBar_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signOutTopBar_toolButton.sizePolicy().hasHeightForWidth())
        self.signOutTopBar_toolButton.setSizePolicy(sizePolicy)
        self.signOutTopBar_toolButton.setMinimumSize(QtCore.QSize(110, 30))
        self.signOutTopBar_toolButton.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.signOutTopBar_toolButton.setFont(font)
        self.signOutTopBar_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signOutTopBar_toolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.signOutTopBar_toolButton.setStyleSheet("QToolButton {\n"
"border-style: none;\n"
"color: white;\n"
"border-radius: 20px;\n"
"padding: 5px;\n"
"background-color: rgb(45, 96, 114);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"border-width: 2px;\n"
"border-color: purple;\n"
"background-color: rgb(90, 160, 42)\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"border-style: outset;\n"
"border-width: 3px;\n"
"border-color: white;\n"
"background-color: rgb(60, 130, 12)\n"
"}")
        self.signOutTopBar_toolButton.setIconSize(QtCore.QSize(25, 25))
        self.signOutTopBar_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.signOutTopBar_toolButton.setObjectName("signOutTopBar_toolButton")
        self.horizontalLayout_2.addWidget(self.signOutTopBar_toolButton)
        self.verticalLayout_2.addWidget(self.topBar_frame)
        self.mainScreen_stackedWidget = QtWidgets.QStackedWidget(self.main_frame)
        self.mainScreen_stackedWidget.setStyleSheet("QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    selection-background-color: rgb(36, 93, 56);\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QLineEdit QMenu {\n"
"background-color: white;\n"
"}\n"
"\n"
"QLineEdit QMenu::item {\n"
"color: black;\n"
"}\n"
"\n"
"QLineEdit QMenu::item::selected { \n"
"background-color: rgb(36, 93, 56)\n"
"}")
        self.mainScreen_stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainScreen_stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainScreen_stackedWidget.setObjectName("mainScreen_stackedWidget")
        self.searchResultsScreen_page0 = QtWidgets.QWidget()
        self.searchResultsScreen_page0.setObjectName("searchResultsScreen_page0")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.searchResultsScreen_page0)
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 9)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.searchResultsScreen_page0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.searchScrollArea = QtWidgets.QWidget()
        self.searchScrollArea.setGeometry(QtCore.QRect(0, 0, 617, 898))
        self.searchScrollArea.setObjectName("searchScrollArea")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.searchScrollArea)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.emptyHeader_label = QtWidgets.QLabel(self.searchScrollArea)
        self.emptyHeader_label.setMinimumSize(QtCore.QSize(175, 32))
        self.emptyHeader_label.setMaximumSize(QtCore.QSize(175, 32))
        self.emptyHeader_label.setStyleSheet("")
        self.emptyHeader_label.setText("")
        self.emptyHeader_label.setObjectName("emptyHeader_label")
        self.gridLayout_7.addWidget(self.emptyHeader_label, 0, 0, 1, 1)
        self.firstNameHeader_label = QtWidgets.QLabel(self.searchScrollArea)
        self.firstNameHeader_label.setMinimumSize(QtCore.QSize(100, 32))
        self.firstNameHeader_label.setMaximumSize(QtCore.QSize(250, 32))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.firstNameHeader_label.setFont(font)
        self.firstNameHeader_label.setStyleSheet("color: rgb(120, 190, 72);")
        self.firstNameHeader_label.setObjectName("firstNameHeader_label")
        self.gridLayout_7.addWidget(self.firstNameHeader_label, 0, 1, 1, 1)
        self.lastNameHeader_label = QtWidgets.QLabel(self.searchScrollArea)
        self.lastNameHeader_label.setMinimumSize(QtCore.QSize(100, 32))
        self.lastNameHeader_label.setMaximumSize(QtCore.QSize(250, 32))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lastNameHeader_label.setFont(font)
        self.lastNameHeader_label.setStyleSheet("color: rgb(120, 190, 72);")
        self.lastNameHeader_label.setObjectName("lastNameHeader_label")
        self.gridLayout_7.addWidget(self.lastNameHeader_label, 0, 2, 1, 1)
        self.titleHeader_label = QtWidgets.QLabel(self.searchScrollArea)
        self.titleHeader_label.setMinimumSize(QtCore.QSize(100, 32))
        self.titleHeader_label.setMaximumSize(QtCore.QSize(250, 32))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.titleHeader_label.setFont(font)
        self.titleHeader_label.setStyleSheet("color: rgb(120, 190, 72);")
        self.titleHeader_label.setObjectName("titleHeader_label")
        self.gridLayout_7.addWidget(self.titleHeader_label, 0, 3, 1, 1)
        self.departmentHeader_label = QtWidgets.QLabel(self.searchScrollArea)
        self.departmentHeader_label.setMinimumSize(QtCore.QSize(100, 32))
        self.departmentHeader_label.setMaximumSize(QtCore.QSize(250, 32))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.departmentHeader_label.setFont(font)
        self.departmentHeader_label.setStyleSheet("color: rgb(120, 190, 72);")
        self.departmentHeader_label.setObjectName("departmentHeader_label")
        self.gridLayout_7.addWidget(self.departmentHeader_label, 0, 4, 1, 1)
        self.scrollArea.setWidget(self.searchScrollArea)
        self.gridLayout_6.addWidget(self.scrollArea, 0, 1, 1, 1)
        self.mainScreen_stackedWidget.addWidget(self.searchResultsScreen_page0)
        self.userInfoScreen_page1 = QtWidgets.QWidget()
        self.userInfoScreen_page1.setObjectName("userInfoScreen_page1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.userInfoScreen_page1)
        self.horizontalLayout.setContentsMargins(9, 4, -1, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userInfo_tabWidget = QtWidgets.QTabWidget(self.userInfoScreen_page1)
        self.userInfo_tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.userInfo_tabWidget.setStyleSheet("")
        self.userInfo_tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.userInfo_tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.userInfo_tabWidget.setObjectName("userInfo_tabWidget")
        self.generalTab = QtWidgets.QWidget()
        self.generalTab.setObjectName("generalTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.generalTab)
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.generalTab)
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem9, 17, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 4, 4, 1, 1)
        self.email_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_label.sizePolicy().hasHeightForWidth())
        self.email_label.setSizePolicy(sizePolicy)
        self.email_label.setMinimumSize(QtCore.QSize(270, 0))
        self.email_label.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.email_label.setFont(font)
        self.email_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.email_label.setObjectName("email_label")
        self.gridLayout_2.addWidget(self.email_label, 3, 3, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 18, 3, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 10, 4, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem14, 2, 3, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem15, 2, 2, 1, 1)
        self.department_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.department_lineEdit.sizePolicy().hasHeightForWidth())
        self.department_lineEdit.setSizePolicy(sizePolicy)
        self.department_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.department_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.department_lineEdit.setFont(font)
        self.department_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.department_lineEdit.setMaxLength(30)
        self.department_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.department_lineEdit.setObjectName("department_lineEdit")
        self.gridLayout_2.addWidget(self.department_lineEdit, 9, 3, 1, 1)
        self.title_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_lineEdit.sizePolicy().hasHeightForWidth())
        self.title_lineEdit.setSizePolicy(sizePolicy)
        self.title_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.title_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.title_lineEdit.setFont(font)
        self.title_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.title_lineEdit.setMaxLength(30)
        self.title_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.title_lineEdit.setObjectName("title_lineEdit")
        self.gridLayout_2.addWidget(self.title_lineEdit, 11, 3, 1, 1)
        self.lastName_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastName_label.sizePolicy().hasHeightForWidth())
        self.lastName_label.setSizePolicy(sizePolicy)
        self.lastName_label.setMinimumSize(QtCore.QSize(270, 0))
        self.lastName_label.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.lastName_label.setFont(font)
        self.lastName_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lastName_label.setObjectName("lastName_label")
        self.gridLayout_2.addWidget(self.lastName_label, 5, 1, 1, 1)
        self.addressOne_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addressOne_label.sizePolicy().hasHeightForWidth())
        self.addressOne_label.setSizePolicy(sizePolicy)
        self.addressOne_label.setMinimumSize(QtCore.QSize(270, 0))
        self.addressOne_label.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.addressOne_label.setFont(font)
        self.addressOne_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.addressOne_label.setObjectName("addressOne_label")
        self.gridLayout_2.addWidget(self.addressOne_label, 8, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem16, 5, 4, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem17, 2, 4, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem18, 17, 4, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem19, 14, 4, 2, 1)
        self.phone_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_label.sizePolicy().hasHeightForWidth())
        self.phone_label.setSizePolicy(sizePolicy)
        self.phone_label.setMinimumSize(QtCore.QSize(270, 0))
        self.phone_label.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.phone_label.setFont(font)
        self.phone_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.phone_label.setObjectName("phone_label")
        self.gridLayout_2.addWidget(self.phone_label, 5, 3, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem20, 16, 4, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem21, 10, 2, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem22, 8, 2, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem23, 17, 0, 1, 1)
        self.startDate_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startDate_label.sizePolicy().hasHeightForWidth())
        self.startDate_label.setSizePolicy(sizePolicy)
        self.startDate_label.setMinimumSize(QtCore.QSize(270, 0))
        self.startDate_label.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.startDate_label.setFont(font)
        self.startDate_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.startDate_label.setObjectName("startDate_label")
        self.gridLayout_2.addWidget(self.startDate_label, 12, 3, 1, 1)
        self.state_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state_lineEdit.sizePolicy().hasHeightForWidth())
        self.state_lineEdit.setSizePolicy(sizePolicy)
        self.state_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.state_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.state_lineEdit.setFont(font)
        self.state_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.state_lineEdit.setMaxLength(30)
        self.state_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.state_lineEdit.setObjectName("state_lineEdit")
        self.gridLayout_2.addWidget(self.state_lineEdit, 13, 1, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem24, 12, 4, 1, 1)
        self.city_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city_label.sizePolicy().hasHeightForWidth())
        self.city_label.setSizePolicy(sizePolicy)
        self.city_label.setMinimumSize(QtCore.QSize(270, 0))
        self.city_label.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.city_label.setFont(font)
        self.city_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.city_label.setObjectName("city_label")
        self.gridLayout_2.addWidget(self.city_label, 10, 1, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem25, 4, 2, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem26, 18, 0, 1, 1)
        self.saveGeneral_toolButton = QtWidgets.QToolButton(self.frame_2)
        self.saveGeneral_toolButton.setMinimumSize(QtCore.QSize(75, 30))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.saveGeneral_toolButton.setFont(font)
        self.saveGeneral_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveGeneral_toolButton.setStyleSheet("QToolButton {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color: rgb(120, 190, 72);\n"
"color: white;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"padding-top: 6px;\n"
"background-color: rgb(120, 190, 72);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"padding-top: 8px;\n"
"background-color: rgb(90, 160, 42);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgba(0, 0, 0, 70);;\n"
"background-color: rgba(120, 190, 72, 70);\n"
"color: rgba(255, 255, 255, 70);;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.saveGeneral_toolButton.setObjectName("saveGeneral_toolButton")
        self.gridLayout_2.addWidget(self.saveGeneral_toolButton, 18, 2, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem27, 9, 2, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem28, 13, 4, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem29, 4, 0, 1, 1)
        self.editGeneral_toolButton_3 = QtWidgets.QToolButton(self.frame_2)
        self.editGeneral_toolButton_3.setMinimumSize(QtCore.QSize(65, 25))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.editGeneral_toolButton_3.setFont(font)
        self.editGeneral_toolButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editGeneral_toolButton_3.setStyleSheet("QToolButton {\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-radius: 15px;\n"
"border-color: transparent;\n"
"color: transparent;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.editGeneral_toolButton_3.setObjectName("editGeneral_toolButton_3")
        self.gridLayout_2.addWidget(self.editGeneral_toolButton_3, 1, 0, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem30, 18, 1, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem31, 13, 0, 1, 1)
        self.employeeIdGeneral_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employeeIdGeneral_label.sizePolicy().hasHeightForWidth())
        self.employeeIdGeneral_label.setSizePolicy(sizePolicy)
        self.employeeIdGeneral_label.setMinimumSize(QtCore.QSize(270, 15))
        self.employeeIdGeneral_label.setMaximumSize(QtCore.QSize(350, 16777215))
        self.employeeIdGeneral_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.employeeIdGeneral_label.setObjectName("employeeIdGeneral_label")
        self.gridLayout_2.addWidget(self.employeeIdGeneral_label, 0, 2, 1, 1)
        self.editGeneral_toolButton = QtWidgets.QToolButton(self.frame_2)
        self.editGeneral_toolButton.setMinimumSize(QtCore.QSize(65, 25))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.editGeneral_toolButton.setFont(font)
        self.editGeneral_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editGeneral_toolButton.setStyleSheet("QToolButton {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color: rgb(120, 190, 72);\n"
"color: white;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"padding-top: 6px;\n"
"background-color: rgb(120, 190, 72);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"padding-top: 8px;\n"
"background-color: rgb(90, 160, 42);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgba(0, 0, 0, 70);;\n"
"background-color: rgba(120, 190, 72, 70);\n"
"color: rgba(255, 255, 255, 70);;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.editGeneral_toolButton.setObjectName("editGeneral_toolButton")
        self.gridLayout_2.addWidget(self.editGeneral_toolButton, 1, 4, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem32, 5, 2, 1, 1)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem33, 0, 1, 1, 1)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem34, 1, 3, 1, 1)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem35, 11, 0, 1, 1)
        spacerItem36 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem36, 7, 0, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem37, 7, 3, 1, 1)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem38, 6, 4, 1, 1)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem39, 0, 3, 1, 1)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem40, 9, 0, 1, 1)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem41, 14, 2, 1, 1)
        spacerItem42 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem42, 7, 4, 1, 1)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem43, 16, 2, 1, 1)
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem44, 0, 4, 1, 1)
        spacerItem45 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem45, 18, 4, 1, 1)
        spacerItem46 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem46, 2, 1, 1, 1)
        spacerItem47 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem47, 10, 0, 1, 1)
        spacerItem48 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem48, 1, 1, 1, 1)
        spacerItem49 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem49, 2, 0, 1, 1)
        spacerItem50 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem50, 7, 1, 1, 1)
        self.addressOne_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addressOne_lineEdit.sizePolicy().hasHeightForWidth())
        self.addressOne_lineEdit.setSizePolicy(sizePolicy)
        self.addressOne_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.addressOne_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.addressOne_lineEdit.setFont(font)
        self.addressOne_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.addressOne_lineEdit.setMaxLength(30)
        self.addressOne_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.addressOne_lineEdit.setObjectName("addressOne_lineEdit")
        self.gridLayout_2.addWidget(self.addressOne_lineEdit, 9, 1, 1, 1)
        self.city_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city_lineEdit.sizePolicy().hasHeightForWidth())
        self.city_lineEdit.setSizePolicy(sizePolicy)
        self.city_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.city_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.city_lineEdit.setFont(font)
        self.city_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.city_lineEdit.setMaxLength(30)
        self.city_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.city_lineEdit.setObjectName("city_lineEdit")
        self.gridLayout_2.addWidget(self.city_lineEdit, 11, 1, 1, 1)
        spacerItem51 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem51, 17, 1, 1, 1)
        self.startDate_dateEdit = QtWidgets.QDateEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startDate_dateEdit.sizePolicy().hasHeightForWidth())
        self.startDate_dateEdit.setSizePolicy(sizePolicy)
        self.startDate_dateEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.startDate_dateEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.startDate_dateEdit.setFont(font)
        self.startDate_dateEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startDate_dateEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startDate_dateEdit.setStyleSheet("QDateEdit {\n"
"border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"color: black;\n"
"padding: 4px;\n"
"padding-left: 50px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    image: url(:/icons/assets/png/drop-down-black.png);\n"
"    width: 22px;\n"
"    height: 35px;\n"
"    padding-right: 6px;\n"
"    padding-top: 2px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin:margin;\n"
"}\n"
"\n"
"QDateEdit::drop-down:hover {\n"
"     width: 25px;\n"
"    height: 38px;\n"
"}")
        self.startDate_dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.startDate_dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.startDate_dateEdit.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.startDate_dateEdit.setCalendarPopup(True)
        self.startDate_dateEdit.setObjectName("startDate_dateEdit")
        self.gridLayout_2.addWidget(self.startDate_dateEdit, 13, 3, 1, 1)
        spacerItem52 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem52, 12, 2, 1, 1)
        spacerItem53 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem53, 11, 4, 1, 1)
        self.state_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state_label.sizePolicy().hasHeightForWidth())
        self.state_label.setSizePolicy(sizePolicy)
        self.state_label.setMinimumSize(QtCore.QSize(270, 0))
        self.state_label.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.state_label.setFont(font)
        self.state_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.state_label.setObjectName("state_label")
        self.gridLayout_2.addWidget(self.state_label, 12, 1, 1, 1)
        spacerItem54 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem54, 8, 4, 1, 1)
        self.zip_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zip_label.sizePolicy().hasHeightForWidth())
        self.zip_label.setSizePolicy(sizePolicy)
        self.zip_label.setMinimumSize(QtCore.QSize(270, 0))
        self.zip_label.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.zip_label.setFont(font)
        self.zip_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.zip_label.setObjectName("zip_label")
        self.gridLayout_2.addWidget(self.zip_label, 14, 1, 1, 1)
        spacerItem55 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem55, 14, 0, 2, 1)
        self.email_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_lineEdit.sizePolicy().hasHeightForWidth())
        self.email_lineEdit.setSizePolicy(sizePolicy)
        self.email_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.email_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.email_lineEdit.setMaxLength(30)
        self.email_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.gridLayout_2.addWidget(self.email_lineEdit, 4, 3, 1, 1)
        spacerItem56 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem56, 12, 0, 1, 1)
        self.department_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.department_label.sizePolicy().hasHeightForWidth())
        self.department_label.setSizePolicy(sizePolicy)
        self.department_label.setMinimumSize(QtCore.QSize(270, 0))
        self.department_label.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.department_label.setFont(font)
        self.department_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.department_label.setObjectName("department_label")
        self.gridLayout_2.addWidget(self.department_label, 8, 3, 1, 1)
        self.employeeIdGeneral_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.employeeIdGeneral_lineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employeeIdGeneral_lineEdit.sizePolicy().hasHeightForWidth())
        self.employeeIdGeneral_lineEdit.setSizePolicy(sizePolicy)
        self.employeeIdGeneral_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.employeeIdGeneral_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.employeeIdGeneral_lineEdit.setFont(font)
        self.employeeIdGeneral_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.employeeIdGeneral_lineEdit.setMaxLength(30)
        self.employeeIdGeneral_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.employeeIdGeneral_lineEdit.setObjectName("employeeIdGeneral_lineEdit")
        self.gridLayout_2.addWidget(self.employeeIdGeneral_lineEdit, 1, 2, 1, 1)
        spacerItem57 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem57, 17, 2, 1, 1)
        self.lastName_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastName_lineEdit.sizePolicy().hasHeightForWidth())
        self.lastName_lineEdit.setSizePolicy(sizePolicy)
        self.lastName_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.lastName_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lastName_lineEdit.setFont(font)
        self.lastName_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.lastName_lineEdit.setMaxLength(30)
        self.lastName_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lastName_lineEdit.setObjectName("lastName_lineEdit")
        self.gridLayout_2.addWidget(self.lastName_lineEdit, 6, 1, 1, 1)
        self.firstName_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstName_lineEdit.sizePolicy().hasHeightForWidth())
        self.firstName_lineEdit.setSizePolicy(sizePolicy)
        self.firstName_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.firstName_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.firstName_lineEdit.setFont(font)
        self.firstName_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.firstName_lineEdit.setMaxLength(30)
        self.firstName_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.firstName_lineEdit.setObjectName("firstName_lineEdit")
        self.gridLayout_2.addWidget(self.firstName_lineEdit, 4, 1, 1, 1)
        self.zip_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zip_lineEdit.sizePolicy().hasHeightForWidth())
        self.zip_lineEdit.setSizePolicy(sizePolicy)
        self.zip_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.zip_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.zip_lineEdit.setFont(font)
        self.zip_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.zip_lineEdit.setMaxLength(30)
        self.zip_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.zip_lineEdit.setObjectName("zip_lineEdit")
        self.gridLayout_2.addWidget(self.zip_lineEdit, 16, 1, 1, 1)
        spacerItem58 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem58, 8, 0, 1, 1)
        spacerItem59 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem59, 5, 0, 1, 1)
        self.title_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMinimumSize(QtCore.QSize(270, 0))
        self.title_label.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.title_label.setObjectName("title_label")
        self.gridLayout_2.addWidget(self.title_label, 10, 3, 1, 1)
        spacerItem60 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem60, 6, 0, 1, 1)
        spacerItem61 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem61, 16, 3, 1, 1)
        spacerItem62 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem62, 9, 4, 1, 1)
        spacerItem63 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem63, 11, 2, 1, 1)
        spacerItem64 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem64, 14, 3, 1, 1)
        spacerItem65 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem65, 13, 2, 1, 1)
        spacerItem66 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem66, 6, 2, 1, 1)
        spacerItem67 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem67, 16, 0, 1, 1)
        self.firstName_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstName_label.sizePolicy().hasHeightForWidth())
        self.firstName_label.setSizePolicy(sizePolicy)
        self.firstName_label.setMinimumSize(QtCore.QSize(270, 0))
        self.firstName_label.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.firstName_label.setFont(font)
        self.firstName_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.firstName_label.setObjectName("firstName_label")
        self.gridLayout_2.addWidget(self.firstName_label, 3, 1, 1, 1)
        spacerItem68 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem68, 7, 2, 1, 1)
        self.phone_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_lineEdit.sizePolicy().hasHeightForWidth())
        self.phone_lineEdit.setSizePolicy(sizePolicy)
        self.phone_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.phone_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.phone_lineEdit.setFont(font)
        self.phone_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.phone_lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.phone_lineEdit.setMaxLength(30)
        self.phone_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.gridLayout_2.addWidget(self.phone_lineEdit, 6, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_3.setStretch(0, 10)
        self.userInfo_tabWidget.addTab(self.generalTab, "")
        self.personalTab = QtWidgets.QWidget()
        self.personalTab.setObjectName("personalTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.personalTab)
        self.verticalLayout_4.setContentsMargins(15, 20, 15, 20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.personalTab)
        self.frame_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QtCore.QSize(270, 45))
        self.frame_8.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_8.setStyleSheet("background-color: none;\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setContentsMargins(-1, 4, -1, 4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.userAccess_label = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.userAccess_label.setFont(font)
        self.userAccess_label.setAlignment(QtCore.Qt.AlignCenter)
        self.userAccess_label.setObjectName("userAccess_label")
        self.horizontalLayout_7.addWidget(self.userAccess_label)
        self.userAccess_comboBox = QtWidgets.QComboBox(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userAccess_comboBox.sizePolicy().hasHeightForWidth())
        self.userAccess_comboBox.setSizePolicy(sizePolicy)
        self.userAccess_comboBox.setMinimumSize(QtCore.QSize(150, 20))
        self.userAccess_comboBox.setMaximumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.userAccess_comboBox.setFont(font)
        self.userAccess_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.userAccess_comboBox.setStyleSheet("QComboBox {\n"
"background-color: rgb(41, 46, 50);\n"
"border-style: outset;\n"
"border: 3px solid rgb(120, 190, 72);\n"
"padding-left: 7px\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    image: url(:/icons/assets/png/icons8-sort-down-96.png);\n"
"    width: 22px;\n"
"    height: 35px;\n"
"    padding-right: 6px;\n"
"    padding-top: 2px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin:margin;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"     width: 25px;\n"
"    height: 38px;\n"
"}")
        self.userAccess_comboBox.setObjectName("userAccess_comboBox")
        self.userAccess_comboBox.addItem("")
        self.userAccess_comboBox.setItemText(0, "")
        self.userAccess_comboBox.addItem("")
        self.userAccess_comboBox.addItem("")
        self.userAccess_comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.userAccess_comboBox)
        spacerItem69 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem69)
        self.gridLayout.addWidget(self.frame_8, 11, 1, 2, 1)
        spacerItem70 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem70, 23, 1, 1, 1)
        spacerItem71 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem71, 13, 1, 1, 1)
        spacerItem72 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem72, 18, 0, 1, 1)
        spacerItem73 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem73, 2, 2, 1, 1)
        spacerItem74 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem74, 11, 2, 1, 1)
        spacerItem75 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem75, 1, 3, 1, 1)
        spacerItem76 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem76, 0, 1, 1, 1)
        self.birthDay_dateEdit = QtWidgets.QDateEdit(self.frame_4)
        self.birthDay_dateEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.birthDay_dateEdit.sizePolicy().hasHeightForWidth())
        self.birthDay_dateEdit.setSizePolicy(sizePolicy)
        self.birthDay_dateEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.birthDay_dateEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.birthDay_dateEdit.setFont(font)
        self.birthDay_dateEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.birthDay_dateEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.birthDay_dateEdit.setStyleSheet("QDateEdit {\n"
"border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"color: black;\n"
"padding: 4px;\n"
"padding-left: 50px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    image: url(:/icons/assets/png/drop-down-black.png);\n"
"    width: 22px;\n"
"    height: 35px;\n"
"    padding-right: 6px;\n"
"    padding-top: 2px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin:margin;\n"
"}\n"
"\n"
"QDateEdit::drop-down:hover {\n"
"     width: 25px;\n"
"    height: 38px;\n"
"}\n"
"\n"
"QDateEdit: disabled {\n"
"    color: color: #808086;\n"
"}")
        self.birthDay_dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.birthDay_dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.birthDay_dateEdit.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.birthDay_dateEdit.setCalendarPopup(True)
        self.birthDay_dateEdit.setObjectName("birthDay_dateEdit")
        self.gridLayout.addWidget(self.birthDay_dateEdit, 7, 1, 1, 1)
        spacerItem77 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem77, 21, 1, 1, 1)
        self.birthDay_label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.birthDay_label.sizePolicy().hasHeightForWidth())
        self.birthDay_label.setSizePolicy(sizePolicy)
        self.birthDay_label.setMinimumSize(QtCore.QSize(270, 15))
        self.birthDay_label.setMaximumSize(QtCore.QSize(350, 15))
        font = QtGui.QFont()
        font.setKerning(True)
        self.birthDay_label.setFont(font)
        self.birthDay_label.setStyleSheet("background-color: none;\n"
"")
        self.birthDay_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.birthDay_label.setObjectName("birthDay_label")
        self.gridLayout.addWidget(self.birthDay_label, 6, 1, 1, 1)
        spacerItem78 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem78, 18, 4, 1, 1)
        spacerItem79 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem79, 23, 3, 1, 1)
        spacerItem80 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem80, 21, 4, 1, 1)
        self.mailAddressZip_lineEdit = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mailAddressZip_lineEdit.sizePolicy().hasHeightForWidth())
        self.mailAddressZip_lineEdit.setSizePolicy(sizePolicy)
        self.mailAddressZip_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.mailAddressZip_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.mailAddressZip_lineEdit.setFont(font)
        self.mailAddressZip_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.mailAddressZip_lineEdit.setMaxLength(30)
        self.mailAddressZip_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.mailAddressZip_lineEdit.setObjectName("mailAddressZip_lineEdit")
        self.gridLayout.addWidget(self.mailAddressZip_lineEdit, 21, 3, 1, 1)
        spacerItem81 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem81, 5, 0, 1, 1)
        spacerItem82 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem82, 2, 3, 1, 1)
        spacerItem83 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem83, 6, 4, 1, 1)
        self.routingNum_label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.routingNum_label.sizePolicy().hasHeightForWidth())
        self.routingNum_label.setSizePolicy(sizePolicy)
        self.routingNum_label.setMinimumSize(QtCore.QSize(270, 15))
        self.routingNum_label.setMaximumSize(QtCore.QSize(350, 15))
        font = QtGui.QFont()
        font.setKerning(True)
        self.routingNum_label.setFont(font)
        self.routingNum_label.setStyleSheet("background-color: none;\n"
"")
        self.routingNum_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.routingNum_label.setObjectName("routingNum_label")
        self.gridLayout.addWidget(self.routingNum_label, 4, 3, 1, 1)
        spacerItem84 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem84, 14, 2, 1, 1)
        spacerItem85 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem85, 17, 4, 1, 1)
        spacerItem86 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem86, 15, 1, 1, 1)
        spacerItem87 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem87, 22, 2, 1, 1)
        spacerItem88 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem88, 6, 0, 1, 1)
        spacerItem89 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem89, 22, 1, 1, 1)
        self.editPersonal_toolButton = QtWidgets.QToolButton(self.frame_4)
        self.editPersonal_toolButton.setEnabled(True)
        self.editPersonal_toolButton.setMinimumSize(QtCore.QSize(65, 25))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.editPersonal_toolButton.setFont(font)
        self.editPersonal_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editPersonal_toolButton.setStyleSheet("QToolButton {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color: rgb(120, 190, 72);\n"
"color: white;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"padding-top: 6px;\n"
"background-color: rgb(120, 190, 72);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"padding-top: 8px;\n"
"background-color: rgb(90, 160, 42);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgba(0, 0, 0, 70);;\n"
"background-color: rgba(120, 190, 72, 70);\n"
"color: rgba(255, 255, 255, 70);;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.editPersonal_toolButton.setObjectName("editPersonal_toolButton")
        self.gridLayout.addWidget(self.editPersonal_toolButton, 1, 4, 1, 1)
        self.editGeneral_toolButton_4 = QtWidgets.QToolButton(self.frame_4)
        self.editGeneral_toolButton_4.setEnabled(False)
        self.editGeneral_toolButton_4.setMinimumSize(QtCore.QSize(65, 25))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.editGeneral_toolButton_4.setFont(font)
        self.editGeneral_toolButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editGeneral_toolButton_4.setStyleSheet("background-color: transparent;\n"
"color: transparent;\n"
"border-color:transparent;\n"
"")
        self.editGeneral_toolButton_4.setObjectName("editGeneral_toolButton_4")
        self.gridLayout.addWidget(self.editGeneral_toolButton_4, 1, 0, 1, 1)
        spacerItem90 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem90, 6, 2, 1, 1)
        self.mailAddressState_label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mailAddressState_label.sizePolicy().hasHeightForWidth())
        self.mailAddressState_label.setSizePolicy(sizePolicy)
        self.mailAddressState_label.setMinimumSize(QtCore.QSize(270, 15))
        self.mailAddressState_label.setMaximumSize(QtCore.QSize(350, 15))
        font = QtGui.QFont()
        font.setKerning(True)
        self.mailAddressState_label.setFont(font)
        self.mailAddressState_label.setStyleSheet("background-color: none;\n"
"")
        self.mailAddressState_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.mailAddressState_label.setObjectName("mailAddressState_label")
        self.gridLayout.addWidget(self.mailAddressState_label, 17, 3, 1, 1)
        spacerItem91 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem91, 16, 4, 1, 1)
        spacerItem92 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem92, 2, 1, 1, 1)
        spacerItem93 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem93, 21, 0, 1, 1)
        spacerItem94 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem94, 16, 0, 1, 1)
        spacerItem95 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem95, 7, 2, 1, 1)
        spacerItem96 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem96, 16, 1, 1, 1)
        self.mailAddressOne_label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mailAddressOne_label.sizePolicy().hasHeightForWidth())
        self.mailAddressOne_label.setSizePolicy(sizePolicy)
        self.mailAddressOne_label.setMinimumSize(QtCore.QSize(270, 15))
        self.mailAddressOne_label.setMaximumSize(QtCore.QSize(350, 15))
        font = QtGui.QFont()
        font.setKerning(True)
        self.mailAddressOne_label.setFont(font)
        self.mailAddressOne_label.setStyleSheet("background-color: none;\n"
"")
        self.mailAddressOne_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.mailAddressOne_label.setObjectName("mailAddressOne_label")
        self.gridLayout.addWidget(self.mailAddressOne_label, 13, 3, 1, 1)
        spacerItem97 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem97, 1, 1, 1, 1)
        spacerItem98 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem98, 15, 2, 1, 1)
        spacerItem99 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem99, 3, 1, 1, 1)
        spacerItem100 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem100, 18, 1, 1, 1)
        spacerItem101 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem101, 0, 4, 1, 1)
        self.mailAddressCity_lineEdit = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mailAddressCity_lineEdit.sizePolicy().hasHeightForWidth())
        self.mailAddressCity_lineEdit.setSizePolicy(sizePolicy)
        self.mailAddressCity_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.mailAddressCity_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.mailAddressCity_lineEdit.setFont(font)
        self.mailAddressCity_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.mailAddressCity_lineEdit.setMaxLength(30)
        self.mailAddressCity_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.mailAddressCity_lineEdit.setObjectName("mailAddressCity_lineEdit")
        self.gridLayout.addWidget(self.mailAddressCity_lineEdit, 16, 3, 1, 1)
        spacerItem102 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem102, 8, 3, 1, 1)
        spacerItem103 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem103, 3, 0, 1, 1)
        spacerItem104 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem104, 10, 0, 1, 1)
        spacerItem105 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem105, 21, 2, 1, 1)
        spacerItem106 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem106, 13, 2, 1, 1)
        spacerItem107 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem107, 4, 4, 1, 1)
        spacerItem108 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem108, 17, 0, 1, 1)
        spacerItem109 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem109, 19, 4, 1, 1)
        self.savePersonal_toolButton = QtWidgets.QToolButton(self.frame_4)
        self.savePersonal_toolButton.setEnabled(True)
        self.savePersonal_toolButton.setMinimumSize(QtCore.QSize(75, 30))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.savePersonal_toolButton.setFont(font)
        self.savePersonal_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.savePersonal_toolButton.setStyleSheet("QToolButton {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color: rgb(120, 190, 72);\n"
"color: white;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"padding-top: 6px;\n"
"background-color: rgb(120, 190, 72);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"padding-top: 8px;\n"
"background-color: rgb(90, 160, 42);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgba(0, 0, 0, 70);;\n"
"background-color: rgba(120, 190, 72, 70);\n"
"color: rgba(255, 255, 255, 70);;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.savePersonal_toolButton.setObjectName("savePersonal_toolButton")
        self.gridLayout.addWidget(self.savePersonal_toolButton, 23, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(270, 45))
        self.frame_5.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_5.setStyleSheet("background-color: none;\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(-1, 4, -1, 4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem110 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem110)
        self.directDeposit_label = QtWidgets.QLabel(self.frame_5)
        self.directDeposit_label.setMinimumSize(QtCore.QSize(105, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.directDeposit_label.setFont(font)
        self.directDeposit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.directDeposit_label.setObjectName("directDeposit_label")
        self.horizontalLayout_4.addWidget(self.directDeposit_label)
        self.directDepositYes_radioButton = QtWidgets.QRadioButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directDepositYes_radioButton.sizePolicy().hasHeightForWidth())
        self.directDepositYes_radioButton.setSizePolicy(sizePolicy)
        self.directDepositYes_radioButton.setMinimumSize(QtCore.QSize(45, 0))
        self.directDepositYes_radioButton.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.directDepositYes_radioButton.setFont(font)
        self.directDepositYes_radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.directDepositYes_radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.directDepositYes_radioButton.setObjectName("directDepositYes_radioButton")
        self.horizontalLayout_4.addWidget(self.directDepositYes_radioButton, 0, QtCore.Qt.AlignVCenter)
        self.directDepositNo_radioButton = QtWidgets.QRadioButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directDepositNo_radioButton.sizePolicy().hasHeightForWidth())
        self.directDepositNo_radioButton.setSizePolicy(sizePolicy)
        self.directDepositNo_radioButton.setMinimumSize(QtCore.QSize(45, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.directDepositNo_radioButton.setFont(font)
        self.directDepositNo_radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.directDepositNo_radioButton.setObjectName("directDepositNo_radioButton")
        self.horizontalLayout_4.addWidget(self.directDepositNo_radioButton, 0, QtCore.Qt.AlignVCenter)
        spacerItem111 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem111)
        self.gridLayout.addWidget(self.frame_5, 3, 3, 1, 1)
        spacerItem112 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem112, 15, 0, 1, 1)
        spacerItem113 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem113, 12, 0, 1, 1)
        self.mailAddressCity_label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mailAddressCity_label.sizePolicy().hasHeightForWidth())
        self.mailAddressCity_label.setSizePolicy(sizePolicy)
        self.mailAddressCity_label.setMinimumSize(QtCore.QSize(270, 15))
        self.mailAddressCity_label.setMaximumSize(QtCore.QSize(350, 15))
        font = QtGui.QFont()
        font.setKerning(True)
        self.mailAddressCity_label.setFont(font)
        self.mailAddressCity_label.setStyleSheet("background-color: none;\n"
"")
        self.mailAddressCity_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.mailAddressCity_label.setObjectName("mailAddressCity_label")
        self.gridLayout.addWidget(self.mailAddressCity_label, 15, 3, 1, 1)
        self.mailAddressZip_label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mailAddressZip_label.sizePolicy().hasHeightForWidth())
        self.mailAddressZip_label.setSizePolicy(sizePolicy)
        self.mailAddressZip_label.setMinimumSize(QtCore.QSize(270, 15))
        self.mailAddressZip_label.setMaximumSize(QtCore.QSize(350, 15))
        font = QtGui.QFont()
        font.setKerning(True)
        self.mailAddressZip_label.setFont(font)
        self.mailAddressZip_label.setStyleSheet("background-color: none;\n"
"")
        self.mailAddressZip_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.mailAddressZip_label.setObjectName("mailAddressZip_label")
        self.gridLayout.addWidget(self.mailAddressZip_label, 19, 3, 1, 1)
        spacerItem114 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem114, 16, 2, 1, 1)
        self.routingNum_lineEdit = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.routingNum_lineEdit.sizePolicy().hasHeightForWidth())
        self.routingNum_lineEdit.setSizePolicy(sizePolicy)
        self.routingNum_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.routingNum_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.routingNum_lineEdit.setFont(font)
        self.routingNum_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.routingNum_lineEdit.setMaxLength(30)
        self.routingNum_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.routingNum_lineEdit.setObjectName("routingNum_lineEdit")
        self.gridLayout.addWidget(self.routingNum_lineEdit, 5, 3, 1, 1)
        spacerItem115 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem115, 8, 1, 1, 1)
        spacerItem116 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem116, 19, 2, 1, 1)
        spacerItem117 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem117, 8, 2, 1, 1)
        spacerItem118 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem118, 5, 2, 1, 1)
        spacerItem119 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem119, 12, 4, 1, 1)
        spacerItem120 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem120, 15, 4, 1, 1)
        self.employeeIdPersonal_lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.employeeIdPersonal_lineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employeeIdPersonal_lineEdit.sizePolicy().hasHeightForWidth())
        self.employeeIdPersonal_lineEdit.setSizePolicy(sizePolicy)
        self.employeeIdPersonal_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.employeeIdPersonal_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.employeeIdPersonal_lineEdit.setFont(font)
        self.employeeIdPersonal_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.employeeIdPersonal_lineEdit.setMaxLength(30)
        self.employeeIdPersonal_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.employeeIdPersonal_lineEdit.setObjectName("employeeIdPersonal_lineEdit")
        self.gridLayout.addWidget(self.employeeIdPersonal_lineEdit, 1, 2, 1, 1)
        spacerItem121 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem121, 0, 3, 1, 1)
        spacerItem122 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem122, 23, 4, 1, 1)
        spacerItem123 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem123, 10, 4, 1, 1)
        spacerItem124 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem124, 0, 0, 1, 1)
        spacerItem125 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem125, 5, 4, 1, 1)
        spacerItem126 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem126, 17, 2, 1, 1)
        spacerItem127 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem127, 14, 1, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(280, 70))
        self.frame_7.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_7.setStyleSheet("background-color: none;\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem128 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem128, 2, 2, 1, 1)
        self.payTypeCommision_radioButton = QtWidgets.QRadioButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.payTypeCommision_radioButton.sizePolicy().hasHeightForWidth())
        self.payTypeCommision_radioButton.setSizePolicy(sizePolicy)
        self.payTypeCommision_radioButton.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.payTypeCommision_radioButton.setFont(font)
        self.payTypeCommision_radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.payTypeCommision_radioButton.setStyleSheet("")
        self.payTypeCommision_radioButton.setObjectName("payTypeCommision_radioButton")
        self.gridLayout_3.addWidget(self.payTypeCommision_radioButton, 1, 2, 1, 1)
        self.payType_label = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.payType_label.setFont(font)
        self.payType_label.setAlignment(QtCore.Qt.AlignCenter)
        self.payType_label.setObjectName("payType_label")
        self.gridLayout_3.addWidget(self.payType_label, 1, 0, 1, 1)
        self.payTypeSalary_radioButton = QtWidgets.QRadioButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.payTypeSalary_radioButton.sizePolicy().hasHeightForWidth())
        self.payTypeSalary_radioButton.setSizePolicy(sizePolicy)
        self.payTypeSalary_radioButton.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.payTypeSalary_radioButton.setFont(font)
        self.payTypeSalary_radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.payTypeSalary_radioButton.setStyleSheet("")
        self.payTypeSalary_radioButton.setObjectName("payTypeSalary_radioButton")
        self.gridLayout_3.addWidget(self.payTypeSalary_radioButton, 2, 1, 1, 1)
        self.payTypeHourly_radioButton = QtWidgets.QRadioButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.payTypeHourly_radioButton.sizePolicy().hasHeightForWidth())
        self.payTypeHourly_radioButton.setSizePolicy(sizePolicy)
        self.payTypeHourly_radioButton.setMinimumSize(QtCore.QSize(70, 0))
        self.payTypeHourly_radioButton.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.payTypeHourly_radioButton.setFont(font)
        self.payTypeHourly_radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.payTypeHourly_radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.payTypeHourly_radioButton.setObjectName("payTypeHourly_radioButton")
        self.gridLayout_3.addWidget(self.payTypeHourly_radioButton, 1, 1, 1, 1)
        spacerItem129 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem129, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_7, 9, 1, 2, 1)
        spacerItem130 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem130, 7, 4, 1, 1)
        spacerItem131 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem131, 7, 0, 1, 1)
        self.employeeIdPersonal_label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employeeIdPersonal_label.sizePolicy().hasHeightForWidth())
        self.employeeIdPersonal_label.setSizePolicy(sizePolicy)
        self.employeeIdPersonal_label.setMinimumSize(QtCore.QSize(200, 15))
        self.employeeIdPersonal_label.setMaximumSize(QtCore.QSize(350, 14))
        self.employeeIdPersonal_label.setStyleSheet("background-color: none;\n"
"")
        self.employeeIdPersonal_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.employeeIdPersonal_label.setObjectName("employeeIdPersonal_label")
        self.gridLayout.addWidget(self.employeeIdPersonal_label, 0, 2, 1, 1)
        self.mailAddressState_lineEdit = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mailAddressState_lineEdit.sizePolicy().hasHeightForWidth())
        self.mailAddressState_lineEdit.setSizePolicy(sizePolicy)
        self.mailAddressState_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.mailAddressState_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.mailAddressState_lineEdit.setFont(font)
        self.mailAddressState_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.mailAddressState_lineEdit.setMaxLength(30)
        self.mailAddressState_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.mailAddressState_lineEdit.setObjectName("mailAddressState_lineEdit")
        self.gridLayout.addWidget(self.mailAddressState_lineEdit, 18, 3, 1, 1)
        spacerItem132 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem132, 13, 0, 1, 1)
        spacerItem133 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem133, 18, 2, 1, 1)
        spacerItem134 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem134, 10, 2, 1, 1)
        spacerItem135 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem135, 2, 4, 1, 1)
        self.accountNum_label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountNum_label.sizePolicy().hasHeightForWidth())
        self.accountNum_label.setSizePolicy(sizePolicy)
        self.accountNum_label.setMinimumSize(QtCore.QSize(270, 15))
        self.accountNum_label.setMaximumSize(QtCore.QSize(350, 15))
        font = QtGui.QFont()
        font.setKerning(True)
        self.accountNum_label.setFont(font)
        self.accountNum_label.setStyleSheet("background-color: none;\n"
"")
        self.accountNum_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.accountNum_label.setObjectName("accountNum_label")
        self.gridLayout.addWidget(self.accountNum_label, 6, 3, 1, 1)
        self.accountNum_lineEdit = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountNum_lineEdit.sizePolicy().hasHeightForWidth())
        self.accountNum_lineEdit.setSizePolicy(sizePolicy)
        self.accountNum_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.accountNum_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.accountNum_lineEdit.setFont(font)
        self.accountNum_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.accountNum_lineEdit.setMaxLength(30)
        self.accountNum_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.accountNum_lineEdit.setObjectName("accountNum_lineEdit")
        self.gridLayout.addWidget(self.accountNum_lineEdit, 7, 3, 1, 1)
        spacerItem136 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem136, 13, 4, 1, 1)
        self.mailAddressOne_lineEdit = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mailAddressOne_lineEdit.sizePolicy().hasHeightForWidth())
        self.mailAddressOne_lineEdit.setSizePolicy(sizePolicy)
        self.mailAddressOne_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.mailAddressOne_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.mailAddressOne_lineEdit.setFont(font)
        self.mailAddressOne_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.mailAddressOne_lineEdit.setMaxLength(30)
        self.mailAddressOne_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.mailAddressOne_lineEdit.setObjectName("mailAddressOne_lineEdit")
        self.gridLayout.addWidget(self.mailAddressOne_lineEdit, 14, 3, 1, 1)
        spacerItem137 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem137, 14, 0, 1, 1)
        spacerItem138 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem138, 3, 2, 1, 1)
        spacerItem139 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem139, 17, 1, 1, 1)
        self.mailAddressRadio_label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mailAddressRadio_label.sizePolicy().hasHeightForWidth())
        self.mailAddressRadio_label.setSizePolicy(sizePolicy)
        self.mailAddressRadio_label.setMinimumSize(QtCore.QSize(270, 20))
        self.mailAddressRadio_label.setMaximumSize(QtCore.QSize(350, 15))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.mailAddressRadio_label.setFont(font)
        self.mailAddressRadio_label.setStyleSheet("background-color: none;\n"
"padding: 1px;\n"
"")
        self.mailAddressRadio_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mailAddressRadio_label.setObjectName("mailAddressRadio_label")
        self.gridLayout.addWidget(self.mailAddressRadio_label, 10, 3, 1, 1)
        self.ssn_lineEdit = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ssn_lineEdit.sizePolicy().hasHeightForWidth())
        self.ssn_lineEdit.setSizePolicy(sizePolicy)
        self.ssn_lineEdit.setMinimumSize(QtCore.QSize(270, 35))
        self.ssn_lineEdit.setMaximumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.ssn_lineEdit.setFont(font)
        self.ssn_lineEdit.setStyleSheet("border-style: outset;\n"
"border-width: 1.5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.ssn_lineEdit.setMaxLength(30)
        self.ssn_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ssn_lineEdit.setObjectName("ssn_lineEdit")
        self.gridLayout.addWidget(self.ssn_lineEdit, 5, 1, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QtCore.QSize(270, 20))
        self.frame_10.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_10.setStyleSheet("background-color: none;\n"
"")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_5.setContentsMargins(2, 4, 2, 4)
        self.gridLayout_5.setSpacing(2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.mailAddressYes_radioButton = QtWidgets.QRadioButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mailAddressYes_radioButton.sizePolicy().hasHeightForWidth())
        self.mailAddressYes_radioButton.setSizePolicy(sizePolicy)
        self.mailAddressYes_radioButton.setMinimumSize(QtCore.QSize(45, 0))
        self.mailAddressYes_radioButton.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.mailAddressYes_radioButton.setFont(font)
        self.mailAddressYes_radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mailAddressYes_radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mailAddressYes_radioButton.setObjectName("mailAddressYes_radioButton")
        self.gridLayout_5.addWidget(self.mailAddressYes_radioButton, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem140 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem140, 0, 5, 1, 1)
        self.mailAddressNo_radioButton = QtWidgets.QRadioButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mailAddressNo_radioButton.sizePolicy().hasHeightForWidth())
        self.mailAddressNo_radioButton.setSizePolicy(sizePolicy)
        self.mailAddressNo_radioButton.setMinimumSize(QtCore.QSize(45, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.mailAddressNo_radioButton.setFont(font)
        self.mailAddressNo_radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mailAddressNo_radioButton.setObjectName("mailAddressNo_radioButton")
        self.gridLayout_5.addWidget(self.mailAddressNo_radioButton, 0, 4, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem141 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem141, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_10, 11, 3, 2, 1)
        self.ssn_label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ssn_label.sizePolicy().hasHeightForWidth())
        self.ssn_label.setSizePolicy(sizePolicy)
        self.ssn_label.setMinimumSize(QtCore.QSize(270, 15))
        self.ssn_label.setMaximumSize(QtCore.QSize(350, 15))
        font = QtGui.QFont()
        font.setKerning(True)
        self.ssn_label.setFont(font)
        self.ssn_label.setStyleSheet("background-color: none;\n"
"")
        self.ssn_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.ssn_label.setObjectName("ssn_label")
        self.gridLayout.addWidget(self.ssn_label, 4, 1, 1, 1)
        spacerItem142 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem142, 22, 3, 1, 1)
        spacerItem143 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem143, 19, 1, 1, 1)
        spacerItem144 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem144, 19, 0, 1, 1)
        spacerItem145 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem145, 14, 4, 1, 1)
        spacerItem146 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem146, 23, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.userInfo_tabWidget.addTab(self.personalTab, "")
        self.horizontalLayout.addWidget(self.userInfo_tabWidget)
        self.mainScreen_stackedWidget.addWidget(self.userInfoScreen_page1)
        self.reportsScreen_page2 = QtWidgets.QWidget()
        self.reportsScreen_page2.setObjectName("reportsScreen_page2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.reportsScreen_page2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem147 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem147)
        self.reports_label = QtWidgets.QLabel(self.reportsScreen_page2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.reports_label.setFont(font)
        self.reports_label.setAlignment(QtCore.Qt.AlignCenter)
        self.reports_label.setObjectName("reports_label")
        self.verticalLayout_6.addWidget(self.reports_label)
        self.frame_6 = QtWidgets.QFrame(self.reportsScreen_page2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.reportType_label = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.reportType_label.setFont(font)
        self.reportType_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.reportType_label.setObjectName("reportType_label")
        self.horizontalLayout_8.addWidget(self.reportType_label)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.reportTypePay_radioButton = QtWidgets.QRadioButton(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.reportTypePay_radioButton.setFont(font)
        self.reportTypePay_radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reportTypePay_radioButton.setStyleSheet("")
        self.reportTypePay_radioButton.setObjectName("reportTypePay_radioButton")
        self.verticalLayout_5.addWidget(self.reportTypePay_radioButton)
        self.reportTypeFull_radioButton = QtWidgets.QRadioButton(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.reportTypeFull_radioButton.setFont(font)
        self.reportTypeFull_radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reportTypeFull_radioButton.setStyleSheet("")
        self.reportTypeFull_radioButton.setObjectName("reportTypeFull_radioButton")
        self.verticalLayout_5.addWidget(self.reportTypeFull_radioButton)
        self.horizontalLayout_8.addWidget(self.frame_9)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.frame_11 = QtWidgets.QFrame(self.reportsScreen_page2)
        self.frame_11.setStyleSheet("")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.archivedEmployeeReport_checkBox = QtWidgets.QCheckBox(self.frame_11)
        self.archivedEmployeeReport_checkBox.setMinimumSize(QtCore.QSize(340, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.archivedEmployeeReport_checkBox.setFont(font)
        self.archivedEmployeeReport_checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.archivedEmployeeReport_checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.archivedEmployeeReport_checkBox.setStyleSheet("QCheckBox::indicator {\n"
"    height: 14px;\n"
"    width: 14px;\n"
"}\n"
"           ")
        self.archivedEmployeeReport_checkBox.setObjectName("archivedEmployeeReport_checkBox")
        self.horizontalLayout_9.addWidget(self.archivedEmployeeReport_checkBox, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_6.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.reportsScreen_page2)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.generateReport_label = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.generateReport_label.setFont(font)
        self.generateReport_label.setAlignment(QtCore.Qt.AlignCenter)
        self.generateReport_label.setObjectName("generateReport_label")
        self.horizontalLayout_10.addWidget(self.generateReport_label)
        self.generateReport_toolButton = QtWidgets.QToolButton(self.frame_12)
        self.generateReport_toolButton.setMinimumSize(QtCore.QSize(140, 50))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.generateReport_toolButton.setFont(font)
        self.generateReport_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generateReport_toolButton.setStyleSheet("QToolButton {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"background-color: rgb(120, 190, 72);\n"
"color: white;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"padding-top: 6px;\n"
"background-color: rgb(120, 190, 72);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"padding-top: 8px;\n"
"background-color: rgb(90, 160, 42);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgba(0, 0, 0, 70);;\n"
"background-color: rgba(120, 190, 72, 70);\n"
"color: rgba(255, 255, 255, 70);;\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.generateReport_toolButton.setObjectName("generateReport_toolButton")
        self.horizontalLayout_10.addWidget(self.generateReport_toolButton)
        self.verticalLayout_6.addWidget(self.frame_12, 0, QtCore.Qt.AlignHCenter)
        spacerItem148 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem148)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 1)
        self.verticalLayout_6.setStretch(3, 1)
        self.verticalLayout_6.setStretch(4, 1)
        self.verticalLayout_6.setStretch(5, 1)
        self.mainScreen_stackedWidget.addWidget(self.reportsScreen_page2)
        self.verticalLayout_2.addWidget(self.mainScreen_stackedWidget)
        self.horizontalLayout_3.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.mainScreen_stackedWidget.setCurrentIndex(1)
        self.userInfo_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.firstName_lineEdit, self.lastName_lineEdit)
        MainWindow.setTabOrder(self.lastName_lineEdit, self.addressOne_lineEdit)
        MainWindow.setTabOrder(self.addressOne_lineEdit, self.department_lineEdit)
        MainWindow.setTabOrder(self.department_lineEdit, self.title_lineEdit)
        MainWindow.setTabOrder(self.title_lineEdit, self.searchField_comboBox)
        MainWindow.setTabOrder(self.searchField_comboBox, self.search_toolButton)
        MainWindow.setTabOrder(self.search_toolButton, self.newEmp_toolButton)
        MainWindow.setTabOrder(self.newEmp_toolButton, self.info_toolButton)
        MainWindow.setTabOrder(self.info_toolButton, self.userManual_toolButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.closeSideBar_toolButton.setText(_translate("MainWindow", "..."))
        self.collapse_toolButton.setText(_translate("MainWindow", "..."))
        self.search_lineEdit.setPlaceholderText(_translate("MainWindow", "Search"))
        self.searchField_comboBox.setCurrentText(_translate("MainWindow", "Full Name"))
        self.searchField_comboBox.setItemText(0, _translate("MainWindow", "Full Name"))
        self.searchField_comboBox.setItemText(1, _translate("MainWindow", "First Name"))
        self.searchField_comboBox.setItemText(2, _translate("MainWindow", "Last Name"))
        self.searchField_comboBox.setItemText(3, _translate("MainWindow", "Employee ID"))
        self.newEmp_toolButton.setText(_translate("MainWindow", "  Add New Employee"))
        self.report_toolButton.setText(_translate("MainWindow", "  Create Report"))
        self.info_toolButton.setText(_translate("MainWindow", "  My Info"))
        self.userManual_toolButton.setText(_translate("MainWindow", "  User Manual"))
        self.signOut_toolButton.setText(_translate("MainWindow", "  Sign Out"))
        self.hamburger_toolButton.setText(_translate("MainWindow", "..."))
        self.signOutTopBar_toolButton.setText(_translate("MainWindow", "Sign Out"))
        self.firstNameHeader_label.setText(_translate("MainWindow", "First"))
        self.lastNameHeader_label.setText(_translate("MainWindow", "Last"))
        self.titleHeader_label.setText(_translate("MainWindow", "Title"))
        self.departmentHeader_label.setText(_translate("MainWindow", "Department"))
        self.email_label.setText(_translate("MainWindow", "Email"))
        self.lastName_label.setText(_translate("MainWindow", "Last Name"))
        self.addressOne_label.setText(_translate("MainWindow", "Street Address 1"))
        self.phone_label.setText(_translate("MainWindow", "Phone Number"))
        self.startDate_label.setText(_translate("MainWindow", "Start Date"))
        self.city_label.setText(_translate("MainWindow", "City"))
        self.saveGeneral_toolButton.setText(_translate("MainWindow", "SAVE"))
        self.editGeneral_toolButton_3.setText(_translate("MainWindow", "Edit"))
        self.employeeIdGeneral_label.setText(_translate("MainWindow", "Employee ID"))
        self.editGeneral_toolButton.setText(_translate("MainWindow", "Edit"))
        self.state_label.setText(_translate("MainWindow", "State"))
        self.zip_label.setText(_translate("MainWindow", "Zip"))
        self.department_label.setText(_translate("MainWindow", "Department"))
        self.title_label.setText(_translate("MainWindow", "Title"))
        self.firstName_label.setText(_translate("MainWindow", "First Name"))
        self.userInfo_tabWidget.setTabText(self.userInfo_tabWidget.indexOf(self.generalTab), _translate("MainWindow", "General"))
        self.userAccess_label.setText(_translate("MainWindow", "User Access:   "))
        self.userAccess_comboBox.setItemText(1, _translate("MainWindow", "General"))
        self.userAccess_comboBox.setItemText(2, _translate("MainWindow", "Manager"))
        self.userAccess_comboBox.setItemText(3, _translate("MainWindow", "Archived"))
        self.birthDay_label.setText(_translate("MainWindow", "Date of Birth"))
        self.routingNum_label.setText(_translate("MainWindow", "Routing Number"))
        self.editPersonal_toolButton.setText(_translate("MainWindow", "Edit"))
        self.editGeneral_toolButton_4.setText(_translate("MainWindow", "Edit"))
        self.mailAddressState_label.setText(_translate("MainWindow", "State"))
        self.mailAddressOne_label.setText(_translate("MainWindow", "Street Address 1"))
        self.savePersonal_toolButton.setText(_translate("MainWindow", "SAVE"))
        self.directDeposit_label.setText(_translate("MainWindow", "Direct Deposit:   "))
        self.directDepositYes_radioButton.setText(_translate("MainWindow", "Yes"))
        self.directDepositNo_radioButton.setText(_translate("MainWindow", "No"))
        self.mailAddressCity_label.setText(_translate("MainWindow", "City"))
        self.mailAddressZip_label.setText(_translate("MainWindow", "Zip"))
        self.payTypeCommision_radioButton.setText(_translate("MainWindow", "Commissioned"))
        self.payType_label.setText(_translate("MainWindow", "Pay Type:   "))
        self.payTypeSalary_radioButton.setText(_translate("MainWindow", "Salary"))
        self.payTypeHourly_radioButton.setText(_translate("MainWindow", "Hourly"))
        self.employeeIdPersonal_label.setText(_translate("MainWindow", "Employee ID"))
        self.accountNum_label.setText(_translate("MainWindow", "Account Number"))
        self.mailAddressRadio_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Mailing Address is Same as Home Address:</p></body></html>"))
        self.mailAddressYes_radioButton.setText(_translate("MainWindow", "Yes   "))
        self.mailAddressNo_radioButton.setText(_translate("MainWindow", "No"))
        self.ssn_label.setText(_translate("MainWindow", "Social Security Number"))
        self.userInfo_tabWidget.setTabText(self.userInfo_tabWidget.indexOf(self.personalTab), _translate("MainWindow", "Personal"))
        self.reports_label.setText(_translate("MainWindow", "Reports:"))
        self.reportType_label.setText(_translate("MainWindow", "Report Type:   "))
        self.reportTypePay_radioButton.setText(_translate("MainWindow", "Pay Report"))
        self.reportTypeFull_radioButton.setText(_translate("MainWindow", "Employee Database"))
        self.archivedEmployeeReport_checkBox.setText(_translate("MainWindow", "Include Archived Employees:    "))
        self.generateReport_label.setText(_translate("MainWindow", "Generate .CSV Report:      "))
        self.generateReport_toolButton.setText(_translate("MainWindow", "Generate"))
        self.topBar_frame.hide()
