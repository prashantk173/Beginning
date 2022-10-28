def power(base, pow):
    return base ** pow
print(power(20,4))

def power_2(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    print(result)

power_2(4,2)

twodlist = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
for w in twodlist:
    for e in w:
        print(e) # nested for loops.