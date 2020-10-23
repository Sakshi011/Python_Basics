# ESCAPE SEQUENCE -----------------------------------------------------------------------
print("this is \\\\ double backshash")
print("these are /\\/\\/\\/\\ mountains")
print("She is\tawesome")
print(" \\\" \\n \\t \\\' ")

# USER INPUT - INPUT() -------------------------------------------------------------------
num_one = input("enter first number: ")
num_two = input("enter second number: ")
num_one = int(num_one) # converted number(str) to int
num_two = int(num_two) # converted number(str) to int
print(num_one,num_two)

# VARIABLES ------------------------------------------------------------------------------
name,age = "Sakshi","19"
print("hello " + name + " your age is " + age)
x=y=z=1
print("sum of x y and z is: " + str(x+y+z)) # converted int to str

# TWO INPUTS FROM USER ------------------------------------------------------------------------
name,age = input("enter your name and age(comma seprated): ").split(",") # comma seprated input
print(name)
print(age)

# STRING ---------------------------------------------------------------------------------------
# STRING FORMATTING 
name,age = "Sakshi",19
print("hello {} your age is {} ".format(name,age)) #PYTHON 3
print(f"hello {name} your age is {age}") # PYTHON 3.6

# STRING INDEXING
language = "python"
print(language[3])

# STRING SLICING
lang = "python"
# syntax - [start argument : stop argument : step]
print(lang[1:4:2])

# STRING METHODS
name = "Sakshi poojaRa"
dots = "............"
# FIND LENGTH
length = len(name)
print(length)
# UPPERCASE
print(name.upper())
# LOWERCASE
print(name.lower())
# TITLE
print(name.title())
# COUNT
print(name.count("s"))
# STRIP
print(name.strip() + dots)
 
# USE OF THESE FUNCTIONS --------------------------------------------------------------
name,char = input("enter comma seprated name and character: ").split(",")
print(f"length of ypur name is {len(name)}")
print(f"char count: {name.strip().lower().count(char.strip().lower())}")

# FIND AND REPLACE --------------------------------------------------------------
string = "she is beatiful and is good dancer"
print(string.replace("is", "was", 2))
is_pos1 = string.find("is")
is_pos2 = string.find("is", is_pos1 + 1)
print(is_pos2)

# CENTER METHOD ------------------------------------------------------------------
name = input("enter your name: ")
print(name.center(len(name)+12, "*"))

#STRINGS ARE IMMUTABLE ------------------------------------------------------------
name = "sakshi"
new_name = string.replace("s", "S")
print(new_name)
name *= 5 # assignment operator
print(name + " ")

# IF-ELSE --------------------------------------------------------------------------
age = int(input("Enter your age: "))
if age > 18:
    print("your are elegeble")
else:
    print("you are not elegeble")

# ELIF STATEMENT --------------------------------------------------------------------
per = int(input("enter percentage: "))
if 80<per<100:
    print("Congrats! First class")
elif 60<per<80:
    print("Congrats! second class")
elif 30<per<60:
    print("Pass!")
else:
    print("FAIL!")

# IN KEYWORD -------------------------------------------------------------------------
string = input("enter name: ")
if 'a' in string:
    print("a is present in string")
else:
    print("oops! a is not present in string")

# CHECK STRIBG IS EMPTY OR NOT --------------------------------------------------------
string = input("enter name: ")
if name: # true if string is not empty
    print("String is not emppty")
else:
    print("oops! string is empty")

# WHILE LOOP --------------------------------------------------------------------------
i=1
while i<=5:
    print(f"while loop {i}")
    i +=1

# WHILE LOOP-EXAMPLE(sum of 1-10) ------------------------------------------------------
sum = 0
i = 1
while i<=10:
    sum += 1
    i += 1
print(f"sum is: {sum}")

# FOR LOOP WITH RANGE FUNCTION ----------------------------------------------------------
for i in range(1,6):
    print(f"for loop {i}")

# FOR LOOP-EXAMPLE(SUM OF DIGITS OF A NUMBER) -------------------------------------------
sum2 = 0
num = input("enter a number: ")
for i in range(0, len(num)):
    sum2 += int(num[i])
print(sum2) 

# BREAK AND CONTINUE --------------------------------------------------------------------
for i in range(1, 11):
    if i == 5:
        break
    print(i)

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# STEP IN LOOPING -----------------------------------------------------------------------
for i in range(1,-11,-1):
    print(i)

# FUNCTION  example-1 -------------------------------------------------------------------
def add_two(a,b):
    return a+b
a = int(input("enter first number: "))
b = int(input("enter second number: "))
total = add_two(a,b)
print(total)
 
# FUNCTION  example-2 -------------------------------------------------------------------
def last_char(name):
    return name[-1]
print(last_char("Sakshi poojara"))

# FUNCTION  example-3 -------------------------------------------------------------------
def odd_even(num):
    if num%2 == 0:
        return "even"
    return "odd"
print(odd_even(10))

# FUNCTION  example-4 -------------------------------------------------------------------
def new_greatest(a,b,c):
    bigger = max(a,b)
    return max(bigger,c)
print(new_greatest(10,200,30))

# FUNCTION  example-6 ------------------------------------------------------------------
def fibbo_sec(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b)
    else:
        print(a,b, end = " ")
        for i in range(n-2):
            c = a+b
            a = b
            b = c
            print(b, end = " ")
fibbo_sec(20)

# DEFAULT PARAMETERS ------------------------------------------------------------------
def user_info(first_name = "sakshi", last_name = "unknown", age=13):
    print(f"your fname is: {first_name}")
    print(f"your lname is: {last_name}")
    print(f"your age is: {age}")
user_info()

# SCOPE ---------------------------------------------------------------------------------
x = 5
def fun():
    global x
    x = 7 # local var
    return x
print(x)
print(fun())
print(x)