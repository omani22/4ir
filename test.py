import os

LG = {1: "IOT", 2: "AI", 3: "BIGDATA", 4: "BLOCKCHAIN", 5: '3D'}
DB = {}

pfdir = os.getcwd() + "/files/"


def cnv(xfile):
    global DB, pfdir
    df = open(pfdir + "/" + xfile, encoding="utf8").read()
    df = df.split("كافة الحقوق")
    name = xfile.replace(".txt", "")
    DB[name] = df


def choice():
    xchoice = 0
    contin = False
    while not contin:
        xint = int(input("Choice, -1 to exit : "))
        if xint == -1:
            exit()
        if 1 <= xint <= 5:
            contin = True
            xchoice = xint
    return xchoice


def search(DATABASE):
    while True:
        word = input("Enter word,-1 to exit : ")
        if word == "-1":
            break
        for i in DATABASE:
            if word in i:
                print(i)


def main():
    global pfdir, DB
    onlyfiles = [f for f in os.listdir(pfdir) if os.path.isfile(os.path.join(pfdir, f))]
    for itm in onlyfiles:
        cnv(itm)
    while True:
        print("\t\tWelcome\n\t1. IOT\n\t2. AI\n\t3. BIG DATA\n\t4. BLOCK CHAIN\n\t5. 3D PRINTING")
        search(DB[LG[choice()]])


main()
