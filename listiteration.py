#without using len()
list_1=[10,20,30,40,50,60,70,80,"OK","hello"]
for b in list_1:
    print(b)
#with len()
list_2=[90,80,70,60,50,40,30,20,10,"nice"]
leng=len(list_2)
for c in range(leng):
    print(list_2[c])
#for reverse 
list_3=["my","life","my","rule"]
list_3=list_3[-1::-1]
p=len(list_3)
for q in range(p):
    print(list_3[q])
#or
list_4=["Python","is","great"]
k=len(list_4)
for j in range(k-1,-1,-1):
    print(list_4[j])