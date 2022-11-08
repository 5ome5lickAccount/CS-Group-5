import abc
import os
from stat import SF_SNAPSHOT
from copy import deepcopy

from numpy import double
class Employee:
    def __init__(self,emp_id,first_name,last_name,address,city,state,zipcode,pay_method,route,account,dob,ssn,start_date,is_manager,is_archived,emp_title,department,office_phone,office_email,password,hourly,salary,commissioned) -> None:
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = False
        self.pay_method = pay_method
        self.route = route
        self.account = account
        self.dob = dob
        self.ssn = ssn
        self.start_date = start_date
        self.is_manager = is_manager
        self.is_archived = is_archived
        self.emp_title = emp_title
        self.department = department
        self.office_phone = office_phone
        self.office_email = office_email
        self.password=password[0:-1]
        #Need this to save them
        self.save_hr = deepcopy(hourly)
        self.save_sal = deepcopy(salary)
        self.save_com = deepcopy(commissioned)
    def make_hourly(self,rate):
        self.classification=Hourly(rate)
    def make_salaried(self,salary):
        self.classification=Salaried(salary)
    def make_commissioned(self,salary,rate):
        self.classification=Commissioned(salary,rate)
    def issue_payment(self, save_file):
        pay = self.classification.compute_pay()
        '''
        Mailing 5599.44 to Issie Scholard at 11 Texas Court Columbia Missouri 65218
        '''
        if pay == 0.0:
            return
        if self.pay_method == 1:
            s=f'Mailing {pay} to {self.first_name} {self.last_name} at {self.address} {self.city} {self.state} {self.zipcode}\n'
        elif self.pay_method == 2:
            s=f'Sending a direct deposit of {pay} to {self.first_name} {self.last_name} at {self.account} with routing number {self.route}\n'
        with open(save_file,'a') as f:
            f.write(s)
    def __str__(self):
        if isinstance(self.classification,  Hourly):
            classification = 1
        elif isinstance(self.classification, Commissioned):
            classification = 3
        elif isinstance(self.classification, Salaried):
            classification = 2
        else:
            classification = 4
        if self.is_archived:
            archive = 1
        else:
            archive = 0
        if self.is_manager:
            manager = 1
        else:
            manager = 0
        detail = self.emp_id+','+self.first_name+' '+self.last_name+','+self.address+','+self.city+','+self.state+','
        detail += self.zipcode+','+str(classification)+','+str(self.pay_method)+','+str(self.save_sal)+','+str(self.save_hr)+','+str(self.save_com)+','
        detail += self.route+','+self.account+','+self.dob+','+self.ssn+','+self.start_date+','+str(manager)+','
        detail += str(archive)+','+self.emp_title+','+self.department+','+self.office_phone+','+self.office_email+','+self.password
        return detail
    
class Classification(abc.ABC):
    @abc.abstractmethod
    def compute_pay(self):
        pass
class Hourly(Classification):
    def __init__(self,hourly_rate) -> None:
        self.hourly_rate=hourly_rate
        self.time_cards=[]
    def add_timecard(self,time):
        self.time_cards.append(time)
    def compute_pay(self):
        hours=0
        for card in self.time_cards:
            hours+=card
        self.time_cards=[]
        return round(self.hourly_rate*hours,2)
class Salaried(Classification):
    def __init__(self,salary) -> None:
        self.salary = salary
    def compute_pay(self):
        return round(self.salary/24, 2)
class Commissioned(Salaried):
    def __init__(self, salary, commission_rate) -> None:
        super().__init__(salary)
        self.commission_rate = commission_rate
        self.receipts_list=[]
    def add_receipt(self,receipt):
        self.receipts_list.append(receipt)
    def compute_pay(self):
        hours = 0
        for rec in self.receipts_list:
            hours+=rec
        self.receipts_list=[]
        sal = self.salary/24
        r = self.commission_rate*hours/100.0
        return round(sal + r,2)


############################################
#
# Global Variables
#
###########################################
PAY_LOGFILE = 'payroll.txt'
#EMPLOYEE_FILE = "employees.csv"
EMPLOYEE_FILE = "employeestest.csv"
employees = []
employees_by_id = {}
current_user = None


###########################################
#
#Functions
#
###########################################

def find_employee_by_id(id):
    for emp in employees:
        if emp.emp_id==id:
            return emp
