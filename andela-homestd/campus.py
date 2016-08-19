class Campus:

    def __init__(self, main_st, name, age, sex, mstatus, cstatus):

        self.name = name
        self.main_status = main_st
        self.age = age
        self.sex = sex
        self.marital_status = mstatus
        self.citizenship_status = cstatus

    def getMainStatus(self):
        return self.main_status

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getSex(self):
        return self.sex

    def getMaritalStatus(self):
        return self.marital_status

    def getCitizenShipStatus(self):
        return self.citizenship_status


class Student(Campus):

    def __init__(self, main_st, name, age, sex, mstatus, cstatus, department, course, registration_date):
        Campus.__init__(self, main_st, name, age, sex, mstatus, cstatus)

        self.dep = department
        self.course = course
        self.regdate = registration_date

    def getDepartment(self):
        return self.dep

    def getRegistrationDate(self):
        return self.regdate

    def getCourse(self):
        return self.course


class Staff(Campus):

    def __init__(self, main_st, name, age, sex, mstatus, cstatus, employement_date, paygrade):
        Campus.__init__(self, main_st, name, age, sex, mstatus, cstatus)

        self.emdate = employement_date
        self.paygrade = paygrade

    def getEmployementDate(self):
        return self.emdate

    def getPayGrade(self):
        return self.paygrade


class Academic(Staff):

    def __init__(self, main_st, name, age, sex, mstatus, cstatus, employement_date, paygrade):
        Staff.__init__(self, main_st, name, age, sex, mstatus, cstatus, employement_date, paygrade)


class NonAcademicStaff(Staff):

    def __init__(self, main_st, name, age, sex, mstatus, cstatus, employement_date, paygrade):
        Staff.__init__(self, main_st, name, age, sex, mstatus, cstatus, employement_date, paygrade)


camp = Student("student", "george", "40", "male", "married",
               "nigerian", "computer science", "5 May 2016", "computer science")

print(camp.getAge(), camp.getName(), camp.getSex())
