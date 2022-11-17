class Employee:
    def __init__(self, employeeId, fullName, address1, city, state, zip,
                 classification, payMethod, salary, hourly, commission, routingNum, accountNum, birthDay, ssn,
                 startDate, ismanager, isArchived, title, department, phone, email, password):
        self.employeeId = employeeId
        self.firstName = fullName[:fullName.find(" ")]
        self.lastName = fullName[fullName.find(" "):]
        self.address1 = address1
        self.city = city
        self.email = email
        self.phone = phone
        self.state = state
        self.zip = zip
        self.department = department
        self.title = title
        self.startDate = startDate
        self.ssn = ssn
        self.birthDay = birthDay
        self.classification = classification
        self.payMethod = payMethod
        self.salary = salary
        self.hourly = hourly
        self.commission = commission
        self.routingNum = routingNum
        self.accountNum = accountNum
        if ismanager == "2":
            self.isManager = True
        else:
            self.isManager = False
        if isArchived == "0":
            self.isArchived = False
        else:
            self.isArchived = True
        self.password = password
        self.ui = ""

def generateEmployeeObjects():
    with open("employeestest.csv", 'r') as f:
        lines = f.readlines()

        empObjectList = []
        del lines[0]
        for subList in lines:
            lyst = subList.split(",")
            employeeId, fullName, address1, city, state, zip, classification, payMethod, salary, hourly, commission, routingNum, accountNum, birthDay, ssn, startDate, ismanager, isArchived, title, department, phone, email, password = lyst

            empObject = Employee(employeeId, fullName, address1, city, state, zip, classification, payMethod,
            salary, hourly, commission, routingNum, accountNum, birthDay, ssn, startDate,
            ismanager, isArchived, title, department, phone, email, password)
            empObjectList.append(empObject)

    return empObjectList


