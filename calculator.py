# calculator using arithmetic operator
first_number=eval(input("Enter your first value:"))
second_number=eval(input("Enter your secind value:"))
operator=input("Enter your operator(+,-,*,/,**,//,%):")
if operator=="+":
    print(first_number+second_number)
elif operator=="-":
    print(first_number-second_number)
elif operator=="*":
    print(first_number*second_number)
elif operator=="/":
    print(first_number/second_number)
elif operator=="**":
    print(first_number**second_number)
elif operator=="//":
    print(first_number//second_number)
elif operator=="%":
    print(first_number%second_number)

else:
    print("Invalid Operator")