#Calculator with Match-Case

num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
op=input("enter the operator +,-,*,/:")

match op:
    case "+":
        print("result:",num1+num2)
    case "-":
        print("result:",num1-num2)
    case "*":
        print("result:",num1*num2)
    case "/":
        if num2!=0:
            print("result:",num1*num2)
        else:
           print("zero is not allowed")
    case _:
        print("default")

