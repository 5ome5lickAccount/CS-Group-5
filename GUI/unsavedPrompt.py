from PyQt5 import QtCore, QtGui, QtWidgets


class Unsaved_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 121)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 90, 71, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 90, 71, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 341, 31))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 311, 16))
        self.label_2.setStyleSheet("color: rgb(200, 0, 0)")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Warning"))
        self.pushButton.setText(_translate("Form", "Yes"))
        self.pushButton_2.setText(_translate("Form", "No"))
        self.label.setText(_translate("Form", "WARNING: There is unsaved data. Are you sure you want to exit without saving your data?"))
        self.label_2.setText(_translate("Form", "Unsaved data will be lost"))
