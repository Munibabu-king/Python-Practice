'''def insert_element_at_index(my_list, index, element_to_insert):
    # Insert the element at the specified index
    my_list.insert(index, element_to_insert)

    return my_list

# Example usage
original_list = [1, 2, 3, 4, 5]
print("Original List:", original_list)
index_to_insert = 2
element = 99
new_list = insert_element_at_index(original_list, index_to_insert, element)


print("New List:", new_list)'''

# Example without using a function

original_list = [1, 2, 3, 4, 5]
index_to_insert = 2
element = 99

# Insert the element at the specified index
original_list.insert(index_to_insert, element)

print("Original List:", original_list)

