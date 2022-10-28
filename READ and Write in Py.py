# opening the file

open("pirate", "r")  # only we can read the file
open("pirate", "w")  # only we can write in the file modify the file
open("pirate", "a")  # we can only add data to the file we cannot read or modify the file.
open("pirate", "r+")  # with this we can do both read and write with this file.

pirate_crew = open("pirate", "r")  # for opening the file
pirate_crew.close()  # for closing the file.

pirate_crew = open("pirate.txt", "r")
print(pirate_crew.readable())  # says whether the file is readable or writable by giving a boolean value.
print(pirate_crew.read())  # reads the whole file
print(pirate_crew.readline())  # Reads only the first line of the file
print(pirate_crew.readlines())  # reads all the lines as a list and we can call the lines using the list grabbing fn.

pirate_crew = open("pirate.txt", "r")
print(pirate_crew.readlines()[2])

pirate_crew = open("pirate.txt", "r")
for pirate in pirate_crew.readlines():
    print(pirate)

pirate_crew.close()

# Writing and appending in the file.

pirate_crew = open("pirate.txt", "a")  # adding text at the end of the file.

pirate_crew.write("\nYamato - Kaizo's daughter")  # use \n for adding in the next line.
# \n Special characters called as escape characters.

pirate2 = open("pirate", "w")
pirate2.write("Chopper has the least bounty")  # erases the whole content of the files and writes as a new file.

pirate3 = open("pirate1.txt", "w")
pirate3.write("Kaizoku oh orewa oni naru")  # creating a new file.

pirate4 = open("pirate1.html", "r+")
pirate4.write("<p>Hello straw hats</p>")
print(pirate4.read())

# Modules in Python
