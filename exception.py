try:
  print(x)
except:
    print("NameError occurred")

try:
    num1 = 20
    num2 = 0
    print(num1 / num2)
except:
    print("ZeroDivisionError occurred")
finally:
    print("success")


# user defined functions
try:
    def multiply(x, y):
        return x * y
except:
    print("Exception occurred")
finally:
    print("success")

print(multiply (10, 20))