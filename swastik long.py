
i=1
j=73
k=1
space_last=5
middle=[8,9,10,11,23,24,25,26]
star2=[8,11,23,26]
star4=[9,10,24,25]
print()
print()
print()
for a in range (1,6) :
        for space in range(40):
                print(" ", end="")
        for b in range(a):
                print(" ", end="")
        for c in range(i):
                print("*", end="")
        i = i+1
        for d in range (j):
                print(" ",end="")
        j=j-4
        for e in range (k):
                print("*",end="")
        k=k+1
        print("")
for a in range(33):
        for space in range(40):
                print(" ", end="")
        for b in range(6):
                print(" ",end="")

        if a<18:
                for c in range(6):
                        print("*", end="")
        elif a>=18 and a<30:
                for c in range(6):
                        print(" ", end="")
        else:
                for c in range(6):
                        print("*", end="")

        if a<15 and (a not in middle) :
                for c in range(24):
                        print(" ", end="")
        elif a in middle:
                if a in star2:
                        for c in range(11):
                                print(" ", end="")
                        print("**",end="")
                        for c in range(11):
                                print(" ", end="")
                else:
                        for c in range(10):
                                print(" ", end="")
                        print("****",end="")
                        for c in range(10):
                                print(" ", end="")
        elif a>=15 and a<18:
                for c in range(24):
                        print("*", end="")
        elif a>=18 and a<30 and (a not in middle):
                for c in range(24):
                        print(" ", end="")
        else:
                for c in range(24):
                        print("*", end="")

        for c in range(6):
                 print("*", end="")

        if a<3:
                for c in range(24):
                        print("*", end="")
        elif a>=3 and a<15 and (a not in middle) :
                for c in range(24):
                        print(" ", end="")
        elif a in middle:
                if a in star2:
                        for c in range(11):
                                print(" ", end="")
                        print("**",end="")
                        for c in range(11):
                                print(" ", end="")
                else:
                        for c in range(10):
                                print(" ", end="")
                        print("****",end="")
                        for c in range(10):
                                print(" ", end="")
        elif a>=15 and a<18:
                for c in range(24):
                        print("*", end="")
        else :
                for c in range(24):
                        print(" ", end="")


        if a<3:
                for f in range(6):
                        print("*", end="")
        elif a>=3 and a<15:
                for f in range(6):
                        print("", end="")
        elif a>=13:
                for f in range(6):
                        print("*", end="")
        print("")
j=57
for a in range (1,6) :
        for space in range(40):
                print(" ", end="")
        for b in range(space_last):
                print(" ", end="")
        space_last = space_last-1
        i=i-1
        for c in range(i):
                print("*", end="")
        for d in range (j):
                print(" ",end="")
        j=j+4
        k=k-1
        for e in range (k):
                print("*",end="")
        print("")
print()
print()
print()

