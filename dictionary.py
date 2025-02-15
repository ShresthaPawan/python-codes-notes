#Dictionary is an unordered data types which works in key/value pair and written inside {}
#to create dictionary
dict={
    "First name":"Pawan",
    "Last name":"Shrestha",
    "Age":19,
}
print(dict["First name"])
print(dict["Last name"])
print(dict["Age"])
# to extract all value
for all in dict:
    print(all) #for all keys
    print(dict[all]) #for all values


#Second dictionary
dict_1={
    "Work":"Google",
    "Position":"Software Engineer",
    "Time":"9-5",
}
print(dict_1["Work"])
print(dict_1["Time"])
for key in dict_1:
    print(key)
    print(dict_1[key])