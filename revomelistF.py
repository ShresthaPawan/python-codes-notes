#1. del=delete the value according to index number 
a=[10,20,30,40,50,60]
del a[1]
print(a)
del a[4]
print(a)

#2. pop()=same as del but we can recall the deleted value
b=[10,20,30,40,50]
print(b.pop(1))
print(b)

#3. remove()=delete value directly without index number
c=[1,2,3,4,5,6,7,8,9]
c.remove(3)
print(c)

#4. clear()=helps to revome the whole list
d=[9,8,7,6,5,4,3,2,1]
d.clear()
print(d)