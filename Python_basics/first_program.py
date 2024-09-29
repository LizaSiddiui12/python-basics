# its use for presentation
a="hi liza"
print(a.title())
x= "welcome to our code"
print(x.title())

# assign variables
b=4
t="biscuits"
print(b,t)
# get the type
print(type(t))
print(type(b))
# assign multiple values in one line
s,d,g=4,5,6
print(s,d,g)
print(s)
print(d)
print(g)
#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# output variable
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# --------------------------------------
x = 5
y = 10
print(x + y)
# ************--------- Slicing--------*****************

b = "Hello, World!"
print(b[2:8])

b = "Hello, World"
print(b[-5:-2]) #-ve sign shows: Use negative indexes to start the slice from the end of the string

#*********_________modify________********
a = "Hello, World!"
print(a.upper())

a = "  Hello, World!  "
print(a.lower())

a = " Hello, World! "
print(a.strip()) # white spacing

a = "Hello, World!"
print(a.replace("Hello", "Liza"))

a = "Hello World!"
print(a.split(","))

# __________________***FORMAT STRING****_____________

age = 36
txt = f"My name is John, I am {age}"  # AGE KO YA NO KO STRING M CONCATINATE KARWANA
print(txt)

# ________________************* LOGIC BUILDING **************_________________

mm = 3
bb=5
print("mm = ",mm,"bb = ",bb)
c=mm
mm=bb
bb=c
print("*****----after interchange the values----******")
print("mm = ",mm,"bb = ",bb)