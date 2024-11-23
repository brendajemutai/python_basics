#dates
from datetime import date, timedelta, datetime
from sys import dont_write_bytecode

today= date.today()
print(today)

formatted_date= today.strftime("%m-%d-%Y")
print(formatted_date)

after_forty_days=today+timedelta(days=40)
print(after_forty_days)

dob=("1990-01-14")
#convert to date time
date_of_birth = datetime.strptime(dob,)
age=today.year - date_of_birth.year
print("i am " , age " years_old ")

age_in_days=datetime.today()- date_of_birth
print(age_in_days.days)



