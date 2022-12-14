import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation

import toggleButton


class SideBarMgr():
    def __init__(self, ui):
        self.ui = ui
        self.originalSettings = {}
        self.newSettings = {}
        self.newIconSize = 50
        self.counter = 1

        self.getOriginalSettings()
        self.getButtonNewSettings()


        self.toggle = toggleButton.ToggleButton(self.ui.horizontalLayout_5)
        self.toggle.setChecked(True)
        self.enableTooltips()
        self.toggle.stateChanged.connect(self.toggleToolTips)

    def pushOutSub(self):
        subWidth = self.ui.sideBar_frame.width()
        print("here: ", subWidth)

        if subWidth != 350:
            self.resetOtherWidgets()
            newWidth = 350

            self.animation1 = QPropertyAnimation(self.ui.sideBar_frame, b"minimumWidth")
            self.animation1.setDuration(1)
            self.animation1.setStartValue(subWidth)
            self.animation1.setEndValue(newWidth)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()


    def collapseSub(self):
        subWidth = self.ui.sideBar_frame.width()

        if subWidth > 102:
            self.shrinkOtherWidgets()
            self.increaseButtonSize()
            newWidth = 102

            self.animation1 = QPropertyAnimation(self.ui.sideBar_frame, b"minimumWidth")

            self.animation1.setDuration(250)
            self.animation1.setStartValue(subWidth)
            self.animation1.setEndValue(newWidth)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()
        else:
            self.pushOutSub()

        print("subWidth: ", subWidth)
        print("tool tip: ", self.toggle.width())
        print("tool tip frame: ", self.ui.toolTipToggle_frame.width())
        print("subWidth: ", subWidth)



    def closeSub(self):
        subWidth = self.ui.sideBar_frame.width()
        subHeight = self.ui.sideBar_frame.height()
        if subWidth != 102:
            self.shrinkOtherWidgets()
            self.increaseButtonSize()
        newWidth = 0
        newHeight = 0

        self.animation1 = QPropertyAnimation(self.ui.sideBar_frame, b"minimumWidth")

        self.animation1.setDuration(300)
        self.animation1.setStartValue(subWidth)
        self.animation1.setEndValue(newWidth)
        self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        self.animation1.start()

        self.animation2 = QPropertyAnimation(self.ui.sideBar_frame, b"minimumHeight")

        self.animation2.setDuration(300)
        self.animation2.setStartValue(subHeight)
        self.animation2.setEndValue(newHeight)
        self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        self.animation2.start()
        self.ui.sideBar_frame.hide()
        self.ui.topBar_frame.show()

    def openSub(self):
        subWidth = self.ui.sideBar_frame.width()
        subHeight = self.ui.sideBar_frame.height()
        self.shrinkOtherWidgets()
        self.increaseButtonSize()

        self.ui.topBar_frame.hide()
        self.ui.sideBar_frame.show()


    def shrinkOtherWidgets(self):
        newButtonSize = QtCore.QSize(self.newIconSize + 10, self.newIconSize + 10)
        newLogOutSize = QtCore.QSize(self.newIconSize - 10, self.newIconSize - 10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/png/arrow-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        for index in range(self.ui.searchField_gridLayout.count(), -1, -1):
            item = self.ui.searchField_gridLayout.itemAt(index)
            if isinstance(item, QtWidgets.QSpacerItem):
                item.changeSize(0, 0)

        self.ui.searchField_comboBox.hide()
        self.ui.search_lineEdit.hide()
        self.ui.collapse_toolButton.setIcon(icon)
        self.ui.collapse_horizontalLayout.itemAt(1).changeSize(0, 0)

        self.ui.search_toolButton.setMaximumSize(newButtonSize)
        self.ui.search_toolButton.setMinimumSize(newButtonSize)
        self.ui.search_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.ui.newEmp_toolButton.setMaximumSize(newButtonSize)
        self.ui.newEmp_toolButton.setMinimumSize(newButtonSize)
        self.ui.newEmp_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.ui.report_toolButton.setMaximumSize(newButtonSize)
        self.ui.report_toolButton.setMinimumSize(newButtonSize)
        self.ui.report_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.ui.info_toolButton.setMaximumSize(newButtonSize)
        self.ui.info_toolButton.setMinimumSize(newButtonSize)
        self.ui.info_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.ui.userManual_toolButton.setMaximumSize(newButtonSize)
        self.ui.userManual_toolButton.setMinimumSize(newButtonSize)
        self.ui.userManual_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.ui.signOut_toolButton.setMaximumSize(newLogOutSize)
        self.ui.signOut_toolButton.setMinimumSize(newLogOutSize)
        self.ui.signOut_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.ui.toolTipToggle_frame.hide()


    def increaseButtonSize(self):
        newSize = QtCore.QSize(self.newIconSize, self.newIconSize)
        newSizeLogOut = QtCore.QSize(self.newIconSize - 20, self.newIconSize - 20)

        for widg in self.newSettings:
            thisObj = self.newSettings[widg]["object"]
            thisObj.setStyleSheet(self.newSettings[widg]["style"])
            thisObj.setIconSize(newSize)
            if thisObj.objectName == "signOut_toolButton":
                thisObj.setIconSize(newSizeLogOut)


    def resetOtherWidgets(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/png/arrow-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        for index in range(self.ui.searchField_gridLayout.count(), -1, -1):
            item = self.ui.searchField_gridLayout.itemAt(index)
            if type(item) == QtWidgets.QSpacerItem:
                item.changeSize(40, 20)

        self.ui.searchField_comboBox.show()
        self.ui.search_lineEdit.show()
        self.ui.collapse_toolButton.setIcon(icon)
        self.ui.collapse_horizontalLayout.itemAt(1).changeSize(280, 20)

        self.ui.newEmp_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.ui.report_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.ui.info_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.ui.userManual_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.ui.signOut_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)

        for widg in self.originalSettings:
            thisObj = self.originalSettings[widg]["object"]
            thisObj.setMinimumSize(self.originalSettings[widg]["minSize"])
            thisObj.setMaximumSize(self.originalSettings[widg]["maxSize"])
            thisObj.setStyleSheet(self.originalSettings[widg]["style"])
            if thisObj.objectName() != "searchField_comboBox" and thisObj.objectName() != "search_lineEdit":
                thisObj.setIconSize(self.originalSettings[widg]["iconSize"])

        self.ui.toolTipToggle_frame.show()


    def getOriginalSettings(self):
        sideBarWidgetList = [self.ui.search_lineEdit, self.ui.searchField_comboBox, self.ui.search_toolButton,
                             self.ui.newEmp_toolButton, self.ui.report_toolButton, self.ui.info_toolButton,
                             self.ui.userManual_toolButton, self.ui.signOut_toolButton]

        for widg in sideBarWidgetList:
            text = ""
            iconSize = ""
            if widg.objectName() != "searchField_comboBox":
                text = widg.text()
                if widg.objectName() != "search_lineEdit":
                    iconSize = widg.iconSize()

            self.originalSettings[widg.objectName()] = {
                "object": widg,
                "iconSize": iconSize,
                "text": text,
                "minSize": widg.minimumSize(),
                "maxSize": widg.maximumSize(),
                "style": widg.styleSheet()
            }


    def getButtonNewSettings(self):
        newRadius = str((self.newIconSize + 10) // 2)
        newLogOutRadius = str((self.newIconSize - 10) // 2)
        sideBarWidgetList = [self.ui.search_toolButton, self.ui.newEmp_toolButton, self.ui.report_toolButton,
                             self.ui.info_toolButton, self.ui.userManual_toolButton, self.ui.signOut_toolButton]

        for widg in sideBarWidgetList:
            oldStyle = widg.styleSheet()
            location = oldStyle.find("border-radius:") + 15
            if widg.objectName() == "signOut_toolButton":
                newStyle = oldStyle[:location] + newLogOutRadius + oldStyle[location + 2:]
            else:
                newStyle = oldStyle[:location] + newRadius + oldStyle[location + 2:]
            self.newSettings[widg.objectName()] = {
                "object": widg,
                "style": newStyle
            }

    def toggleToolTips(self):
        if self.toggle.isChecked():
            self.enableTooltips()
        else:
            self.disableTooltips()
    def disableTooltips(self):
        self.ui.closeSideBar_toolButton.setToolTip("")
        self.ui.collapse_toolButton.setToolTip("")
        self.ui.search_lineEdit.setToolTip("")
        self.ui.searchField_comboBox.setToolTip("")
        self.ui.search_toolButton.setToolTip("")
        self.toggle.setToolTip("")
        self.ui.newEmp_toolButton.setToolTip("")
        self.ui.report_toolButton.setToolTip("")
        self.ui.info_toolButton.setToolTip("")
        self.ui.userManual_toolButton.setToolTip("")
        self.ui.signOut_toolButton.setToolTip("")
        self.ui.hamburger_toolButton.setToolTip("")
        self.ui.signOutTopBar_toolButton.setToolTip("")

    def enableTooltips(self):
        self.ui.closeSideBar_toolButton.setToolTip("Close the side bar")
        self.ui.collapse_toolButton.setToolTip("Colapse the side bar")
        self.ui.search_lineEdit.setToolTip("Type employee information for search here")
        self.ui.searchField_comboBox.setToolTip("Select the empoloyee information type")
        self.ui.search_toolButton.setToolTip("Click to search for the employee information entered above")
        self.toggle.setToolTip("Turn hover tips on/off")
        self.ui.newEmp_toolButton.setToolTip("Create a new employee")
        self.ui.report_toolButton.setToolTip("This is the report_toolButton ToolTip")
        self.ui.info_toolButton.setToolTip("Click to view your employee information")
        self.ui.userManual_toolButton.setToolTip("Click to view the program manual")
        self.ui.signOut_toolButton.setToolTip("Log out of your account")
        self.ui.hamburger_toolButton.setToolTip("Reopen the side bar")
        self.ui.signOutTopBar_toolButton.setToolTip("Sign out of your account")

