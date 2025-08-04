def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a, b):
    if b==0:
        return "Error:Cannot divide by zero."
    else:
        return a/b
    
def calculator():
    while True:
         print("Select operation:")
         print("1. Addition (+)")
         print("2. Subtraction (-)")
         print("3. Multiplication (*)")
         print("4. Division (/)")
         print("5. Exit")
         ch=input("choose your choice(1/2/3/4/5):")
         if ch=='5':
             print("Exiting calculator.")
             break
         if ch in ['1', '2', '3', '4']:
             a=float(input("enter first number:"))
             b=float(input("enter second number:"))
             if ch=='1':
                   print("addition of",a,'and',b,'is',add(a,b))
             elif ch=='2':
                   print("subtraction of",a,'and',b,'is',subtract(a,b))
             elif ch=='3':
                   print("multiplication of",a,'and',b,'is',multiply(a,b))
             elif ch=='4':
                   print("Division of",a,'and',b,'is',divide(a,b))
             
         else:
               print("choose correct option(1-5)")
         
         
calculator()    
