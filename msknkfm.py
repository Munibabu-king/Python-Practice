def mergesort(list):
    if len(list)>1:
        mid=len(list)//2
        left_l=list[:mid]
        right_l=list[mid:]
        mergesort(left_l)
        mergesort(right_l)
        i=0
        j=0
        k=0
        while i<len(left_l)and j<len(right_l):
            if left_l[i] < right_l[j]:
                list[k]=left_l[i]
                k+=1
                i+=1
            else:
                list[k]=right_l[j]
                k+=1
                j+=1
        while i<len(left_l):
            list[k]=left_l[i]
            k+=1
            i+=1
        while j<len(right_l):
            list[k]=right_l[j]
            k+=1
            j+=1
        return list
a=[2,3,4,1,2,3]
k=mergesort(a)
print(k)
