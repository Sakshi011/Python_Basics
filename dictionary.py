# Dictionary is unordered collection of data in key-value pair

# CREATE DICTIONARY ---------------------------------------------------------------------
user = {'name':'Sakshi', 'age':19}
print(user)
print(type(user))
print("\n")
# second method --------------------------------------------------------------------------
user1 = dict(name = 'Sakshi', age = 19)
print(user1)
print(user['name'])
print(user['age'])
print("\n")
user_info = {
    'name':'sakshi',
    'age':19,
    'fav_movies':['coco','kimi no na wa'],
    'fav_tunes':['awakening','fairy tale']
}
print(user_info['fav_movies'])
print("\n")

# IN KEYWORD------------------------------------------------------------------------------
if 'name' in user_info:
    print('present')
else:
    print('not present')
print("\n")
# for values
if 'sakshi' in user_info.values():
    print('present')
else:
    print('not present')
print("\n")

# for loop -------------------------------------------------------------------------------
for i in user_info.values():
    print(i)
for i in user_info:
    print(user_info[i])
print("\n")

# VALUES MATHOD -------------------------------------------------------------------------
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))
print("\n")

user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))
print("\n")

# ITEMS METHOD --------------------------------------------------------------------------
user_items = user_info.items()
print(user_items)
print(type(user_items))
print("\n")

for key,value in user_items:
    print(f"key is {key} and value is {value}")
print("\n")

# ADD DATA -------------------------------------------------------------------------------
user_info2 = {}
user_info2['name'] = 'sakshi'
user_info2['fav_songs'] = ['song1','song2']
user_info2['fav_tunes'] = ['tune1','tune2']
user_info2['fav_movies'] = ['movie1','movie2']
print(user_info2)
print("\n")

# POP METHOD -----------------------------------------------------------------------------
popped_item = user_info2.pop('fav_songs')
print(f"popped item is {popped_item}") # here type of popped_item is list
print(user_info2)
print("\n")

# POPITEM METHOD -------------------------------------------------------------------------
popped_item = user_info2.popitem()
print(popped_item)
print(user_info2)
print("\n")

# UPDATE() METHOD ------------------------------------------------------------------------
more_info = {'name':'sakshii','state':'gujarat','fav_fruits':['fruit1','fruit2']}
user_info.update(more_info)
print(user_info)
print("\n")

# FROMKEYS -------------------------------------------------------------------------------
# d = {'name':'unknown','age':'unknown'}
d = dict.fromkeys(['name','age','height'],'unknown')
d = dict.fromkeys('abc','unknown')
print(d)
print("\n")

# GET METHOD -----------------------------------------------------------------------------
# print(d['age'])
print(user_info.get('name'))
# print(d['names']) # error
print(d.get('name')) # none
if d.get('name'):
    print('present')
else:
    print('not present')
print(user_info.get('fav','not found'))
print("\n")

# COPY METHOD ----------------------------------------------------------------------------
d1 = d.copy()
d1 = d
print(d)
print(d1)
print("\n")

# CLEAR METHODS --------------------------------------------------------------------------
d.clear()
print(d)
print("\n")

# EXAMPLE-1 ------------------------------------------------------------------------------
def cube_finder(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes
print(cube_finder(10))
print("\n")

# EXAMPLE-2 ------------------------------------------------------------------------------
def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count
print(word_counter('sakshi'))
print("\n")

# EXAMPLE-3(user input) ------------------------------------------------------------------
user = {}
name = input('enter name')
age = input('enter age')
fav_songs = input('enter favorite songs(comma seprated)').split(',')

user['name'] = name
user['age'] = age
user['fav_songs'] = fav_songs

for key,value in user.items():
    print(f"{key} : {value}")
print("\n")

# DICTIONARY COMPREHENSION ---------------------------------------------------------------
# ex-1
square = {num:num**2 for num in range(1,11)}
print(square)
print(type(square))

# print("\n")
# ex-2
string = "sakshi"
word_count = {char:string.count(char) for char in string}
print(word_count)

