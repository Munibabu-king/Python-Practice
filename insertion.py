#insertion sor
'''def insertion(my_list):
    for i in range(1,len(my_list)):
        curr=my_list[i]
        pos=i
        while curr < my_list[pos-1] and pos>0:
            my_list[pos]=my_list[pos-1]
            pos=pos-1
        my_list[pos]=curr
a=[1,2,5,2,8,5,6]
insertion(a)
print(a)'''
#selection sort
def selection(my_list):
    for i in range(len(my_list)):
        pos=i
        for j in range(i+1,len(my_list)):
            if my_list[pos]>my_list[j]:
                pos=j
        my_list[i],my_list[pos]=my_list[pos],my_list[i]
    return my_list
a=[1,2,1,3,1,5,6,4,3]
print(selection(a))
            
    
