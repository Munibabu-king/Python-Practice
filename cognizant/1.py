import sys
ltt=int(input("Enter the no of liters to fill the tank:"))


lt= (ltt*1.00)

if(ltt<1):
    print(f"{ltt} is an Invalid Input")
    sys.exit()

print("Enter the distance covered")

diss =int(input())

dis= (diss*1.00)

if(diss<1):
    print("{} is an Invalid Input".format(diss))
    sys.exit()

hundred = ((lt/dis)*100)

print("Liters/100KM")

print(round(hundred,2))

miles = (dis*0.6214);

gallons =(lt*0.2642);

mg = miles/gallons;

print("Miles/gallons")

print(round(mg,2))
