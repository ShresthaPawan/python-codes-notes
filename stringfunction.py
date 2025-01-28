#1.lower()=makes all letter small
demo="Hello WOrld"
demo_1=demo.lower()
print(demo_1)
#2.upper()=makes all letter big
word="My name is Pawan Shrestha"
word_1=word.upper()
print(word_1)
#3.title()=make the first letter of every word big
nepal="It is beautiful"
nepal_1=nepal.title()
print(nepal_1)
#4.capitaiize()makes the first letter of first word capital
china="it is the second largest country"
china_1=china.capitalize()
print(china_1)
#5.find()=help to find the particular element available or not, if exits give its index number, if not, give -1 
happy="Welcome to Nepal"
print(happy.find("e",7))
print(happy.find("u"))
#6.find()=same as find() but gives error if the value is not available
sad="Obito is broken hero"
print(sad.index("i",3))
#7.isalpha()=gives true if all the values are alphabets only, but gives false if values contain any space
cry="Hellomy"
print(cry.isalpha())
#8.isdigit()=gives true if all the values are numbers only, but gives false if values contain any space
cry="12345"
print(cry.isdigit())
#9.isalnum()=gives true if all the values are alphabets and number but gives false if values contain any space
cry="Hello123"
print(cry.isalnum())