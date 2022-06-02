## the Pure function should have two conditions

# Do not interact with outside world like printing or changing any variable
# Everytime it gives the same result

# creating normal function

def twotimes(li):
    new_list = []
    for item in li:
        new_list.append(item*2)

    return new_list


#print(twotimes([3,4,5]))


# using map()
## Used a lot in the programming


## print(map(twotimes, [3,4,5])) # it gives the location of the result object to see list we need to write list

## print(list(map(twotimes, [5,6,4]))) # in map function we dont even need to create empty list

def twotime2(item): ## to use any function with map, we give what will be the out put Map will take care of iterations
    return item * 2
my_list=[23,4,5,63,21,53,98]
print(f'Result of Map function{list(map(twotime2,my_list))}')


## Using filter on functions:

# it checks the result of the function return, and prints it if the resultin TRUE , it works on the boolean
## return of the function should be boolean

# For Example create afunction which checks odd in a list:

def only_odd(item):
    return item % 2 != 0

print(f'Result of Filter Function{list(filter(only_odd, my_list))}') ## this is only keeping the odd values of list provided


# Using ZIP Function:

# take two or more iterable and zip them together and create tuple of 1st item of two iterables and so on

age = [2,3,4]
name = ['Papu','raja','chacha']

print(f'gives the combine of two iterables --> {list(zip(name,age))}')