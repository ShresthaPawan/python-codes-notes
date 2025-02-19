#practise 2: Calcator from return type function
while True:
 def sum(a,b):
    c=a+b
    return c
 def sub(a,b):
    c=a-b
    return c
 def mul(a,b):
    c=a*b
    return c
 def div(a,b):
    c=a/b
    return c
 
 def mod(a,b):
    c=a%b
    return c
 def flo(a,b):
    c=a//b
    return c
 def exp(a,b):
    c=a**b
    return c
 value_1=eval(input("Enter the first number:"))
 value_2=eval(input("Enter the second number:"))
 opr=input("Enter the operator:")
 if opr=="+":
    d=sum(value_1,value_2)
    print(d)
 elif opr=="-":
    d=sub(value_1,value_2)
    print(d)
 elif opr=="*":
    d=mul(value_1,value_2)
    print(d)
 elif opr=="/":
    d=div(value_1,value_2)
    print(d)
 elif opr=="%":
    d=mod(value_1,value_2)
    print(d)
 elif opr=="//":
    d=flo(value_1,value_2)
    print(d)
 elif opr=="**":
    d=exp(value_1,value_2)
    print(d)
 else:
    print("Invalid syntax")