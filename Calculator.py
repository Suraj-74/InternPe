### Build a simple calculator to perform different operation

print("Select an operation to perform:")
print("1: Addition")
print("2 :Subtraction")
print("3 :Multiplication")
print("4 :Division")

operation=input()  # user input which he/she want to perfom their task

if operation=="1":
    n1=float(input("Enter the first number:"))  # used float datatype to convert into float 
    n2=float(input("Enter the second number:")) # used float datatype to convert into float 
    add=n1+n2 # addition of n1 and n2
    print("The addition of", n1, "and", n2, "is", add)
elif operation=="2":
    n1=float(input("Enter the first number:"))  # used float datatype to convert into float 
    n2=float(input("Enter the second number:")) # used float datatype to convert into float 
    sub=n1-n2  # subtraction of n1 and n2
    print("The difference of", n1, "and", n2, "is", sub)
elif operation=="3":
    n1=float(input("Enter the first number:")) # used float datatype to convert into float 
    n2=float(input("Enter the second number:")) # used float datatype to convert into float 
    mul=n1*n2 # multiplication of n1 and n2
    print("The multiplication of", n1, "and", n2, "is", mul)
elif operation=="4":
    n1=float(input("Enter the first number:")) # used float datatype to convert into float 
    n2=float(input("Enter the second number:")) # used float datatype to convert into float 
    div=n1/n2 # division of n1 and n2
    print("The division of", n1, "and", n2, "is", div)
else:
    print("Invalid operaiton, select valid operation as per given")