# tuple data type-tuples are ordered collections of items
# tuple can store any data type
# once tuple is created you can't update
# tuples are faster than list

# INTRO---------------------------------------------------------------------------------
nums = ('one','two','three')
print(nums)
print(nums[:2])
print(type(nums))

# FOR LOOP-------------------------------------------------------------------------------
mixed = (1,2,3,4.0)
for i in mixed:
    print(i)

# TUPLE WITH ONE ELEMENT-----------------------------------------------------------------
num = (1)       #it is not tuple
print(type(num))
num = (1,)      # it is tuple
print(type(num))

# TUPLE WITHOUT PARENTHESIS -------------------------------------------------------------
words = 'word1', 'word2', 'word3'
print(type(words))

# TUPLE UNPACKING ------------------------------------------------------------------------
fruits = ('apple', 'mango', 'grapes')
fruit1, fruit2, fruit3 = (fruits)
print(fruits)

# LIST INSIDE TUPLE ----------------------------------------------------------------------
fruits = ('apple', ['mango', 'grapes'])
print(fruits[1].pop())
fruits[1].append('banana')
print(fruits)

# FUNCTION RETURNING TWO VALUES ----------------------------------------------------------
def func(num1, num2):
    add = num1 + num2
    multi = num1*num2
    return add,multi
add, multi = func(2,3)
print(add)
print(multi) 