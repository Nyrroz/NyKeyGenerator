""" String generator by Nyrroz"""


import string, random, os

def key_gen(path, length_inbytes):
    prtbl = string.printable
    file = open(path, "w+")
    africa = length_inbytes

    #africa = random.randint(1, 1000000) #Above 10000000 the computer takes too much time to generate

    for i in range(africa):
        file.write(prtbl[random. randint(1, 94)]) #Above 95 there is a space character



length = input("Length in bytes: ")
try:
    key_gen("gen.txt", int(length))
    print("Key successfully generated!\n")
except:
    print("Error!\n")



os.system("pause")