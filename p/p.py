arr = list(map(int, input().split()))
d = len(arr) // 2

for i in range(d):
    if arr[d-i-1] != arr[d+i+1]:
        print("false")
        break
else:
    print("true")
