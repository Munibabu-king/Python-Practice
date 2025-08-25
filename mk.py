# Get input from the user
s = input("Enter a string: ")

# Initialize the required variables
char_set = set()
left = 0

# Iterate through the string
for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    char_set.add(s[right])

# Output the result
print(len(char_set))
print(char_set)
