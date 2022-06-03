## creating decorator which super boost the normal function
## to have multiple argument and keyword argument we just need to pass **args and **kwargs in
# wrap function and function in decorator pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('+++++')
        func(*args, **kwargs)
        print('+++++')
    return wrap_func

## Using decorator with the normal function
@my_decorator
def hello():
    print('Hello')

@my_decorator
def bye():
    print('Bye Bye')

#hello()
#bye()

## FUnction with parameter

@my_decorator
def hello_2(greeting, emoji):
    print(greeting + emoji)

hello_2("Bye", ':)')

hello_2()