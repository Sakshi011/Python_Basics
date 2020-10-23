# set data type
# unordered collection of data

# INTRO ----------------------------------------------------------------------------------
s = {1,1.1,2.3,3,'string'}
print(s)
print("\n")
# In set all elemets are unique that's why it is used to remove duplicate elements
l = [1,2,4,2,3,6,3,7,6,6]
s2 = list(set(l))
print(s2)
print("\n")

# ADD AND REMOVE ELEMENT -----------------------------------------------------------------
s3 = {1,2,3}
s3.add(4)
s3.add(5)
print(s3)
s3.remove(4)
s3.discard(5)
print(s3)
print("\n")

# FOR LOOP ------------------------------------------------------------------------------
for i in s:
    print(i)
print("\n")

# UNION ---------------------------------------------------------------------------------
s1 = {1,2,3,4}
s2 = {3,4,5,6}
union_set = s1 | s2
print(union_set)
print("\n")

# INTERSECTION --------------------------------------------------------------------------
intersection_set = s1 & s2
print(intersection_set)
print("\n")

# SET COMPREHENSION ---------------------------------------------------------------------
s = {i**2 for i in range(1,11)}
print(s)
print("\n")

names = ['siya','tiya','nia']
first = {i[0] for i in names}
print(first)
