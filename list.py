# INTRO TO LIST----------------------------------------------------------------------------
numbers = [1,2,3,4]
print(numbers[3])
words = ["word1","word2","word3"]
print(words[2])
mixed = [1,2,"list",3.2]
print(mixed[1])
print(mixed)
mixed[1:] = ["three","four"]
print(mixed)
print("\n")

# INSERT IN LIST---------------------------------------------------------------------------
fruits1 = ["mango","apple"]
fruits1.append("grapes")
fruits1.append("orange")
print(fruits1)
fruits1.insert(2,"banana")
print(fruits1)
fruits2 = ["strawbwrry","cherry"]
fruits = fruits1 + fruits2
print(fruits)
fruits1.extend(fruits2)
print(fruits1)
print(fruits2)
print("\n")

# DELETE FROM LIST -----------------------------------------------------------------------
fruits = ['mango', 'orange','apple','cherry','banana']
print(fruits)
popped = fruits.pop(1)
print(fruits)
print(popped)
del fruits[1]
print(fruits)
fruits.remove('banana') # without index number
print(fruits)
print("\n")

# SOME BUILT-IN FUNCTION -----------------------------------------------------------------
fruits = ['mango', 'orange','apple','cherry','orange']
print(fruits.count('orange')) #count()
fruits.sort() #sort()
print(fruits)
numbers = [3,2,6,4,9,8]
numbers.sort()
print(numbers)
print(sorted(numbers)) #sorted()
numbers_copy = numbers.copy() #copy()
print(numbers_copy)
numbers.clear() #clear
print(numbers)
print("\n")

# 'IN' IN LIST ---------------------------------------------------------------------------
fruits = ['mango', 'orange','apple','cherry','orange']
if 'mango' in fruits:
    print("mango is present")
else:
    print("mango is not present")

# == AND IS--------------------------------------------------------------------------------
fruits1 = ["apple","mango"]
fruits2 = ["apple","mango"]
print(fruits1 == fruits2) # compares only values
print(fruits1 is fruits2) # compares values with file location
print("\n")

# SPLIT AND JOIN METHOD -------------------------------------------------------------------
# convert string to list
name, age = input("enter your name and age(comma seprated): " ).split(',')
print(name)
print(age)
#convert list to string
user_info = ["sakshi",'19']
print(','.join(user_info))
print("\n")

# FOR-LOOP -------------------------------------------------------------------------------
fruits = ['mango', 'orange','apple','cherry','pear']
for fruit in fruits:
    print(fruit)
print("\n")

# WHILE-LOOP -----------------------------------------------------------------------------
fruits = ['mango', 'orange','apple','cherry','pear']
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
print("\n")

# LIST INSIDE LIST -----------------------------------------------------------------------
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[2])
for sublist in matrix:
    for i in sublist:
        print(i)
print(matrix[2][0])

# LIST EXAMPLE-1 ------------------------------------------------------------------------
numbers = [1,2,3,4,5,6,7,8,9]
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))

# LIST EXAMPLE-2 -------------------------------------------------------------------------
def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square
numbers = list(range(1,11)) #creating list
print(square_list(numbers))

# LIST EXAMPLE-3 -------------------------------------------------------------------------
def reverse_list1(l):
    return l[::-1]
numbers = list(range(1,11)) #creating list
print(reverse_list1(numbers))
def reverse_list2(l):
    r_list = []
    for i in range(len(l)):
        popped = l.pop()
        r_list.append(popped)
    return r_list
numbers = list(range(1,11)) #creating list
print(reverse_list2(numbers))

# LIST EXAMPLE-4 -------------------------------------------------------------------------
def filter_odd_even(l):
    odd = []
    even = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    output = [odd,even]
    return output
nums = [1,2,3,4,5,6,7,8,9]
print(filter_odd_even(nums))

# LIST EXAMPLE-6 -------------------------------------------------------------------------
nums = [2,30,20]
print(min(nums))
print(max(nums))
def greatest_diff(l):
    return max(l) - min(l)
print(greatest_diff(nums))

# LIST EXAMPLE-7 -------------------------------------------------------------------------
def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count
mixed = [1,2,3,[3,4],[7,8]]
print(sublist_counter(mixed)) 

# LIST COMPREHENSION ---------------------------------------------------------------------
# with the help of list comprehension we can create list in one line

# example-1
square = [i**2 for i in range(1,11)]
print(square)

# example-2
negative = [-i for i in range(1,11)]
print(negative)

# example-3
names = ['siya','tiya','nia']
new_list = [i[0] for i in names]
print(new_list)

# example-4
def rev_string(l):
    return [i[::-1] for i in l]
print(rev_string(['abc','efg','xyz']))

# example-5 (with if)
even_nums = [i for i in range(1,11) if i%2 == 0]
print(even_nums)
odd_nums = [i for i in range(1,11) if i%2 != 0]
print(odd_nums)

# example-5
# input ------>[True,False,[1,2,3],1,1.0,3]
# output ------>['1','1.0','3']
def num_to_string(l):
    return[str(i) for i in l if (type(i) == int or type(i) == float)]
print(num_to_string([True,False,[1,2,3],1,1.0,3]))

# example-6 (if..else)
new_ex = [i*2 if i%2 == 0 else -i for i in range(1,11)]
print(new_ex)

# example-7 (nested list)
# output ------> [[1,2,3],[1,2,3],[1,2,3]]
nested_comp = [[i for i in range(1,4)] for j in range(3)]
print(nested_comp)