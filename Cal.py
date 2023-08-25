print("CALCULATOR")
print("Choose your operand","1.Multiply","2.Divide","3.Add","4.Subtract")
x=int(input("enter your operand"))
if x==1:
    print("You choose Multiplication")
    a=int(input("enter no 1:"))
    b=int(input("enter no 2:"))
    print("Answer is",a*b)
elif x==2:
    print("You choose Division")
    a=int(input("enter no 1:"))
    b=int(input("enter no 2:"))
    print("Answer is",a/b)
elif x==3:
    print("You choose Addition")
    a=int(input("enter no 1:"))
    b=int(input("enter no 2:"))
    print("Answer is",a+b)
elif x==4:
    print("you choose Subtraction")
    a=int(input("enter no 1:"))
    b=int(input("enter no 2:"))
    print("Answer is",a-b)
    print("PROGRAM OVER") 
     
