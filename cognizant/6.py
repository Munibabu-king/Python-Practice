ticket=int(input("enter the no of tickets"))
if(5 < ticket <= 40):
    coupen=input("do you have coupen enter 'y' no means 'n'")
    ref=input("do you want refreshment y or n")
    value=input("enter what type of circle ticket do you want k or q")
    if(value=='k'):
        cash=(ticket*75)
        if(ref=='y'):
            cash=cash+(ticket*50)
            
    elif(value=='q'):
        cash=(ticket*150)
        if(ref=='y'):
            cash=cash+(ticket*50)
           
    else:
        print("invalid input")
else:
    print("ticket should be more than 5 lessthan 40")
if(ticket >20):
    cash=cash*0.1
    print(cash)
if(coupen=='y'):
    cash=cash*0.02
    print(cash)

