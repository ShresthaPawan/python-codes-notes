#The stack is a linear data structure
#Stores items in a Last In First Out (LIFO) or First In Last Out (FILO) manner
#Stack operators
#Push=insert an element
#Pop= deletion of last element
#Peek= display last element
#Display= display list

list=[]
while True:
    first=eval(input("1) Push ELement\n 2) Pop Element\n 3) Peek Element\n 4) Display List\n 5) Exist\n :"))
    if first==1:
        inp=input("Enter the value:")
        list.append(inp)
        print(list)
    elif first==2:
        if len(list)==0:
           print("The list is empty!!!! ")
        else:
           de=list.pop()
           print(list)
           print("Recently Deleted Value,",de)
    elif first==3:
        if len(list)==0:
           print("The list is empty!!!! ")
        else:
           print("The last inputed value is",list[-1])
    elif first==4:
        if len(list)==0:
           print("The list is empty!!!! ")
        else:
            print("The Value of List:",list)
    elif first==5:
        print("Thank You, Have a good day")
        break;
    else:
        print("Invalid Operator, Check the index number properly")

