from mylib import myfunc
a = input('Enter your character: ')
b = input('How many turns you want to run: ')
for i in range(1, int(b)+1):
    myfunc(a,i)
#myfunc(a,b)