courses = ["MIT","Cybersecurity","Data science"]

# accessing an element in an array
print(courses[1])

# looping through an array
for course in courses:
    print(course)

# Adding an element into an array
courses.append("Android development")
print(courses)

# Deleting an element from an array(elements are case sensitive must be written exactly as written originally.)
courses.remove("Android development")
print(courses)