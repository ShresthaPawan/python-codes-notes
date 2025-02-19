#Set is an unordered data types with unique elements and are written inside {}
#Iteration
set_1={10,20,30,40,50,60,70}
for s in set_1:
    print(s)
#Function of set
#set()= to convert list into set
lis=[10,20,30,40,50,60]
se=set(lis)
print(se)
#add()= value store in random postion
lis_1={10,20,30,40,50,60,70,80}
lis_1.add(90)
print(lis_1)
#pop()=delete random element
se_1={11,22,33,44,55}
se_1.pop()
print(se_1)
#clear()
se_3={20,30,40,50,55}
se_3.clear()
print(se_3)
#remove()
se_2={10,20,30,40,50,60}
se_2.remove(10)
print(se_2)
#discard()  However, there is a difference between remove() and discard(). When the specified element does not exist in the given set, # the remove() function raises an error.
#  Whereas the discard() method does not raise an error when the specified element does not exist in the set, and the set remains unchanged.
p={10,20,30}
p.discard(20)
print(p)
#update()
t={10,20,30,40,50,60}
u={11,22,33,44}
t.update(u)
print(t)