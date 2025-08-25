mu=int(input())
Found_prime=False
for i in range(2,mu):
    if mu%i==0:
        Found_prime=True
        break
if Found_prime==False:
    print("good")
else:
    print("false")
