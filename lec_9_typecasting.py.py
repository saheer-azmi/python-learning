# Typecasting Practice Program by Saheer Azmi

# 1. String to Integer
string_number = "25"
print("Before typecasting (string):", string_number, type(string_number))
int_number = int(string_number)
print("After typecasting (int):", int_number, type(int_number))
print()

# 2. Integer to String
integer_value = 100
print("Before typecasting (int):", integer_value, type(integer_value))
string_value = str(integer_value)
print("After typecasting (string):", string_value, type(string_value))
print()

# 3. Float to Integer
float_value = 45.67
print("Before typecasting (float):", float_value, type(float_value))
int_from_float = int(float_value)
print("After typecasting (int):", int_from_float, type(int_from_float))
print()

# 4. Integer to Float
int_value = 8
print("Before typecasting (int):", int_value, type(int_value))
float_from_int = float(int_value)
print("After typecasting (float):", float_from_int, type(float_from_int))
print()

# 5. String to Float
str_float = "9.81"
print("Before typecasting (string):", str_float, type(str_float))
float_value = float(str_float)
print("After typecasting (float):", float_value, type(float_value))
print()

# 6. Value to Boolean
empty_string = ""
non_empty_string = "Python"
zero_number = 0
non_zero_number = 7

print("Empty string to bool:", bool(empty_string))      # False
print("Non-empty string to bool:", bool(non_empty_string))  # True
print("Zero to bool:", bool(zero_number))                # False
print("Non-zero number to bool:", bool(non_zero_number))  # True
print()

# Bonus: User input example
user_input = input("Enter any number: ")
print("Data type before typecasting:", type(user_input))

user_input_int = int(user_input)
print("Data type after typecasting:", type(user_input_int))
print("Double the number:", user_input_int*2)