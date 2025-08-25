import sys
cse=int(input("enter the no of placements got"))
ece=int(input("enter the no of placements got"))
mec=int(input("enter the no of placements got"))
if(cse<0 or ece <0 or mec<0):
    print("invalid input")
    sys.exit()
elif(cse > ece and cse > mec):
    print("cse got high placements")
elif(ece > cse and ece > mec):
    print("ece got high placements")
    
elif(mec > cse and mec > ece):
    print("mec got high placements")
    
elif(ece == mec and ece!=cse ):
    print("mec and ece high placements")
    
elif(mec == cse and cse!=ece ):
    print("cse and mec got high placemens")
    
elif(ece==cse and cse!=mec):
    print("cse and ece got high placements")
    
else:
    print ("non of the above got high pacakge")
    
