from art import logo
from replit import clear

print(logo)

#add
def add(n1, n2):
  """Takes two numbers as input and adds them up."""
  return n1 + n2

#subtract
def subtract(n1, n2):
  """Takes two numbers as input and subtracts second number from first number."""
  return n1 - n2

#multiply
def multiply(n1, n2):
  """Takes two numbers as input and multplies them."""
  return n1 * n2

#division
def divide(n1, n2):
  """Takes two numbers as input and divides first number by second number."""
  return n1 / n2
#type of operation
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
  }
#recursion function
def calculator():
  #ask user for input variables
  num1 = float(input("What's the first number?: "))
  calc_on = True
  while calc_on:
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation from the list above: ")
    num2 = float(input("What's the next number?: "))
    #perform calculations based on input variables
    function = operations[operation_symbol]
    answer = function(n1= num1, n2=num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or type '0' to exit the calculator: ")
    if continue_calc == 'n':
      calc_on = False
      clear()
      #recursion
      calculator()
    elif continue_calc == "y":
      num1 = answer
    else:
      calc_on = False
calculator()