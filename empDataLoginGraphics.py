# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'empDataLogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(500, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QtCore.QSize(500, 700))
        LoginWindow.setMaximumSize(QtCore.QSize(500, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/png/UVUMonogramGreen-0005.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/icons/assets/png/logo-no-background.png);\n"
"padding: 10px;\n"
"")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.login_frame = QtWidgets.QFrame(self.frame_4)
        self.login_frame.setMaximumSize(QtCore.QSize(600, 275))
        self.login_frame.setStyleSheet("background-color: transparent;\n"
"border-width: 2px;\n"
"border-color: green;\n"
"")
        self.login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setObjectName("login_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.login_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.login_frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 85))
        self.frame_2.setStyleSheet("background-color: transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.employeeIdLogin_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employeeIdLogin_label.sizePolicy().hasHeightForWidth())
        self.employeeIdLogin_label.setSizePolicy(sizePolicy)
        self.employeeIdLogin_label.setMinimumSize(QtCore.QSize(180, 20))
        self.employeeIdLogin_label.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.employeeIdLogin_label.setFont(font)
        self.employeeIdLogin_label.setStyleSheet("color: rgb(180, 180, 180);")
        self.employeeIdLogin_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.employeeIdLogin_label.setObjectName("employeeIdLogin_label")
        self.gridLayout_3.addWidget(self.employeeIdLogin_label, 0, 0, 1, 1)
        self.employeeIdLogin_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.employeeIdLogin_lineEdit.setMinimumSize(QtCore.QSize(300, 40))
        self.employeeIdLogin_lineEdit.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.employeeIdLogin_lineEdit.setFont(font)
        self.employeeIdLogin_lineEdit.setStyleSheet("border-bottom:2px solid black;\n"
"border-top-left-radius :35px;\n"
"border-top-right-radius : 20px;\n"
"border-bottom-left-radius : 0px; \n"
"border-bottom-right-radius : 0px;\n"
"border-color: white;\n"
"color: white")
        self.employeeIdLogin_lineEdit.setText("")
        self.employeeIdLogin_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.employeeIdLogin_lineEdit.setObjectName("employeeIdLogin_lineEdit")
        self.gridLayout_3.addWidget(self.employeeIdLogin_lineEdit, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.login_frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 85))
        self.frame_3.setStyleSheet("background-color: transparent;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.passwordLogin_label = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLogin_label.sizePolicy().hasHeightForWidth())
        self.passwordLogin_label.setSizePolicy(sizePolicy)
        self.passwordLogin_label.setMinimumSize(QtCore.QSize(180, 20))
        self.passwordLogin_label.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.passwordLogin_label.setFont(font)
        self.passwordLogin_label.setStyleSheet("color: rgb(180, 180, 180);")
        self.passwordLogin_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passwordLogin_label.setObjectName("passwordLogin_label")
        self.gridLayout_2.addWidget(self.passwordLogin_label, 0, 0, 1, 1)
        self.passwordLogin_lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.passwordLogin_lineEdit.setMinimumSize(QtCore.QSize(300, 40))
        self.passwordLogin_lineEdit.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.passwordLogin_lineEdit.setFont(font)
        self.passwordLogin_lineEdit.setStyleSheet("border-bottom:2px solid black;\n"
"border-top-left-radius :35px;\n"
"border-top-right-radius : 20px;\n"
"border-bottom-left-radius : 0px; \n"
"border-bottom-right-radius : 0px;\n"
"border-color: white;\n"
"color: white")
        self.passwordLogin_lineEdit.setText("")
        self.passwordLogin_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLogin_lineEdit.setObjectName("passwordLogin_lineEdit")
        self.gridLayout_2.addWidget(self.passwordLogin_lineEdit, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.frame_5 = QtWidgets.QFrame(self.login_frame)
        self.frame_5.setStyleSheet("background-color: transparent;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.login_toolButton = QtWidgets.QToolButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_toolButton.sizePolicy().hasHeightForWidth())
        self.login_toolButton.setSizePolicy(sizePolicy)
        self.login_toolButton.setMinimumSize(QtCore.QSize(300, 40))
        self.login_toolButton.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_toolButton.setFont(font)
        self.login_toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_toolButton.setStyleSheet("QToolButton {\n"
"border-style: solid;\n"
"border-width: 2px;\n"
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
"border-color: rgba(0, 0, 0, 70);\n"
"background-color: rgba(120, 190, 72, 70);\n"
"color: rgba(255, 255, 255, 70);\n"
"padding: 4px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.login_toolButton.setObjectName("login_toolButton")
        self.horizontalLayout_4.addWidget(self.login_toolButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addWidget(self.frame_5)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout_2.addWidget(self.login_frame)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.horizontalLayout.addWidget(self.frame_4)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Employee Data Login"))
        self.employeeIdLogin_label.setText(_translate("LoginWindow", "Employee Id"))
        self.passwordLogin_label.setText(_translate("LoginWindow", "  Password "))
        self.login_toolButton.setText(_translate("LoginWindow", "Login"))
import Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
