
import abc
import os
class Employee:
    def __init__(self,emp_id,first_name,last_name,address,city,state,zipcode) -> None:
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = False
    def make_hourly(self,rate):
        self.classification=Hourly(rate)
    def make_salaried(self,salary):
        self.classification=Salaried(salary)
    def make_commissioned(self,salary,rate):
        self.classification=Commissioned(salary,rate)
    def issue_payment(self):
        pay = self.classification.compute_pay()
        '''
        Mailing 5599.44 to Issie Scholard at 11 Texas Court Columbia Missouri 65218
        '''
        s=f'Mailing {pay} to {self.first_name} {self.last_name} at {self.address} {self.city} {self.state} {self.zipcode}\n'
        with open(PAY_LOGFILE,'a') as f:
            f.write(s)
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

PAY_LOGFILE = 'payroll.txt'
pay_logfile = 'payroll.txt'
employees = []

def find_employee_by_id(id):
    for emp in employees:
        if emp.emp_id==id:
            return emp
def load_employees():
    '''
    id,first_name,last_name,address,city,state,zip,classification,salary,commission,hourly
    51-4678119,Issie,Scholard,11 Texas Court,Columbia,Missouri,65218,3,134386.51,34,91.06
    '''
    filename="employees.csv"
    with open(filename,'r') as f:
        lines=f.readlines()
        lines.pop(0)
        for line in lines:
            line=line.split(',')
            id=line[0]
            first_name=line[1]
            last_name=line[2]
            address=line[3]
            city=line[4]
            state=line[5]
            zip=line[6]
            classification = int(line[7])
            salary=float(line[8])
            commission=float(line[9])
            hourly=float(line[10])
            x=Employee(id,first_name,last_name,address,city,state,zip)
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
                
def run_payroll():
    if os.path.exists(PAY_LOGFILE): # pay_log_file is a global variable holding ‘payroll.txt’ 
        os.remove(PAY_LOGFILE) 
    for emp in employees:      # employees is the global list of Employee objects 
        emp.issue_payment()        # issue_payment calls a method in the classification 
      # object to compute the pay