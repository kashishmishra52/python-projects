def addition(n1,n2):
  return n1+n2
def subtraction(n1,n2):
  return n1-n2
def multiplication(n1,n2):
  return n1*n2
def divison(n1,n2):
  return n1/n2
operation={
  "+":addition,"-":subtraction,"*":multiplication,"/":divison
          }
def calculator():
  num1=int(input("enter first number?"))
  for keys in operation:
    print(keys)
  calculation=True
  while calculation:
    operation_symbol=input("choose an operator from the options given above ")
    num2=int(input("enter next  number?"))
    calculation_function=operation[operation_symbol]
    answer=calculation_function(n1=num1,n2=num2)
    print(f"{num1} {operation_symbol} {num2}= {answer} ")
    if input(f"type y to continue for calculating with {answer} and type n to start new calculation")=="y":
        num1=answer
    else:
        calculation=False
        calculator()
calculator()


  
