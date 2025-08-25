n =int(input())# Total number of rows for the top half of the diamond

for i in range(1, 2 * n):  # Single loop to iterate through rows
    if i <= n:  # Upper half of the diamond
        print(" " * (n - i) + "* " * i)
    else:  # Lower half of the diamond
        print(" " * (i - n) + "* " * (2 * n - i))
