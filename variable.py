y = 5
x = 4 #integer
x = "shoukat" #string

print(x , y)


x = str(3) 
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


x ,y , z = "hello" , "world" , "Pakistan"
print(x)
print(y)
print(z)
x = y = z = "orange"
print(x)
print(y)
print(z)

fruits = ["apple" , "banana" , "orange"]
x , y , z = fruits
print(x)
print(y)
print(z)

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)
myfunc()

print("Python is " + x)