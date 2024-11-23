#inheritance
#error handling
#dates

class Employee:
    def __init__(self, name, id_number, dob, gender):
        self.name = name
        self.id_number = id_number
        self.dob = dob
        self.gender = gender
    def print_details(self):
        print( f"name: {self.name}\nid, {self.id_number}\ndob, {self.dob}\ngender, {self.gender}")

class permanentempoyee(Employee):
    def __init__(self, name, id_number, dob, gender,salary):
      #  self.name = name
       # self.id_number = id_number
       # self.dob = dob
        #self.gender = gender
        super.__init__(name, id_number, dob, gender)
        self.salary = salary
    def print_salary(self):
        print(f"salary is{self.salary}")

    def print_details(self):
        super().print_details()
        print(f"salary")

class temporaryempoyee(Employee):
    def __init__(self, name, id_number, dob, gender,hourly_pay,end_date):
        super.__init__( name , id_number, dob, gender)
        self.hourly_pay = hourly_pay
        self.end_date = end_date

    def print_hourly_pay(self):
        print(f"hourly_pay is{self.hourly_pay}")

    def print_end_date(self):
        print(f"end_date is{self.end_date}")

p1= permanentempoyee(salary=10000,name="brenda",id_number=36988487,gender="f",dob="1999-12-01")
p1.print_details()
p1.print_salary()

t1=temporaryempoyee("jemuu",09879,)