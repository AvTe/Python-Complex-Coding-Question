# Answer 5: In Python, we use = operator to create a copy of an object. You may think that this creates 
# a new object; it doesn't. It only creates a new variable that shares the reference of the original object.

# In Python, there are two ways to create copies:
# Shallow Copy.
# Deep Copy.


old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))