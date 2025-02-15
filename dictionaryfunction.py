happy={
    "First Name":"Pawan",
    "Second Name":"-",
    "Last Name":"Shrestha",
    "Grade":"Bachelor First Year",
    "University Name":"Techspire College",
    "Interested Language":"Python",
    "Favourite Color":"Black",
    "Address":"Nepal",
}
for keyvalue in happy:
    print(keyvalue)
    print(happy[keyvalue])
#funtions
#1) get()
g=happy.get("First Name")
print(g)
#2) pop()
p=happy.pop("Address")
print(p)
#3) items()
for a,b in happy.items():
    print(a,b)
#4) keys()
for b in happy.keys():
    print(b)
#5) values()
for c in happy.values():
    print(c)
#6) del[]
del happy["Second Name"]
print(happy)
#7) dict()
a=dict(name="Ram",address="KTM",)
print(a)