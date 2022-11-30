from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QFileDialog, QWidget, QApplication, QDialog, QMainWindow, QPushButton, QMessageBox
from payroll import database_report, pay_report
from errorWindow import Error_Form


class InfoScreenInterface():
    def __init__(self, ui, activeUserObject):
        self.ui = ui
        self.activeUser = activeUserObject
        self.selectedUser = ""
        self.Pop_up = QWidget()
        self.Form = Error_Form()
        
        self.ui.mailAddressYes_radioButton.toggled.connect(self.hideMailingAddress)
        self.ui.mailAddressNo_radioButton.toggled.connect(self.showMailingAddress)

    def setSelectedUser(self, selectedUserObject):
        self.selectedUser = selectedUserObject

    def dateToQDate(self, date):
        dateList = date.split("/")
        return QDate(int(dateList[2]), int(dateList[1]), int(dateList[0]))

    def qDateToDate(self,qDate):
        tempDate = qDate.toString("yyyy.M.d")
        dateList = tempDate.split('.')
        date = dateList[2]+'/'+dateList[1]+'/'+dateList[0]
        return date

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

            if self.activeUser.isManager or self.activeUser.employeeId == self.selectedUser.employeeId:
                self.enablePersonalTab()
                self.ui.employeeIdPersonal_lineEdit.setText(self.selectedUser.employeeId)
                self.ui.ssn_lineEdit.setText(self.selectedUser.ssn)
                self.ui.birthDay_dateEdit.setDate(self.dateToQDate(self.selectedUser.birthDay))

                if self.selectedUser.classification == "1":
                    self.ui.payTypeHourly_radioButton.setChecked(True)
                elif self.selectedUser.classification == "2":
                    self.ui.payTypeSalary_radioButton.setChecked(True)
                else:
                     self.ui.payTypeCommision_radioButton.setChecked(True)

                if self.selectedUser.payMethod == "2":
                    self.ui.directDepositYes_radioButton.setChecked(True)
                else:
                    self.ui.directDepositNo_radioButton.setChecked(True)

                if self.selectedUser.isArchived:
                    self.ui.userAccess_comboBox.setCurrentIndex(3)
                elif self.selectedUser.isManager:
                    self.ui.userAccess_comboBox.setCurrentIndex(2)
                elif self.selectedUser.isManager == "":
                    self.ui.userAccess_comboBox.setCurrentIndex(0)
                else:
                    self.ui.userAccess_comboBox.setCurrentIndex(1)

                self.ui.mailAddressYes_radioButton.setChecked(True)
                self.ui.routingNum_lineEdit.setText(self.selectedUser.routingNum)
                self.ui.accountNum_lineEdit.setText(self.selectedUser.accountNum)
                if self.selectedUser.unsavedData and self.selectedUser.unsavedDataFields:
                    displayText = "\nThis user contains empty fields. Consider filling them out.\n"
                    for i in self.selectedUser.unsavedDataFields:
                        displayText+=i+" "
                    
                    self.Form.setupUi(self.Pop_up, displayText)
                    self.Pop_up.show()
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

        if self.activeUser.classification == "1":
            self.ui.payTypeHourly_radioButton.setChecked(True)
        elif self.activeUser.classification == "2":
            self.ui.payTypeSalary_radioButton.setChecked(True)
        else:
                self.ui.payTypeCommision_radioButton.setChecked(True)

        if self.activeUser.payMethod == "2":
            self.ui.directDepositYes_radioButton.setChecked(True)
        else:
            self.ui.directDepositNo_radioButton.setChecked(True)

        if self.activeUser.isArchived:
            self.ui.userAccess_comboBox.setCurrentIndex(3)
        elif self.activeUser.isManager:
            self.ui.userAccess_comboBox.setCurrentIndex(2)
        elif self.activeUser.isManager == "":
            self.ui.userAccess_comboBox.setCurrentIndex(0)
        else:
            self.ui.userAccess_comboBox.setCurrentIndex(1)

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
        self.ui.mailAddressCity_lineEdit.setText("")
        self.ui.mailAddressState_lineEdit.setText("")
        self.ui.mailAddressState_lineEdit.setText("")
        self.resetRadioButtons()

    def disableInfoInputs(self):
        self.ui.employeeIdGeneral_lineEdit.setEnabled(False)
        self.ui.firstName_lineEdit.setEnabled(False)
        self.ui.lastName_lineEdit.setEnabled(False)
        self.ui.addressOne_lineEdit.setEnabled(False)
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
        self.ui.payTypeCommision_radioButton.setEnabled(False)
        self.ui.directDepositYes_radioButton.setEnabled(False)
        self.ui.directDepositNo_radioButton.setEnabled(False)
        self.ui.mailAddressYes_radioButton.setEnabled(False)
        self.ui.mailAddressNo_radioButton.setEnabled(False)
        self.ui.userAccess_comboBox.setEnabled(False)

        self.ui.routingNum_lineEdit.setEnabled(False)
        self.ui.accountNum_lineEdit.setEnabled(False)
        self.ui.mailAddressOne_lineEdit.setEnabled(False)
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
        self.ui.mailAddressCity_lineEdit.setEnabled(True)
        self.ui.mailAddressState_lineEdit.setEnabled(True)
        self.ui.mailAddressZip_lineEdit.setEnabled(True)

        if self.activeUser.isManager:
            self.ui.department_lineEdit.setEnabled(True)
            self.ui.title_lineEdit.setEnabled(True)
            self.ui.startDate_dateEdit.setEnabled(True)
            self.ui.ssn_lineEdit.setEnabled(True)
            self.ui.birthDay_dateEdit.setEnabled(True)
            self.ui.payTypeHourly_radioButton.setEnabled(True)
            self.ui.payTypeSalary_radioButton.setEnabled(True)
            self.ui.payTypeCommision_radioButton.setEnabled(True)
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

    def generateReport(self):
        file = SaveLocation()
        fileName, _ = file.openFileNameDialog()
        archived = self.ui.archivedEmployeeReport_checkBox.isChecked()
        if self.ui.reportTypePay_radioButton.isChecked():
            pay_report(archived, fileName+'.txt')
        else:
            database_report(archived, fileName+'.csv')
    
    def finalCheck(self,emp):
        if not self.checkForEdits(emp):
            return True
        dlg = QMessageBox()
        dlg.setWindowTitle("Unsaved data will be lost")
        dlg.setText("WARNING: There is unsaved data. Are you sure you want to exit without saving your data?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            return True
        else:
            return False
        
    def checkForEdits(self,emp):
        if self.ui.employeeIdGeneral_lineEdit.text() != emp.employeeId:
            return True
        if self.ui.firstName_lineEdit.text() != emp.firstName:
            return True
        if self.ui.lastName_lineEdit.text() != emp.lastName:
            return True
        if self.ui.addressOne_lineEdit.text() != emp.address1:
            return True
        if self.ui.city_lineEdit.text() != emp.city:
            return True
        if self.ui.state_lineEdit.text() != emp.state:
            return True
        if self.ui.zip_lineEdit.text() != emp.zip:
            return True
        if self.ui.email_lineEdit.text() != emp.email:
            return True
        if self.ui.phone_lineEdit.text() != emp.phone:
            return True
        if self.ui.department_lineEdit.text() != emp.department:
            return True
        if self.ui.title_lineEdit.text() != emp.title:
            return True
        if self.ui.startDate_dateEdit.date() != self.dateToQDate(emp.startDate):
            return True
        if self.ui.ssn_lineEdit.text() != emp.ssn:
            return True
        if self.ui.birthDay_dateEdit.date() != self.dateToQDate(emp.birthDay):
            return True
        '''if self.ui.mailAddressYes_radioButton.isChecked() != True:
            return True'''
        if self.ui.routingNum_lineEdit.text() != emp.routingNum:
            return True
        if emp.classification == "1" and not self.ui.payTypeHourly_radioButton.isChecked():
            return True
        if emp.classification == "2" and not self.ui.payTypeSalary_radioButton.isChecked():
            return True
        if emp.payMethod == "1" and not self.ui.directDepositNo_radioButton.isChecked():
            return True
        if emp.payMethod == "2" and not self.ui.directDepositYes_radioButton.isChecked():
            return True
        '''if emp.isArchived  and self.ui.userAccess_comboBox.currentIndex() != 3:
            return True
        elif emp.isManager and self.ui.userAccess_comboBox.currentIndex() != 2:
            return True
        elif emp.isManager == "" and self.ui.userAccess_comboBox.currentIndex() != 0:
            return True
        elif not emp.isManager and self.ui.userAccess_comboBox.currentIndex() != 1:
            return True'''
        return False

    def hideMailingAddress(self):
        self.ui.mailAddressOne_label.hide()
        self.ui.mailAddressOne_lineEdit.hide()
        self.ui.mailAddressCity_label.hide()
        self.ui.mailAddressCity_lineEdit.hide()
        self.ui.mailAddressState_label.hide()
        self.ui.mailAddressState_lineEdit.hide()
        self.ui.mailAddressZip_label.hide()
        self.ui.mailAddressZip_lineEdit.hide()

    def showMailingAddress(self):
        self.ui.mailAddressOne_label.show()
        self.ui.mailAddressOne_lineEdit.show()
        self.ui.mailAddressCity_label.show()
        self.ui.mailAddressCity_lineEdit.show()
        self.ui.mailAddressState_label.show()
        self.ui.mailAddressState_lineEdit.show()
        self.ui.mailAddressZip_label.show()
        self.ui.mailAddressZip_lineEdit.show()
    
class SaveLocation(QWidget):
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Choose File", "","csv (*.csv)", options=options)
        if '.csv' in fileName:
            fileName=fileName[:-5]
        return fileName, _