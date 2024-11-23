#functions
import math
from datetime import date


def calc_area_triangle(b,h):
    area=0.5 * b * h
    print(area)

def calc_area_circle(radius):
    area=math.pi*radius*radius
    area=round(area,2)
    print("Area of the circle is",area,"cm^2")

def print_todays_date():
    today=date.today()
    print(today)

def add(*args):
    total=0
    for num in args:
        total+=num
        print("Total is",total)

def sayHi(name,age=21):
    print("Hello ",name," I am  ",age, " years old")

sayHi("Mary")
sayHi("Kevo",23)

sayHi(age=23,name="Mary")

#use a function-calling
calc_area_triangle(5,3)
calc_area_triangle(40,66)

triangles=[[5,8],[34,56],[3,8],[9,10],[21,45],[34.7,89.9]]

for triangle in triangles:
    #calc_area_triangle(*triangle)
    calc_area_triangle(triangle[0],triangle[1])

calc_area_circle(5.906743)
calc_area_circle(45.789)

print_todays_date()

add(1,2,3,4,5)
add(45,89,60,90,5,67,345)

#data name,gender,phone,amount
#account
#deposit/withdrawal/check balance
#oop
#________________________
#matatu ->number,driver,conductor,route
