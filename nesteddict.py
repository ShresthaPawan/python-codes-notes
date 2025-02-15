#Nested dictionary means putting a dictionary inside another dictionary or collection of dictionary into one single dictionary
course={
    "Python":{"Duration":"4 Months","Time":"7-9 am","Fees":"NPR 20000",},
    "Java":{"Duration":"6 Months","Time":"9:30-11:30 am","Fees":"NPR 30000",},
    "UI/UX":{"Duration":"2 Months","Time":"12-1 pm","Fees":"NPR 10000",},
    "Html":{"Duration":"3 Months","Time":"1-2 pm","Fees":"NPR 12000",},
    "C Programming":{"Duration":"4 Months","Time":"2-3:30 pm","Fees":"NPR 20000",},
    "Dot Net":{"Duration":"8 Months","Time":"3:30-5:30 pm","Fees":"NPR 35000",},
} 
for a,b in course.items():
    print(a,b)
print(course)
print(course["Java"]["Fees"])
course["Java"]["Fees"]="NPR 23000"
print(course["Java"]["Fees"])