#Queue is a linear data structure
#Stores items in an FIrst In First Out (FIFO) manners
#Queue Operators
#a Enqueue=adds an items in queue
#b Degueue=removes an items from the queue
#c Front=get the front items from the queue
#d Rear=get the last items from the queue
list=[]
while True:
    que=eval(input("1) Enqueue ELement\n2) Dequeue ELement\n3) Front Element\n4) REar Element\n5) Exist\n :") )
    if que==1:
        ask=input("Enter the value:")
        list.append(ask)
        print(list)
    elif que==2:
        if len(list)==0:
            print("The list is empty!!!")
        else:
            rem=list.pop(0)
            print("The deleted value is,",rem)
            print(list)
    elif que==3:
        if len(list)==0:
            print("The list is empty!!!")
        else:
            print("The first value of list is,",list[0])
    elif que==4:
        if len(list)==0:
            print("The list is empty!!!")
        else:
            print("The last value of list is,",list[-1])
    elif que==5:
        print("Thank You, Have a good day")
        break;
    else:
        print("Invalid Operator, Check the Operator properly")
