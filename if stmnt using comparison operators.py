# divisibility by 3
def by3(num):
    if num % 3 == 0:
        print(str(num) + " is divisible by 3", "by", str((num / 3)))
    else:
        print(str(num) + " is not divisible by 3")


by3(9876543210)


# comparison operators
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(str(max_num(1,17,7))+ " is the maximum nummber.")
