rows = int(input())
cols = int(input())
matrix = []

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Input matrix
for i in range(rows):
    l = []
    for j in range(cols):
        k = int(input())
        l.append(k)
    matrix.append(l)

# Check each row for at least one prime number
for i in range(rows):
    isFound = False
    for j in range(cols):
        if is_prime(matrix[i][j]):
            isFound = True
            break
    if isFound:
        print(f"Row {i} is valid (contains at least one prime number)")
    else:
        print(f"Row {i} is not valid (no prime numbers found)")

