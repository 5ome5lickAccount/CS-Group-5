class ReportScreenManager:
    def __init__(self, ui):
        self.ui = ui
        self.reportType = ""
        self.includeArchived = False

        self.clearReportScreen()
        self.ui.reportTypePay_radioButton.toggled.connect(self.validateRequiredInfoPresent)
        self.ui.reportTypeFull_radioButton.toggled.connect(self.validateRequiredInfoPresent)
        self.ui.archivedEmployeeReport_checkBox.toggled.connect(self.validateRequiredInfoPresent)


    def clearReportScreen(self):
        self.ui.reportTypePay_radioButton.setAutoExclusive(False)
        self.ui.reportTypePay_radioButton.setChecked(False)
        self.ui.reportTypePay_radioButton.setAutoExclusive(True)

        self.ui.reportTypeFull_radioButton.setAutoExclusive(False)
        self.ui.reportTypeFull_radioButton.setChecked(False)
        self.ui.reportTypeFull_radioButton.setAutoExclusive(True)

        self.ui.archivedEmployeeReport_checkBox.setChecked(False)
        self.ui.generateReport_toolButton.setEnabled(False)

    def validateRequiredInfoPresent(self):
        if self.ui.reportTypePay_radioButton.isChecked() or self.ui.reportTypeFull_radioButton.isChecked():
            self.ui.generateReport_toolButton.setEnabled(True)
