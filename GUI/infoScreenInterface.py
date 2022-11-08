from PyQt5.QtCore import QDate


class InfoScreenInterface():
    def __init__(self, ui, activeUserObject):
        self.ui = ui
        self.activeUser = activeUserObject
        self.selectedUser = ""

    def setSelectedUser(self, selectedUserObject):
        self.selectedUser = selectedUserObject

    def dateToQDate(self, date):
        dateList = date.split("/")
        return QDate(int(dateList[2]), int(dateList[1]), int(dateList[0]))

    def fillOutPageWithOtherUser(self):
        if isinstance(type(self.selectedUser), object):
            self.ui.employeeIdGeneral_lineEdit.setText(self.selectedUser.employeeId)
            self.ui.firstName_lineEdit.setText(self.selectedUser.firstName)
            self.ui.lastName_lineEdit.setText(self.selectedUser.lastName)
            self.ui.addressOne_lineEdit.setText(self.selectedUser.address1)
            self.ui.city_lineEdit.setText(self.selectedUser.city)
            self.ui.state_lineEdit.setText(self.selectedUser.state)
            self.ui.zip_lineEdit.setText(self.selectedUser.zip)
            self.ui.email_lineEdit.setText(self.selectedUser.email)
            self.ui.phone_lineEdit.setText(self.selectedUser.phone)
            self.ui.department_lineEdit.setText(self.selectedUser.department)
            self.ui.title_lineEdit.setText(self.selectedUser.title)
            self.ui.startDate_dateEdit.setDate(self.dateToQDate(self.selectedUser.startDate))

            if self.activeUser.isManager:
                self.enablePersonalTab()
                self.ui.employeeIdPersonal_lineEdit.setText(self.selectedUser.employeeId)
                self.ui.ssn_lineEdit.setText(self.selectedUser.ssn)
                self.ui.birthDay_dateEdit.setDate(self.dateToQDate(self.selectedUser.birthDay))

                if self.selectedUser.payMethod == "2":
                    self.ui.payTypeHourly_radioButton.setChecked(True)
                else:
                    self.ui.payTypeSalary_radioButton.setChecked(True)

                if self.selectedUser.payMethod == "2":
                    self.ui.directDepositYes_radioButton.setChecked(True)
                else:
                    self.ui.directDepositNo_radioButton.setChecked(True)

                if self.selectedUser.isArchived:
                    self.ui.userAccess_comboBox.setCurrentIndex(3)
                elif self.selectedUser.isManager:
                    self.ui.userAccess_comboBox.setCurrentIndex(2)
                else:
                    self.ui.userAccess_comboBox.setCurrentIndex(2)

                self.ui.mailAddressYes_radioButton.setChecked(True)
                self.ui.routingNum_lineEdit.setText(self.selectedUser.routingNum)
                self.ui.accountNum_lineEdit.setText(self.selectedUser.accountNum)
            else:
                self.disablePersonalTab()

    def fillOutPageWithActiveUser(self):
        self.enablePersonalTab()

        self.ui.employeeIdGeneral_lineEdit.setText(self.activeUser.employeeId)
        self.ui.firstName_lineEdit.setText(self.activeUser.firstName)
        self.ui.lastName_lineEdit.setText(self.activeUser.lastName)
        self.ui.addressOne_lineEdit.setText(self.activeUser.address1)
        self.ui.city_lineEdit.setText(self.activeUser.city)
        self.ui.state_lineEdit.setText(self.activeUser.state)
        self.ui.zip_lineEdit.setText(self.activeUser.zip)
        self.ui.email_lineEdit.setText(self.activeUser.email)
        self.ui.phone_lineEdit.setText(self.activeUser.phone)
        self.ui.department_lineEdit.setText(self.activeUser.department)
        self.ui.title_lineEdit.setText(self.activeUser.title)
        self.ui.startDate_dateEdit.setDate(self.dateToQDate(self.activeUser.startDate))
        self.ui.employeeIdPersonal_lineEdit.setText(self.activeUser.employeeId)
        self.ui.ssn_lineEdit.setText(self.activeUser.ssn)
        self.ui.birthDay_dateEdit.setDate(self.dateToQDate(self.activeUser.birthDay))
        self.ui.mailAddressYes_radioButton.setChecked(True)
        self.ui.routingNum_lineEdit.setText(self.activeUser.routingNum)
        self.ui.accountNum_lineEdit.setText(self.activeUser.accountNum)

        if self.activeUser.payMethod == "2":
            self.ui.payTypeHourly_radioButton.setChecked(True)
        else:
            self.ui.payTypeSalary_radioButton.setChecked(True)

        if self.activeUser.payMethod == "2":
            self.ui.directDepositYes_radioButton.setChecked(True)
        else:
            self.ui.directDepositNo_radioButton.setChecked(True)

        if self.activeUser.isArchived:
            self.ui.userAccess_comboBox.setCurrentIndex(3)
        elif self.activeUser.isManager:
            self.ui.userAccess_comboBox.setCurrentIndex(2)
        else:
            self.ui.userAccess_comboBox.setCurrentIndex(2)

    def clearInfoScreen(self):
        self.enableInfoInputs()
        self.ui.employeeIdGeneral_lineEdit.setText("")
        self.ui.firstName_lineEdit.setText("")
        self.ui.lastName_lineEdit.setText("")
        self.ui.addressOne_lineEdit.setText("")
        self.ui.city_lineEdit.setText("")
        self.ui.state_lineEdit.setText("")
        self.ui.zip_lineEdit.setText("")
        self.ui.email_lineEdit.setText("")
        self.ui.phone_lineEdit.setText("")
        self.ui.department_lineEdit.setText("")
        self.ui.title_lineEdit.setText("")
        self.ui.startDate_dateEdit.setDate(QDate(2000, 1, 1))
        self.ui.employeeIdPersonal_lineEdit.setText("")
        self.ui.ssn_lineEdit.setText("")
        self.ui.birthDay_dateEdit.setDate(QDate(2000, 1, 1))
        self.ui.userAccess_comboBox.setCurrentIndex(0)
        self.ui.routingNum_lineEdit.setText("")
        self.ui.accountNum_lineEdit.setText("")
        self.ui.mailAddressOne_lineEdit.setText("")
        self.ui.mailAddressTwo_lineEdit.setText("")
        self.ui.mailAddressCity_lineEdit.setText("")
        self.ui.mailAddressState_lineEdit.setText("")
        self.ui.mailAddressState_lineEdit.setText("")
        self.resetRadioButtons()

    def disableInfoInputs(self):
        self.ui.employeeIdGeneral_lineEdit.setEnabled(False)
        self.ui.firstName_lineEdit.setEnabled(False)
        self.ui.lastName_lineEdit.setEnabled(False)
        self.ui.addressOne_lineEdit.setEnabled(False)
        self.ui.addressTwo_lineEdit.setEnabled(False)
        self.ui.city_lineEdit.setEnabled(False)
        self.ui.state_lineEdit.setEnabled(False)
        self.ui.zip_lineEdit.setEnabled(False)
        self.ui.email_lineEdit.setEnabled(False)
        self.ui.phone_lineEdit.setEnabled(False)
        self.ui.department_lineEdit.setEnabled(False)
        self.ui.title_lineEdit.setEnabled(False)
        self.ui.startDate_dateEdit.setEnabled(False)
        self.ui.employeeIdPersonal_lineEdit.setEnabled(False)
        self.ui.ssn_lineEdit.setEnabled(False)
        self.ui.birthDay_dateEdit.setEnabled(False)

        self.ui.payTypeHourly_radioButton.setEnabled(False)
        self.ui.payTypeSalary_radioButton.setEnabled(False)
        self.ui.directDepositYes_radioButton.setEnabled(False)
        self.ui.directDepositNo_radioButton.setEnabled(False)
        self.ui.mailAddressYes_radioButton.setEnabled(False)
        self.ui.mailAddressNo_radioButton.setEnabled(False)
        self.ui.userAccess_comboBox.setEnabled(False)

        self.ui.routingNum_lineEdit.setEnabled(False)
        self.ui.accountNum_lineEdit.setEnabled(False)
        self.ui.mailAddressOne_lineEdit.setEnabled(False)
        self.ui.mailAddressTwo_lineEdit.setEnabled(False)
        self.ui.mailAddressCity_lineEdit.setEnabled(False)
        self.ui.mailAddressState_lineEdit.setEnabled(False)
        self.ui.mailAddressZip_lineEdit.setEnabled(False)

        self.ui.editGeneral_toolButton.setEnabled(True)
        self.ui.editPersonal_toolButton.setEnabled(True)
        self.ui.saveGeneral_toolButton.setEnabled(False)
        self.ui.savePersonal_toolButton.setEnabled(False)

    def enableInfoInputs(self):
        self.ui.firstName_lineEdit.setEnabled(True)
        self.ui.lastName_lineEdit.setEnabled(True)
        self.ui.addressOne_lineEdit.setEnabled(True)
        self.ui.addressTwo_lineEdit.setEnabled(True)
        self.ui.city_lineEdit.setEnabled(True)
        self.ui.state_lineEdit.setEnabled(True)
        self.ui.zip_lineEdit.setEnabled(True)
        self.ui.email_lineEdit.setEnabled(True)
        self.ui.phone_lineEdit.setEnabled(True)
        self.ui.directDepositYes_radioButton.setEnabled(True)
        self.ui.directDepositNo_radioButton.setEnabled(True)
        self.ui.mailAddressYes_radioButton.setEnabled(True)
        self.ui.mailAddressNo_radioButton.setEnabled(True)
        self.ui.routingNum_lineEdit.setEnabled(True)
        self.ui.accountNum_lineEdit.setEnabled(True)
        self.ui.mailAddressOne_lineEdit.setEnabled(True)
        self.ui.mailAddressTwo_lineEdit.setEnabled(True)
        self.ui.mailAddressCity_lineEdit.setEnabled(True)
        self.ui.mailAddressState_lineEdit.setEnabled(True)
        self.ui.mailAddressZip_lineEdit.setEnabled(True)

        if self.activeUser.isManager:
            self.ui.department_lineEdit.setEnabled(True)
            self.ui.title_lineEdit.setEnabled(True)
            self.ui.startDate_dateEdit.setEnabled(True)
            self.ui.employeeIdPersonal_lineEdit.setEnabled(True)
            self.ui.employeeIdGeneral_lineEdit.setEnabled(True)
            self.ui.ssn_lineEdit.setEnabled(True)
            self.ui.birthDay_dateEdit.setEnabled(True)
            self.ui.payTypeHourly_radioButton.setEnabled(True)
            self.ui.payTypeSalary_radioButton.setEnabled(True)
            self.ui.userAccess_comboBox.setEnabled(True)

        self.ui.editGeneral_toolButton.setEnabled(False)
        self.ui.editPersonal_toolButton.setEnabled(False)
        self.ui.saveGeneral_toolButton.setEnabled(True)
        self.ui.savePersonal_toolButton.setEnabled(True)

    def myInfoScreenActivate(self):
        self.clearInfoScreen()
        self.fillOutPageWithActiveUser()
        self.disableInfoInputs()

    def otherUserInfoScreenActivate(self, selectedUser):
        self.clearInfoScreen()
        self.setSelectedUser(selectedUser)
        self.fillOutPageWithOtherUser()
        self.disableInfoInputs()

    def disablePersonalTab(self):
        self.ui.userInfo_tabWidget.setCurrentIndex(0)
        self.ui.userInfo_tabWidget.setTabEnabled(1, False)

    def enablePersonalTab(self):
        self.ui.userInfo_tabWidget.setCurrentIndex(0)
        self.ui.userInfo_tabWidget.setTabEnabled(1, True)

    def resetRadioButtons(self):
        buttonList = [self.ui.payTypeHourly_radioButton, self.ui.payTypeSalary_radioButton, self.ui.directDepositYes_radioButton,
                      self.ui.directDepositNo_radioButton, self.ui.mailAddressYes_radioButton, self.ui.mailAddressNo_radioButton]
        for button in buttonList:
            button.setAutoExclusive(False)
            button.setChecked(False)
            button.setAutoExclusive(True)

    def startEdit(self):
        self.enableInfoInputs()