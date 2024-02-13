text = "hello"
text1 = "THERE"

print(text)

# accessing an element in a string
print(text[1])
print(text[1:5])

# modifying a string
print(text.upper())
print(text1.lower())

#size/length of a string
print(len(text))

#string concatenation - combining strings
print(text + " " + text1.lower())

#reassign a string
text = "who is "
print(text+" "+ text1.lower())

#deleting a string
del text
print(text)

