def calculate(num1, num2, operator):
  """
  Performs the chosen operation on two numbers.

  Args:
      num1: The first number.
      num2: The second number.
      operator: The operation to perform (add, subtract, multiply, or divide).

  Returns:
      The result of the operation.
  """
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("Error: Division by zero")
      return None  # Indicate error
    else:
      return num1 / num2
  else:
    print("Invalid operator")
    return None  # Indicate error

# Get user input
while True:
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    break
  except ValueError:
    print("Invalid input. Please enter numbers only.")

# Get operation choice
while True:
  operator = input("Choose operation (+, -, *, /): ")
  if operator in "+-*/":
    break
  else:
    print("Invalid operator. Please choose +, -, *, or /.")

# Perform calculation and display result
result = calculate(num1, num2, operator)
if result is not None:
  print(f"{num1} {operator} {num2} = {result}")