def load_employees():
    '''
    id,full name,address,city,state,zip,classification,paymethod,salary,commission,hourly,Route,Account,DOB,SSN,StartDate,RoutingNum,AcctNum,IsManager,IsArchived,EmpTitle,Department,OfficePhone,OfficeEmail,Password
    51-4678119,Issie,Scholard,11 Texas Court,Columbia,Missouri,65218,3,134386.51,34,91.06
    '''
    global employees
    if len(employees) != 0:
        employees = []
    filename=EMPLOYEE_FILE
    with open(filename,'r') as f:
        lines=f.readlines()
        lines.pop(0)
        for line in lines:
            line=line.split(',')
            id=line[0]
            first_name=line[1].split(' ')[0]
            if len(line[1].split(' ')) > 2:
                first_name+=' '+line[1].split(' ')[1]
            last_name=line[1].split(' ')[-1]
            address=line[2]
            city=line[3]
            state=line[4]
            zip=line[5]
            classification = int(line[6])

            #PayMethod - identify how this should be tracked what it is for
            pay_method=int(line[7])

            salary=float(line[8])
            commission=float(line[10])
            hourly=float(line[9])
            
            route=line[11]
            account=line[12]
            dob=line[13]
            ssn=line[14]
            start_date=line[15]
            is_manager=bool(int(line[16]))
            is_archived=bool(int(line[17]))
            emp_title=line[18]
            department=line[19]
            office_phone=line[20]
            office_email=line[21]
            password=line[22]
            x=Employee(id,first_name,last_name,address,city,state,zip,pay_method,route,account,dob,ssn,start_date,is_manager,is_archived,emp_title,department,office_phone,office_email,password,hourly,salary,commission)
            if classification==1:
                x.make_hourly(hourly)
            elif classification==2:
                x.make_salaried(salary)
            elif classification==3:
                x.make_commissioned(salary,commission)
            else:
                print('classification error:')
                print(classification)
            employees.append(x)
            employees_by_id[x.emp_id] = x

def process_timecards():
    '''
    51-4678119,7.6,3.1,1.4,4.1,6.4,7.7,6.6
    '''
    filename='timecards.csv'
    with open(filename,'r') as f:
        lines=f.readlines()
        for line in lines:
            line=line.split(',')
            id=line[0]
            line.pop(0)
            employee=find_employee_by_id(id)
            assert isinstance(employee,Employee)
            for card in line:
                try: 
                    employee.classification.add_timecard(int(card))
                except:
                    pass
                    # print(f'employee {id} is not hourly')
def process_receipts():
    filename='receipts.csv'
    with open(filename,'r') as f:
        lines=f.readlines()
        for line in lines:
            line=line.split(',')
            id=line[0]
            line.pop(0)
            employee=find_employee_by_id(id)
            assert isinstance(employee,Employee)
            for card in line:
                try: 
                    employee.classification.add_receipt(int(card))
                except:
                    pass
                    #print(f'employee {id} is not commissioned')
                
def run_payroll(include_archived, save_file):
    if os.path.exists(save_file): # pay_log_file is a global variable holding ‘payroll.txt’ 
        os.remove(save_file) 
    for emp in employees:      # employees is the global list of Employee objects 
        if include_archived:
            emp.issue_payment()
        elif emp.is_archived is False:
            emp.issue_payment()        # issue_payment calls a method in the classification 
      # object to compute the pay

#################
#New Functions
#################

def update_file():
    if os.path.exists(EMPLOYEE_FILE): # pay_log_file is a global variable holding ‘payroll.txt’ 
        os.remove(EMPLOYEE_FILE) 
    with open(EMPLOYEE_FILE, 'w') as fout:
        fout.write("ID,Name,Address,City,State,Zip,Classification,PayMethod,Salary,Hourly,Commission,Route,Account,DOB,SSN,StartDate,IsManager,IsArchived,EmpTitle,Department,OfficePhone,OfficeEmail,Password")
        fout.write("\n")
        for emp in employees:
            fout.write(str(emp))
            fout.write('\n')

def search_full_name(term):
    term = term.lower()
    results = []
    if ' ' not in term:
        results = search_first_name(term)
        results += search_last_name(term)
        return results
    for emp in employees:
        fullname = (emp.first_name).lower() + " " + (emp.last_name).lower()
        if term in fullname:
            results.append(deepcopy(emp))
    return results

def search_first_name(term):
    results = []
    for emp in employees:
        if term.lower() in (emp.first_name).lower():
            results.append(deepcopy(emp))
    return results

def search_last_name(term):
    results = []
    for emp in employees:
        if term.lower() in (emp.last_name).lower():
            results.append(deepcopy(emp))
    return results

