# Basic Variables Naming Rules

# 1. Start with a letter or underscore (a-z, A-Z)(_)
age = 32
_secret = "Shh!"
# 2fast = "Speedy!" # This will cause an error

# 2. Use letters, numbers, or underscores (az, a_)
user_age_2 = 30
best_friend_1 = "Alice"
# my-variable = 10 # Hypens are not allowed

# 3. Case-sensitive (az, aZ, Az, a_)
Age = 32
age = 32
AGE = 32

print(Age)
print (age)
print (AGE)

# 4. No reserved words (from, del)
# from = "Boston" # can't be declared a variable
# if = 5 # can't be declared a variable
# print = "Hello" # can't be declared a variable

# Best practices.
# 1. Be descriptive.
user_age = 32
a = 32 # Not good, what does 'a' mean?

# 2. Use underscores for spaces.
first_name = "John"
last_name = "Smith"
firstname = "John"  # not readable
lastname = "Smith"  # not readable

# 3. Keep it simple
max_speed = 100 # Excellent
maximum_car_speed_on_highway = 150 # Too long

# Common mistakes
# 1. starting with a number
# 1st_place = "gold" # Cant start with a number

# 2. Using spaces
# my variable = 10 # Incorrect

# 3. Using special characters
user@mail = 'mymail@mydomain.com' # Incorrect