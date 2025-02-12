# split();= breaks the string and turn it in list for single input
#for single input
a=input("Enter the Value:")
b=a.split();
print(b)

#for multiple input

p=[]
for q in range(1,4):
    r=input("Enter the value"+str(q)+":")
    p.append(r)
    print(p)