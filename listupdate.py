#1). insert()=insert value with two parameter where the first value is the index number and second one is the value
a=[10,20,30,40,50]
a.insert(0,5)
print(a)
#2. append()=insert one value at a time, the value will directly go to the end
b=[10,20,30,40]
b.append(50)
print(b)
# for multiple values
p=[70,80]
q=[22,33,44,55,66]
p.append(q)
print(p)
#3). extend()
c=[1,2,3,4,5,6,7,8]
d=[9,10]
c.extend(d)
print(c)