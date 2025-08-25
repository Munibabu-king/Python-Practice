#square matrix taken perfect specific
'''n = int(input())                 
points = []
for i in range(n):
    x,y= map(int, input().split())
    points.append([x,y])
print(points)'''
#what ever how would you like the matrix
'''n = int(input())
points = []
for i in range(n):
    x= list(map(int, input().split()))
    points.append(x)
print(points)'''
#list inside no  list taking input

'''n = int(input())
points = [1,2,3,4]
points2=[3,4,5,6]
for i in range(n):
    x,y,z= map(int, input().split())
    x1,y2,z3= map(int, input().split())
    points.append([x,y,z])
    points.append([x1,y2,z3])
k=list(map(lambda x,y:x+y,points,points2))
print(k)'''
# list inside no list so do the take input
'''n = int(input())
points = [3,4]
points2=[6,7]
for i in range(n):
    points.append(int(input()))
    points2.append(int(input()))
    for i in range(n):
    x,y,z= map(int, input().split())
    x1,y2,z3= map(int, input().split())
    points.append([x,y,z])
    points.append([x1,y2,z3])
k=list(map(lambda x,y:x+y,points,points2))
print(k)'''
#list inside list addition
'''n = int(input())
points = []
points2=[]
for i in range(n):
    x,y,z= map(int,input().split())
    x1,y2,z3= map(int,input().split())
    points.append([x,y,z])
    points2.append([x1,y2,z3])
k=list(map(lambda x,y:[x[i]+y[i] for i in range(3)],points,points2))
print(k)'''

# matrix addition [2,3,4]+[2,3,4,5]
'''n=int(input())
points=[]
points2=[]
for i in range(n):
    points.append(int(input()))
    points2.append(int(input()))
print(list(map(lambda x,y:x+y,points,points2)))'''

# Read matrix dimensions
n = int(input("Enter number of rows of Matrix A: "))
m = int(input("Enter number of columns of Matrix A / rows of Matrix B: "))
p = int(input("Enter number of columns of Matrix B: "))

# Input Matrix A
print("Enter Matrix A (each row):")
A = [list(map(int, input().split())) for _ in range(n)]

# Input Matrix B
print("Enter Matrix B (each row):")
B = [list(map(int, input().split())) for _ in range(m)]

# Initialize result matrix with zeros (n × p)
result = [[0 for _ in range(p)] for _ in range(n)]

# Matrix multiplication logic
for i in range(n):
    for j in range(p):
        for k in range(m):
            result[i][j] += A[i][k] * B[k][j]

# Output the result
print("Result of A × B:")
for row in result:
    print(row)



































