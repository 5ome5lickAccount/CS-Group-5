from PyQt5 import QtWidgets
from empDataGraphics import Ui_MainWindow
from empDataLoginGraphics import Ui_LoginWindow
from sessionManager import SessionManager
from payroll import load_employees, login
import sys
from errorWindow import Error_Form


class CentralWindow(QtWidgets.QMainWindow, SessionManager):
    def __init__(self, activeUser, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.activeUser = activeUser

        self.initializeSessionManager(self.ui, self.activeUser)


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loginUi = Ui_LoginWindow()
        self.loginUi.setupUi(self)
        self.activeUser = False

        self.loginUi.login_toolButton.clicked.connect(self.validateLoginInfo)
        load_employees()

    def validateLoginInfo(self):
        userName = self.loginUi.employeeIdLogin_lineEdit.text()
        password = self.loginUi.passwordLogin_lineEdit.text()
        self.activeUser = login(userName, password)

        if self.activeUser is not False:
            self.proceedWithLogin()
            self.loginUi.employeeIdLogin_lineEdit.setText("")
            self.loginUi.passwordLogin_lineEdit.setText("")
        else:
            self.Form = Error_Form()
            self.Pop_up = QtWidgets.QWidget()
            displayText = "\nInvalid Username or Password.\n"            
            self.Form.setupUi(self.Pop_up, displayText)
            self.Pop_up.show()

    def proceedWithLogin(self):
        self.Central = CentralWindow(self.activeUser)
        self.createAccessDependentInterface()
        self.Central.ui.signOut_toolButton.clicked.connect(self.signOutOfMainWindow)
        self.Central.ui.signOutTopBar_toolButton.clicked.connect(self.signOutOfMainWindow)
        self.Central.show()
        self.hide()

    def createAccessDependentInterface(self):
        if self.activeUser.isManager == False:
            self.Central.ui.newEmp_toolButton.hide()
            self.Central.ui.report_toolButton.hide()
        else:
            self.Central.ui.newEmp_toolButton.show()
            self.Central.ui.report_toolButton.show()

    def signOutOfMainWindow(self):
        self.Central.close()
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    CentralLogin = LoginWindow()
    CentralLogin.show()
    try:
        sys.exit(app.exec())
    except:
        pass

main()
