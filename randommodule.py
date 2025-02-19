import random
# 1) randit()= return a number from a to b (both included as well)
print(random.randint(1,10))
# 2) randrange()=return a number from a to b(a included b not included)
print(random.randrange(1,10))
# 3) choice()=return a random value from given values
lis=["ram","shyam","hari","sita","gita"]
print(random.choice(lis))
# 4) ramdom()=gives a random float number between 0 to 1
print(random.random())
# 5) shuffle()=takes a sequence and return the sequence in order
random.shuffle(lis)
print(lis)
# 6) uniform()=gives a random float number between two given parameter
print(random.uniform(1,5))