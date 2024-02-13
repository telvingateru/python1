# inbuilt functions
number = max(80, 34, 34, 546, 23)
print(number)

x = min(23, 34, 26, 76, 45)
print(x)

z = pow(2, 3)
print(z)


# user-defined functions
def name():
    print("Telvin")


name()  # calling a function

def student():
    name ="Vincent"
    age = 18
    course = "MIT"
    print(name, age, course)

student()
#Parameters/variables and arguments/values
def students(name,age,course):
    print(name, age, course)

students('Vincent',18,'MIT')
students('Telvin',19,'Cybersecurity')
students('Allan',20,'MIT')
students('Mary',24,'Cybersecurity')
students('Helen',17,'Cybersecurity')
students('Melinda',19,'MIT')
students('Roland',18,'Cybersecurity')

def employees(fullname,age,gender,position,salary):
    print(fullname,age,gender,position,salary)


employees( "Allan" ,18,'Male',"Manager",39989)
employees("Mike Mwaniki",37,"Male","Chief Executive Officer",879690 )
employees("James Bond",47,"Male","Assistant Treasurer",85076 )
employees("Elizabeth Mwihaki",27,"Female","Chief Secretary",300000 )
employees("Jane Mwaniki",46,"Female","Clerk",300000 )