from math import *
import useful_tools
from Student import Student

print("HEllo\n world!")
theString = "The string"
print(theString.upper())

print(ceil(3.1))

name = input("Type your name please.")
print("Hello, " + name)

friends = ["Kevin", "Karen", "Jim", "Bob"]


print(friends[1:3])

friends.append("Jerry")

numbers = [1, 2, 3]

numbers.extend(friends)

print(numbers)


def say_hi(name):
    print("Hello " + name)


say_hi("Jim")

employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)

employee_file.close()


employee_file = open("employees.txt", "a")

employee_file.write("\nToby - Human Resources")

employee_file.close()


employee_file = open("employees.txt", "r")
file_lines = employee_file.readlines()
print(file_lines[len(file_lines)-1])

employee_file.close()

print(useful_tools.get_file_ext("testfile.png"))

student1 = Student("Jim", "Business", 3.1, False)

print("GPA = " + str(student1.gpa) +
      ", is on honor roll = " + str(student1.on_honor_roll()))