def search_id(term):
    if str(term) in employees_by_id.keys():
        return [deepcopy(employees_by_id[str(term)])]    
    
def update_employee(new_emp):
    overwrite_emp = find_employee_by_id(new_emp.emp_id)
    if overwrite_emp is None:
        return False
    if overwrite_emp.ssn != new_emp.ssn:
        return False
    overwrite_emp.first_name = new_emp.first_name
    overwrite_emp.last_name = new_emp.last_name
    overwrite_emp.address = new_emp.address
    overwrite_emp.city = new_emp.city
    overwrite_emp.state = new_emp.state
    overwrite_emp.zipcode = new_emp.zipcode
    overwrite_emp.classification = new_emp.classification
    overwrite_emp.pay_method = new_emp.pay_method
    overwrite_emp.route = new_emp.route
    overwrite_emp.account = new_emp.account
    overwrite_emp.dob = new_emp.dob
    overwrite_emp.start_date = new_emp.start_date
    overwrite_emp.is_manager = new_emp.is_manager
    overwrite_emp.is_archived = new_emp.is_archived
    overwrite_emp.emp_title = new_emp.emp_title
    overwrite_emp.department = new_emp.department
    overwrite_emp.office_phone = new_emp.office_phone
    overwrite_emp.office_email = new_emp.office_email
    update_file()
    return True

def validate_fields(emp):
    problem_fields = []
    
    def validate_ssn(ssn_fields):
        ssn = ssn_fields.split('-')
        if len(ssn) != 3:
            return False
        if len(ssn[0]) != 3:
            return False
        elif len(ssn[1]) != 2:
            return False
        elif len(ssn[2]) != 4:
            return False
        return True

    def validate_no_commas(emp): #Confirms no commas are found # No special characters#Numbers only have numbers potential dashes,slashes
        bad_fields = []
        if ',' in emp.first_name:
            bad_fields.append('First Name')
        if ',' in emp.last_name:
            bad_fields.append('Last Name')
        if ',' in emp.address:
            bad_fields.append('Address')
        if ',' in emp.city:
            bad_fields.append('City')
        if ',' in emp.state:
            bad_fields.append('State')
        if ',' in emp.zipcode:
            bad_fields.append('Zipcode')
        if ',' in emp.route:
            bad_fields.append('Route')
        if ',' in emp.account:
            bad_fields.append('Account')
        if ',' in emp.dob:
            bad_fields.append('Date of Birth')
        if ',' in emp.ssn:
            bad_fields.append('SSN')
        if ',' in emp.dob:
            bad_fields.append('Date of Birth')
        if ',' in emp.start_date:
            bad_fields.append('Start Date')
        if ',' in emp.emp_title:
            bad_fields.append('Employee Title')
        if ',' in emp.department:
            bad_fields.append('Department')
        if ',' in emp.office_email:
            bad_fields.append('Office Email')
        return bad_fields

    if not validate_ssn(emp.ssn):
        problem_fields.append("SSN")

    problems_fields += validate_no_commas(emp)

    return problem_fields

def login(id, password):
    if id in employees_by_id.keys():
        if employees_by_id[id].password == password:
            current_user = employees_by_id[id]
            return deepcopy(current_user)
    return False

def logout():
    current_user = None
    update_file()
    return True

def pay_report(include_archived, save_file):
    if current_user.is_manager is False:
        return False #Change this later when determined better way to send this error
    process_timecards()
    process_receipts()
    run_payroll(include_archived, save_file)


def database_report(include_archived, save_file): #Just output as if to the save file... but to another file
    if current_user.isManager is False:
        return False #Change this later when determined better way to send this error
    if os.path.exists(save_file): # pay_log_file is a global variable holding ‘payroll.txt’ 
        os.remove(save_file) 
    with open(save_file, 'w') as fout:
        fout.write("ID,Name,Address,City,State,Zip,Classification,PayMethod,Salary,Hourly,Commission,Route,Account,DOB,SSN,StartDate,IsManager,IsArchived,EmpTitle,Department,OfficePhone,OfficeEmail,Password")
        fout.write("\n")
        for emp in employees or emp.is_archived is False:
            if include_archived:
                fout.write(str(emp))
                fout.write('\n')
            elif emp.is_archived:
                    continue

def add_employee(new_emp): #can only be called by manager - and will throw error if non manager user is currently active
    if current_user.is_manager is False:
        return False #Change this later when determined better way to send this error
    #validate fields
    employees.append(new_emp)
    employees_by_id[new_emp.emp_id] = new_emp

