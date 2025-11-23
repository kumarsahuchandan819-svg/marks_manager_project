# Name : Chandan Kumar sahu
# Registration Number : 25MIM10179

import os

data = []
if os.path.exists("marks.txt"):
    f = open("marks.txt","r")
    for l in f:
        l = l.strip()
        if "|" in l:
            t = l.split("|")
            if len(t) == 2:
                mk = t[1]
                if mk.replace( "." , "" ,1).isdigit():
                    data.append([t[0], float(mk)])
    f.close()


def add():
    n = input("Student name : ").strip()
    m = input("Marks : ").strip()

    if m.replace( "." , "" ,1).isdigit():
        m = float(m)
    else:
        print("Invalid\n")
        return

    data.append([n, m])

    g = open("marks.txt","w")
    for x in data:
        g.write(x[0] + "|" + str(x[1]) + "\n")
    g.close()

    print("OK\n")


def view():
    if len(data) == 0:
        print("none\n")
        return

    for s in data:
        print(s[0], s[1])
    print()


def avg():
    if len(data) == 0:
        print("No data\n")
        return

    total = 0
    for a in data:
        total += a[1]

    print("Avg:", total / len(data), "\n")

while True:
    print("1 Add  2 View  3 Avg  4 Exit")
    c = input("Choice: ").strip()

    if c == "1":
        add()
    elif c == "2":
        view()
    elif c == "3":
        avg()
    elif c == "4":
        break
    else:
        print("Wrong\n")