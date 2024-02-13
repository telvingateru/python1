#Data types
number = 45  # int
num = 56.78  # float
greeting = "Hello there"  # string
isPythonInteresting = True  # bool

# Variable storing multiple values
languages = ["Python", "php", "Java"]  # list
fruits = ("apple", "","banana", "orange")  # tuple()
countries = {"Kenya","China","USA"}  # set{}

# Dictionary
details = {
    "Firstname": "Grace",
    "Age": 17,
    "Course": "MIT",
    "Nationality": "Kenyan Nationality"
}
print(number)
print(greeting)
print(countries)
print(isPythonInteresting)
print(details)
print(details["Course"])

#Determining the data type
print( type(details) )
print(type(countries))

# Type casting - Converting one datatype to another
print(float(number))
print(int(num))