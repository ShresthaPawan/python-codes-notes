#len()=to find the length with space included.
a="Welcome to Nepal"
b=len(a)
for c in range(b):
    print(a[c])
    #without using lens
for c in a:
    print(c)
# for reverse iteration
p="My name is Pawan Shrestha"
p=p[-1::-1]
q=len(p)
for r in range(q):
    print(p[r]) 
     #or
m="hello sir"
s=len(m)
for t in range(s-1,-1,-1):
    print(m[t])
