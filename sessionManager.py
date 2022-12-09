from infoScreenInterface import InfoScreenInterface
from reportScreenInterface import ReportScreenManager
from searchScreenInterface import SearchManager
from sideBarManager import SideBarMgr
from payroll import backendSearcher, Employee, update_employee, add_employee

class SessionManager():
    def __init__(self):
        self.ui = ""
        self.currentUser = ""
        self.managerPermission = ""
        self.mainScreen = ""
        self.infoScreen = ""
        self.reportScreen = ""
        self.originalData = ""

    def initializeSessionManager(self,  ui, currentUserObject):
        self.ui = ui
        self.currentUser = currentUserObject
        self.managerPermission = currentUserObject.isManager
        self.mainScreen = ui.mainScreen_stackedWidget

        self.infoScreen = InfoScreenInterface(self.ui, self.currentUser)
        self.reportScreen = ReportScreenManager(self.ui)
        self.sideBarManager = SideBarMgr(self.ui)
        self.infoScreen.enableTooltips()
        self.reportScreen.enableTooltips()
        self.connectButtons()
        self.firstLogin()

    def connectButtons(self):
        self.ui.collapse_toolButton.clicked.connect(self.sideBarManager.collapseSub)
        self.ui.closeSideBar_toolButton.clicked.connect(self.sideBarManager.closeSub)
        self.ui.hamburger_toolButton.clicked.connect(self.sideBarManager.openSub)
        self.ui.search_toolButton.clicked.connect(self.activateSearchScreen)
        self.ui.newEmp_toolButton.clicked.connect(self.activateNewEmployeeInfoScreen)
        self.ui.report_toolButton.clicked.connect(self.activateReportScreen)
        self.ui.info_toolButton.clicked.connect(self.activateMyInfoScreen)
        # self.ui.userManual_toolButton.clicked.connect(lambda: sideBarButtonClick())
        self.ui.editGeneral_toolButton.clicked.connect(self.infoScreen.startEdit)
        self.ui.editPersonal_toolButton.clicked.connect(self.infoScreen.startEdit)
        self.ui.saveGeneral_toolButton.clicked.connect(self.saveEmployee)
        self.ui.savePersonal_toolButton.clicked.connect(self.saveEmployee)
        self.ui.generateReport_toolButton.clicked.connect(self.infoScreen.generateReport)
        
        '''self.ui.signOut_toolButton.clicked.connect(self.checkForSaveDataOnSignOut)
        self.ui.signOutTopBar_toolButton.clicked.connect(self.checkForSaveDataOnSignOut)

    def checkForSaveDataOnSignOut(self):
        self.saveCheck()'''

    def saveEmployee(self):
        newEmp = self.getUpdatedEmployee()
        if not update_employee(newEmp):
            add_employee(newEmp)
        self.createOriginalData()
        self.infoScreen.disableInfoInputs()
        if newEmp.employeeId == self.infoScreen.activeUser.employeeId: 
            self.infoScreen.activeUser = newEmp

    def firstLogin(self):
        self.activateMyInfoScreen()

    def activateSearchScreen(self):
        if self.saveCheck():
            searchFilter = self.ui.searchField_comboBox.currentText()
            searchText = self.ui.search_lineEdit.text()
            searchResultsList = backendSearcher(searchFilter, searchText)
            SearchManager(self.ui, searchResultsList, self.activateOtherEmployeeInfoScreen).populateSearchResults()
            self.mainScreen.setCurrentIndex(0)
            self.createOriginalData()

    def activateMyInfoScreen(self):
        if self.saveCheck():
            self.infoScreen.myInfoScreenActivate()
            self.mainScreen.setCurrentIndex(1)
            self.createOriginalData()

    def activateOtherEmployeeInfoScreen(self, selectedUser):
        if self.saveCheck():
            self.infoScreen.otherUserInfoScreenActivate(selectedUser)
            self.mainScreen.setCurrentIndex(1)
            self.createOriginalData()

    def activateNewEmployeeInfoScreen(self):
        if self.saveCheck():
            self.infoScreen.clearInfoScreen()
            self.mainScreen.setCurrentIndex(1)
            self.createOriginalData()

    def activateReportScreen(self):
        if self.saveCheck():
            self.reportScreen.clearReportScreen()
            self.mainScreen.setCurrentIndex(2)
            self.originalData = ""

    def saveCheck(self):
        if self.originalData == "":
            return True
        if self.mainScreen.currentIndex() == 1:
            return self.infoScreen.finalCheck(self.originalData)
        return True 

    def createOriginalData(self):
        if self.ui.directDepositNo_radioButton.isChecked():
            payMethod = "1"
        elif self.ui.directDepositYes_radioButton.isChecked():
            payMethod = "2"
        else:
            payMethod = ""
        if self.ui.userAccess_comboBox.currentIndex() != 3:
            isArchived = True
        else:
            isArchived = ""
        if self.ui.userAccess_comboBox.currentIndex() != 2:
            isManager = True
        else:
            isManager = ""
        
        startDate = self.infoScreen.qDateToDate(self.ui.startDate_dateEdit.date())
        birthDate = self.infoScreen.qDateToDate(self.ui.birthDay_dateEdit.date())

        self.originalData = Employee(self.ui.employeeIdGeneral_lineEdit.text(),
        self.ui.firstName_lineEdit.text(),
        self.ui.lastName_lineEdit.text(), #!= emp.lastName
        self.ui.addressOne_lineEdit.text(),# != emp.address1:
        self.ui.city_lineEdit.text(),# != emp.city:
        self.ui.state_lineEdit.text(),# != emp.state:
        self.ui.zip_lineEdit.text(),# != emp.zip:
        payMethod,
        self.ui.routingNum_lineEdit.text(),# != emp.routingNum:
        self.ui.accountNum_lineEdit.text(),
        birthDate,# != self.dateToQDate(emp.birthDay):
        self.ui.ssn_lineEdit.text(),# != emp.ssn:
        startDate,# != self.dateToQDate(emp.startDate):
        isManager,
        isArchived,
        self.ui.title_lineEdit.text(),# != emp.title:
        self.ui.department_lineEdit.text(),# != emp.department:
        self.ui.phone_lineEdit.text(),# != emp.phone:
        self.ui.email_lineEdit.text(),# != emp.email:
        "",#Dont compare Passwords
        0.0,#hourly,salary,commissioned
        0.0,
        0.0
        )
        #TODO: FIX THIS
        if self.ui.payTypeSalary_radioButton.isChecked():
            classification = "2"
        elif self.ui.payTypeHourly_radioButton.isChecked():
            classification = "1"
        elif self.ui.payTypeHourly_radioButton.isChecked():
            classification = "3"
        else:
            classification = ""


    def getUpdatedEmployee(self):
        #if isinstance(self.originalData, Employee):
        #    return
        if self.ui.payTypeSalary_radioButton.isChecked():
            classification = "2"
        elif self.ui.payTypeHourly_radioButton.isChecked():
            classification = "1"
        elif self.ui.payTypeHourly_radioButton.isChecked():
            classification = "3"
        else:
            classification = ""
        if self.ui.directDepositNo_radioButton.isChecked():
            payMethod = "1"
        elif self.ui.directDepositYes_radioButton.isChecked():
            payMethod = "2"
        else:
            payMethod = ""
        if self.ui.userAccess_comboBox.currentIndex() == 3:
            isArchived = True
        else:
            isArchived = ""
        if self.ui.userAccess_comboBox.currentIndex() == 2:
            isManager = True
        else:
            isManager = ""
        
        startDate = self.infoScreen.qDateToDate(self.ui.startDate_dateEdit.date())
        birthDate = self.infoScreen.qDateToDate(self.ui.birthDay_dateEdit.date())

        newEmp = Employee(self.ui.employeeIdGeneral_lineEdit.text(),
        self.ui.firstName_lineEdit.text(),
        self.ui.lastName_lineEdit.text(), #!= emp.lastName
        self.ui.addressOne_lineEdit.text(),# != emp.address1:
        self.ui.city_lineEdit.text(),# != emp.city:
        self.ui.state_lineEdit.text(),# != emp.state:
        self.ui.zip_lineEdit.text(),# != emp.zip:
        payMethod,
        self.ui.routingNum_lineEdit.text(),# != emp.routingNum:
        self.ui.accountNum_lineEdit.text(),
        birthDate,# != self.dateToQDate(emp.birthDay):
        self.ui.ssn_lineEdit.text(),# != emp.ssn:
        startDate,# != self.dateToQDate(emp.startDate):
        isManager,
        isArchived,
        self.ui.title_lineEdit.text(),# != emp.title:
        self.ui.department_lineEdit.text(),# != emp.department:
        self.ui.phone_lineEdit.text(),# != emp.phone:
        self.ui.email_lineEdit.text(),# != emp.email:
        "",#Dont compare Passwords
        0.0,#hourly,salary,commissioned
        0.0,
        0.0
        )
        if self.ui.payTypeSalary_radioButton.isChecked():
            newEmp.classification = "2"
        elif self.ui.payTypeHourly_radioButton.isChecked():
            newEmp.classification = "1"
        elif self.ui.payTypeHourly_radioButton.isChecked():
            newEmp.classification = "3"
        else:
            newEmp.classification = ""
        return newEmp