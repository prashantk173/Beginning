# return fn, it is used to call the back the value which is mentioned in the fn.

def cube(num):
    return num**3 # after the return keyword there is no other function which will be executed.

print(cube(7))

def odd_or_even(num):
    if num % 2 == 1:
        print(str(num)+ " is a Odd number")
    else:
        print(str(num)+ " is a even number")
odd_or_even(16)
odd_or_even(17)