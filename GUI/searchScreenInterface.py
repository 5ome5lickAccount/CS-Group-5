from PyQt5 import QtWidgets, QtCore, QtGui
from empTest import generateEmployeeObjects


class SeparatorLine(QtWidgets.QFrame):
    def __init__(self, indexCounter, container, *args, **kwargs):
        super().__init__()
        self.index = indexCounter
        self.setLineWidth(1)
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        container.addWidget(self, self.index, 0, 1, 5)


class UserSearchResultLabels(QtWidgets.QLabel):
    def __init__(self, container, userInfo, row, column, *args, **kwargs):
        super().__init__()
        self.userInfo = userInfo
        self.row = row
        self.column = column
        self.setMinimumSize(QtCore.QSize(100, 32))
        self.setMaximumSize(QtCore.QSize(250, 32))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.setFont(font)
        self.setStyleSheet("")
        container.addWidget(self, self.row, self.column, 1, 1)
        self.setText(self.userInfo)


class viewUserButtonTemplate(QtWidgets.QToolButton):
    def __init__(self, indexCounter, container, employeeObj, ui, clickFunction, *args, **kwargs):
        super().__init__()
        self.index = indexCounter
        self.employee = employeeObj
        self.ui = ui
        self.container = container
        self.rowCounter = 1
        self.clicked.connect(lambda: clickFunction(self.employee))

        self.setMinimumSize(QtCore.QSize(130, 32))
        self.setMaximumSize(QtCore.QSize(130, 32))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.setFont(font)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("QToolButton {\n"
                           "border-style: none;\n"
                           "color: white;\n"
                           "border-radius: 15px;\n"
                           "padding: 5px;\n"
                           "padding-left: 20px;\n"
                           "padding-right: 10px;\n"
                           "background-color:  rgb(36, 93, 56)\n"
                           "}\n"
                           "\n"
                           "QToolButton:hover {\n"
                           "border-width: 2px;\n"
                           "border-color: white;\n"
                           "background-color: rgb(5, 62, 25)\n"
                           "}\n"
                           "\n"
                           "QToolButton:pressed {\n"
                           "border-style: outset;\n"
                           "border-width: 3px;\n"
                           "border-color: white;\n"
                           "background-color: rgb(0, 50, 13);\n"
                           "}")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/png/view-info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(25, 25))
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        container.addWidget(self, self.index, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.setText("  View")

class SearchManager():
    def __init__(self, ui, searchResultList, viewUserFunction):
        self.ui = ui
        self.container = self.ui.gridLayout_7
        self.viewUserFunction = viewUserFunction
        self.rowCounter = 0
        self.searchResults = searchResultList

    def populateSearchResults(self):
        testEmpList = generateEmployeeObjects()
        self.clearSearchScreen()

        for employee in testEmpList:
            self.populateSearchRow(employee, self.ui)

        for i in range(0, 6):
            self.ui.gridLayout_7.addItem(
                QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding),
                self.rowCounter, i, 1, 1)

    def populateSearchRow(self, employeeObj, ui):
        self.rowCounter += 1
        SeparatorLine(self.rowCounter, self.container)
        self.rowCounter += 1
        viewUserButtonTemplate(self.rowCounter, self.container, employeeObj, ui, self.viewUserFunction)
        userInfoList = [employeeObj.firstName, employeeObj.lastName, employeeObj.title, employeeObj.department]
        for i in range(len(userInfoList)):
            userInfo = userInfoList[i]
            UserSearchResultLabels(self.container, userInfo, self.rowCounter, i + 1)

    def clearSearchScreen(self):
        for i in range(self.ui.gridLayout_7.count() - 1, 4, -1):
            item = self.ui.gridLayout_7.itemAt(i)
            if item.widget() != None:
                item.widget().deleteLater()
