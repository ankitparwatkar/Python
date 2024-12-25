#Global Variable
x="awesome"

def myfunc():
    print("Python is "+ x)
    
myfunc()

x="awesome"

def myfunc():
    x="fantastic"
    print("Python is "+x)
    
myfunc()

print("Python is "+x)

def myfunc():
    global x
    x="fantastic"
    
myfunc()

print("Python is "+x)

x="awesome"

def myfunc():
    global x
    x="fantastic"
    
myfunc()

print("Python is "+x)

x=5
print(type(x))

x=1
y=1.5
z=1j

print(type(x))
print(type(y))
print(type(z))

x=1
y=365897451662
z=-325686

print(type(x))
print(type(y))
print(type(z))

x=1.25
y=1.0
z=-37.29

print(type(x))
print(type(y))
print(type(z))

x=35e5
y=12E4
z=-85.71e100

print(type(x))
print(type(y))
print(type(z))

x=3+5j
y=5j
z=-5j

print(type(x))
print(type(y))
print(type(z))

x=1
y=2.8
z=1j

a=float(x)
b=int(y)
c=complex(z)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 10))

print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a="Hello"
print(a)

a='''Lorem, jqeok.'''
print(a)

