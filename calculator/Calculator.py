from art_calculator import logo

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


operations = {"+": addition, 
"-": subtraction,
"*": multiplication,
"/": division}




def calculator():
  print(logo)
  num1 = float(input("Enter first number:"))
  for kv in operations:
    print(kv)
  
  should_cont = True
  
  while should_cont:
    choice = input("Enter your operation choice.(+,-,* or /):")
    num2 = float(input("Enter second number:"))
    function = operations[choice]
    ans = function(num1,num2)
    print(f"{num1} {choice} {num2} = {ans}")
    choice2 = input("Type 'y' to continue with {ans} or type 'n' to start a new calculation pr type 'e' to exit calculator: ")

    if choice2 == "y":
      num1 = ans
    elif choice2 == "n":
      #should_cont = False
      calculator()
    else:
      should_cont = False
      print("Programme Closed!")  

calculator()
