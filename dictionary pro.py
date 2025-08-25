rows=int(input())
cols=int(input())
matrix=[]
def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
for i in range(rows):
    l=[]
    for j in range(cols):
        k=int(input())
        l.append(k)
    matrix.append(l)
for i in range(rows):
    is_found=True
    for j in range(cols):
        n=matrix[i][j]
        if is_prime(n):
            is_found=False
            break
    if is_found:
        print(f"row{i}valid")
    else:
        print(f"row{i}invalid")
print(matrix)   
        
            
        
    
    
