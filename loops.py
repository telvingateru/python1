# while loop - decrement
number = 105
while number >= 60:
    print(number)
    number -= 1

# increment
number1 = 5
while number1 <= 10:
    print(number1)
    number1 += 1

# break statement
x = 20
while x <= 25:
    print(x)
    if x == 24:
        break
    x += 1

# continue statement
y = 79
while y < 85:
    y +=1
    if y ==83:
        continue
    print(y)

# for loop
languages = ["python", "java", "C++"]
for z in languages:
    print(z)

# range
for mynumber in range(5):
    print(mynumber)

for mynum in range(2,5):
    print(mynum)

for count in range(20,30,2):# third input represents the incrementation
    print(count)