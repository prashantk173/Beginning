#here vowels will be written as g
#for eg. cat -> cgt and dog-> dgg
#lets cal it Giraffee translator.
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("enter the phrase: ")))