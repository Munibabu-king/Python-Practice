'''num1 = int(input("Enter a number: "))
l = []

for i in range(2, num1 + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        l.append(i)

print("Prime numbers up to", num1, "are:", l)'''



num1 = int(input("Enter a number: "))
l = []

for i in range(2, num1 + 1):
    is_prime = True  # assume i is prime
    for j in range(2, i):
        if i % j == 0:
            is_prime = False # here if take 4 it is 4%2==0 : atomatically it breaks ,and that whole loop is completed and comes from first
            break   '''example if take 7 it wont %2!=0 so again it in that loop after complets the range still
        inside condition not change so it comes back to the 2nd
        loop then it checks outside condition then it append 7 to the list'''
    if is_prime==False:
        l.append(i)

print(l)
