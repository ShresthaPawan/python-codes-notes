#Tuple is an ordered, immutable data type which is written inside ().
tup=(10,20,30,40,50)
b=tup[2]
print(b)
#Iteration without using len()
for d in tup:
    print(d)
#Iteration with len()
l=len(tup)
for t in range(l):
    print(tup[t])
#For reverse
for t in range(l-1,-1,-1):
    print(tup[t])
#or
app=(90,80,70,60,50,40)
ball=app[-1::-1]
cat=len(ball)
for dog in range(cat):
    print(ball[dog])
