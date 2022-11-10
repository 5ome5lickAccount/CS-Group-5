from infoScreenInterface import InfoScreenInterface
from reportScreenInterface import ReportScreenManager
from searchScreenInterface import SearchManager
from sideBarManager import SideBarMgr
from payroll import backendSearcher


class SessionManager():
    def __init__(self):
        self.ui = ""
        self.currentUser = ""
        self.managerPermission = ""
        self.mainScreen = ""
        self.infoScreen = ""
        self.reportScreen = ""

    def initializeSessionManager(self,  ui, currentUserObject):
        self.ui = ui
        self.currentUser = currentUserObject
        self.managerPermission = currentUserObject.isManager
        self.mainScreen = ui.mainScreen_stackedWidget

        self.infoScreen = InfoScreenInterface(self.ui, self.currentUser)
        self.reportScreen = ReportScreenManager(self.ui)
        self.sideBarManager = SideBarMgr(self.ui)
        self.connectButtons()
        self.firstLogin()

    def connectButtons(self):
        self.ui.collapse_toolButton.clicked.connect(self.sideBarManager.collapseSub)
        self.ui.search_toolButton.clicked.connect(self.activateSearchScreen)
        self.ui.newEmp_toolButton.clicked.connect(self.activateNewEmployeeInfoScreen)
        self.ui.report_toolButton.clicked.connect(self.activateReportScreen)
        self.ui.info_toolButton.clicked.connect(self.activateMyInfoScreen)
        # self.ui.userManual_toolButton.clicked.connect(lambda: sideBarButtonClick())
        # self.ui.signOut_toolButton.clicked.connect(lambda: sideBarButtonClick())

        self.ui.editGeneral_toolButton.clicked.connect(self.infoScreen.startEdit)
        self.ui.editPersonal_toolButton.clicked.connect(self.infoScreen.startEdit)
        # self.ui.saveGeneral_toolButton.clicked.connect(self.infoScreen.startEdit)
        # self.ui.savePersonal_toolButton.clicked.connect(self.infoScreen.startEdit)
        self.ui.generateReport_toolButton.clicked.connect(self.infoScreen.generateReport)

    def firstLogin(self):
        self.activateMyInfoScreen()

    def activateSearchScreen(self):
        searchFilter = self.ui.searchField_comboBox.currentText()
        searchText = self.ui.search_lineEdit.text()
        searchResultsList = backendSearcher(searchFilter, searchText)
        SearchManager(self.ui, searchResultsList, self.activateOtherEmployeeInfoScreen).populateSearchResults()
        self.mainScreen.setCurrentIndex(0)

    def activateMyInfoScreen(self):
        self.infoScreen.myInfoScreenActivate()
        self.mainScreen.setCurrentIndex(1)

    def activateOtherEmployeeInfoScreen(self, selectedUser):
        self.infoScreen.otherUserInfoScreenActivate(selectedUser)
        self.mainScreen.setCurrentIndex(1)

    def activateNewEmployeeInfoScreen(self):
        self.infoScreen.clearInfoScreen()
        self.mainScreen.setCurrentIndex(1)

    def activateReportScreen(self):
        self.reportScreen.clearReportScreen()
        self.mainScreen.setCurrentIndex(2)

