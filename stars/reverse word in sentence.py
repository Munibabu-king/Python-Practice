'''def reverse_word(word_list):
    reversed_word = word_list[::-1]
    return reversed_word

# Example usage:
input_word = list("Python babu king")
output_word = reverse_word(input_word)

print("Input Word:", ''.join(input_word))
print("Reversed Word:", ''.join(output_word))'''

'''# Without using a function

# Example usage:
ints=input("enter the values")
m=ints.split()
input_word=m

reversed_characters_list =list(input_word[::-1])

print("Input sentence:", ''.join(ints))

# Reverse the list in-place

print("Reversed Characters List:", reversed_characters_list)

'''
'''
word = input("enter the value:")
words=word

reversed_characters_list = list(words[::-1])

print("Original Word:", word)
print("Reversed Characters List:", reversed_characters_list)
m=word.split()
for m in reversed(m):
    print(m)
    '''


# Without using a function

# Example usage:
i=["python","muni"]

for i in reversed(i):
    print(i)
print(''.join(i))
    
'''
# Example usage:
word_list = ["Python", "is", "awesome", "and", "powerful"]

reversed_word_list = []'''
'''for i in word_list:
    reversed_word_list.append(i[::-1])'''
'''
reversed_word_list = [i[::-1] for i in word_list]

# Print all words in reverse
print("Original Word List:", word_list)
print("Reversed Word List:", reversed_word_list)
print("reverse words",reversed_word_list[::-1])
print(word_list[::-1])'''



'''a = [float(x) for x in input("enter value:").split()]
print(tuple(a))'''

    





