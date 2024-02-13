weight = input("Enter your weight:")
Weight = int(weight) * 0.7
print(Weight)

price = 1000000
credit = input("Enter your credit(Good/Bad):")
if credit == "Good":
    print("Your new pri")

number = 9
limit = 3
guessing_number = 1
while guessing_number <= limit:
     guessed_number = int(input("Guess a number:"))
     guessing_number += 1
     if guessed_number == number:
        print("Congratulations,you won!!!")
        break
else:
 print("Game lost!")

command = input(">")
while command == "start":
    print("car started...Ready to go!")
elif command == "stop":
      print("car stopped.")
elif command == "help":
       print("""
         start - to start the car
         stop - to stop the car
         quit - to quit       
                """)
else:
    quit()