my_list = [1,2,3]
print(f"Original list: {my_list}")
print(f"Original list id: {id(my_list)}")

my_list.append(4)
 
print(f"Modified list: {my_list}")
print(f"Modified list id: {id(my_list)}")

print("-----------------------------")
my_tuple = (1,2,3)
print(f"Original tuple: {my_tuple}")
print(f"Original tuple id: {id(my_tuple)}")

#re-assignment
my_tuple = my_tuple + (4,)
print(f"Modified tuple: {my_tuple}")
print(f"Modified tuple id: {id(my_tuple)}")

# string
name = "Sarah"
name[0] = "T"

# mutable /változtatható 
# lists, dictionaries, set, bytearray

# immutable / változtathatlan 
# int, bool, float, string, tuple, frozenset, None