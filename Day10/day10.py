# #Functions with outputs

# def format_name(f_name, l_name):
#     if f_name =="" or l_name == "":
#         return "You didn't provide valid inputs."
    
#     formated_first_name = f_name.title()
#     formated_last_name = l_name.title()
       
#     return f"{formated_first_name} {formated_last_name}"


# first_name = input("Enter Your First Name: ")
# last_name = input("Enter Your Last Name: ")

# print(format_name(first_name, last_name))

from art import logo


def add(n1, n2):
  return n1 + n2


def substract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1/n2


operators = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))

  for symb in operators:
    print(symb)

  calculatoin_over = False
  while not calculatoin_over:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    result = operators[operation_symbol]
    answer = result(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continue_calc = input(
        f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
    if continue_calc == "y":
      num1 = answer

    else:
      calculatoin_over = True
      calculator()
