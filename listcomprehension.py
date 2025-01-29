#List comprehension is the elegant way to define and create lists based on existing list.
n=[m for m in range(1,101)]
print(n)
#using filter
even=[num for num in range(1,1001) if num%2==0]
print(even)
odd=[num for num in range(1,500) if num%2==1]
print(odd)