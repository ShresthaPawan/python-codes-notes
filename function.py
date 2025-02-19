#Two types of funtions
# 1) In-built function like count(),del[],pop().
# 2) User define funtions: Block of statement which can be used repetitively in a program.
# Simple function
def function():
    print("Hello")
function()
# Function with argument
def sum(a,b):
    print(a+b)
sum(4,10)
# set up default value
def mul(a,b=2):
    print(a*b)
p=12
mul(12)
#value override
mul(12,3)
# Return type
def div(a,b):
    c=a/b
    return c
d=div(20,4)
print(d)
#Practise 1
def sub(a,b):
    if a>b:
        c=a-b
    elif b>a:
        c=b-a
    else:
        print("0")
    return c
d=sub(2,4)
print(d)
#practise 2
value_1=eval(int("Enter the first number:"))
value_2=
