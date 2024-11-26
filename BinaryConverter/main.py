#
#   /!\ A n'utiliser que sur la calculatrice
#

while True:
    try:
        nb = input("Choisissez un nombre (0x pour hex et 0b pour bin) : ")
        print("Binaire :", bin(int(nb)))
        print("Hexadécimal :", hex(int(nb)))
        print("Décimal :", int(nb))
    except:
        if nb == "":
            break
