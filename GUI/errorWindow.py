from PyQt5 import QtCore, QtGui, QtWidgets


class Error_Form(object):
    def setupUi(self, Form, displayText):
        Form.setObjectName("Form")
        Form.resize(400, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 90, 71, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 321, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton.clicked.connect(Form.close)

        self.retranslateUi(Form, displayText)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, displayText):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ERROR"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.label.setText(_translate("Form", displayText))