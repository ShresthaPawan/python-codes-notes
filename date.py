import datetime
x=datetime.datetime.now()
print(x)
y=datetime.datetime.now()
m=x.strftime("%b")
print(m)
# %b=month name, short version
# %B=month name, full version
# %m=months as number(0-12)
# %M=minute
# %y=year short version without century
# %Y=year full version
# %H=hour(0-24)
# %I=hour(1-12)
# %p=am/pm