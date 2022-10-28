#function is defined as the collection of code used to perform a task.
# import core concept in python
#key word is def
# any fn inside the code needs to be indented.
def say_hello():
    print("Helllo User")

say_hello() # fn name can be either string or a number and an also be in upper o lower case.

def Say_hi_2_me():
    print("Hi Prasanth")
Say_hi_2_me()

def Hi(name): #here name is the parameter which we are giving beforehand.
    print("hello "+name)
Hi("Luffy")
Hi("Zorro")
Hi("Jinbei")
print("\n")

def position(name, age, position):
    print("hello Mr." +name+ ",")
    print("you are "+age+ " years old,") # or we can use age as str(age) to makeit a string.
    print("you are the "+position+ " of the ship.")

position("luffy","17","captain")
print("\n")
position("Zorro",str(21),"vice captain")
print("\n")
