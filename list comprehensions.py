# list, dictionary or set

#str = input("Give me any string: ")
str_list = []

#for x in str:
    #str_list.append(x)

#print(str_list)

# Now using list comprehension to do the same thing with less code
# formula : my_list = [ param for param in iterable condition]
#str_list_2 =[ char for char in str]
#print(str_list_2)

my_list = [num ** 2 for num in range(0,100)]
print(my_list)

# print only the even number of square of range (0,100)

my_list_even = [num ** 2 for num in range(0,100) if num % 2 == 0]

print(my_list_even)

# dictionary comprehension

simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(simple_dict)
my_dict = {k: v**2 for k, v in simple_dict.items() if v**2 > 5} # k= Key and V= value
print(my_dict)

