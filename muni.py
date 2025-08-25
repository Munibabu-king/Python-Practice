def replace_a_patterns(s):
    # Step-by-step replacement in order of priority
    s = s.replace("aaa", "$")
    s = s.replace("aa", "#")
    s = s.replace("a", "%")
    return s

# Example
input_str = "Maaaaaabuaa"
output_str = replace_a_patterns(input_str)
print(output_str)  # Output: M$%bu#
