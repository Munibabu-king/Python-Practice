sentence = input("enter the  sentence:")


words = sentence.split()
print(words)


if len(words) >= 2:
   
    words[0], words[-1] = words[-1], words[0]

    
    new_sentence = ' '.join(words)
    print("sentence:",words)

    
    print("Original sentence:", sentence)
    print("Modified sentence:", new_sentence)
else:

    print("The sentence should have at least two words.")
