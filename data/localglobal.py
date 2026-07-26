x = 10   # global variable
print(x)

def hello():
    global x   # local to global variable
    x = 4
    y = 5 # local variable
    print("The Local varable y is ",y)
    print("The global variable  x is {}".format(x))
    print("Hello anku")

print("The global variable x is ",x)
hello()
print(x)
# print(y) # throw the error because y is local variable and is not accessible
print("The global variable x is {}".format(x))