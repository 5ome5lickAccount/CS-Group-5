from PyQt5 import QtCore, QtGui, QtWidgets
from empDataGraphics import Ui_MainWindow
from payroll import Employee 
from sessionManager import SessionManager
import sys


class CentralWindow(QtWidgets.QMainWindow, SessionManager):
    def __init__(self, activeUser, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.activeUser = activeUser

        self.initializeSessionManager(self.ui, self.activeUser)

#Put all on backend start up functions 
# class LoginWindow(QtWidgets.QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.loginUi = Ui_LoginWindow()
#         self.loginUi.setupUi(self)


def main():
    # todo delete after connecting to backend
    activeUser = Employee("7777777", "Grayson Pratt", "123 w 456 n", "Orem", "UT", "84057", "2", "2", "40872.60",
                               "57.05", "31", "13255163-4", "104934-8350", "7/11/1984", "123-45-6789",
                               "9/11/2019", "2", "0", "Software Engineer", "Software Engineering", "222-333-4444",
                               "grayson.pratt@uvu.edu", "password")

    app = QtWidgets.QApplication(sys.argv)
    Central = CentralWindow(activeUser)
    Central.show()
    try:
        sys.exit(app.exec())
    except:
        print("Exiting")


main()
