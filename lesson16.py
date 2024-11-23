#error handling
x = input ("Enter the first number: ")
y = input ("Enter the second: ")
z = input("Enter the third number: ")

try:
    x_num = int()
    y_num = int()
    z_num = int()

    print(x_num * y_num * z_num)
except:
    print("enter a valid number")