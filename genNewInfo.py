import random as rand
departments = ["Science", "Engineer", "Medical", "Command", "Security"]
titles = ["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Wizard"]
    
with open("employees.csv", 'r') as f:
    lines=f.readlines()
newLine = []    
for line in lines:
    if line[0] == 'I':
        newLine.append(line)
        continue
    data = line.split(',')
    day = rand.randrange(1,30)
    month = rand.randrange(1,12)
    year = rand.randrange(1950, 2000)
    dob =str(day)+"/"+str(month)+"/"+str(year)
    ssn =str(rand.randrange(100, 999)) + "-" + str(rand.randrange(10,99)) + "-"+str(rand.randrange(1000,9999))
    startdate = str(rand.randrange(1, 30)) + "/" + str(rand.randrange(1,12)) + "/"+str(rand.randrange(2000,2021))
    #has_dd=str(rand.randrange(0,2))
    routing_num=str(rand.randrange(100000000,999999999))
    acct_num=str(rand.randrange(100000000,999999999))
    ismanager=str(rand.randrange(0,2))
    isarchived=str(rand.randrange(0,2))
    emptitle=rand.choice(titles)
    department = rand.choice(departments)
    officephone=str(rand.randrange(100,999)) + "-"+str(rand.randrange(100,999))+"-"+str(rand.randrange(1000,9999))
    firstname = data[1].split(" ")[0]
    lastname = data[1].split(" ")[1]
    officeemail=lastname+firstname+"@uvu.edu"
    password = str(rand.randrange(350,1000))+rand.choice(["Terran", "Zerg", "Protoss"])+rand.choice(['#','$','@','*'])
    newData= ""
    for item in data:
        newData += item+","
    newData = newData[0:-2]
    newData +=','+dob+','+ssn+','+startdate+','+routing_num+','+acct_num+','+ismanager
    newData += ','+isarchived+','+emptitle+','+department+','+officephone+','+officeemail+','+password+'\n'
    newLine.append(newData)

with open("employeestest.csv", 'w') as w:
    for line in newLine:
        w.write(line)