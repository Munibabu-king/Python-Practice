'''def mark(x=25):
    print(f"the marks are {x}")
mark(20)
mark()'''

def my_mark(*x):
    for element in x:
        print(f"the number is {element}",end=" ")
my_mark(1,2,3,40)

