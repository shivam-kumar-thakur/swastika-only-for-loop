def space(howmanytimes):
        for i in range(howmanytimes):
                print(" ", end="")
def stars(howmanystars):
        for i in range(howmanystars):
                print("*", end="")


i=1
j=74
k=1
space_last=5
middle=[8,9,10,11,23,24,25,26]
star2=[8,11,23,26]
star4=[9,10,24,25]
print()
print()
print()
for a in range (1,6) :
        space(40)
        #for space in range(40):
        #        print(" ", end="")
        space(a)
        #for b in range(a):
        #        print(" ", end="")
        stars(i)
        #for c in range(i):
        #        print("*", end="")
        i = i+1
        space(j)
        #for d in range (j):
        #        print(" ",end="")
        j=j-4
        stars(k)
        #for e in range (k):
        #        print("*",end="")
        k=k+1
        print("")
for a in range(33):
        space(40)
        #for space in range(40):
        #        print(" ", end="")
        space(6)
        #for b in range(6):
        #        print(" ",end="")

        if a<18:
                stars(6)
                #for c in range(6):
                #        print("*", end="")
        elif a>=18 and a<30:
                space(6)
                #for c in range(6):
                #        print(" ", end="")
        else:
                stars(6)
                #for c in range(6):
                #        print("*", end="")

        if a<15 and (a not in middle) :
                space(24)
                #for c in range(24):
                #        print(" ", end="")
        elif a in middle:
                if a in star2:
                        space(11)
                        #for c in range(11):
                        #        print(" ", end="")
                        print("**",end="")
                        space(11)
                        #for c in range(11):
                        #        print(" ", end="")
                else:
                        space(10)
                        #for c in range(10):
                        #        print(" ", end="")
                        print("****",end="")
                        space(10)
                        #for c in range(10):
                        #        print(" ", end="")
        elif a>=15 and a<18:
                stars(24)
                #for c in range(24):
                #        print("*", end="")
        elif a>=18 and a<30 and (a not in middle):
                space(24)
                #for c in range(24):
                #        print(" ", end="")
        else:
                stars(24)
                #for c in range(24):
                #        print("*", end="")
        stars(6)

        #for c in range(6):
        #         print("*", end="")

        if a<3:
                stars(24)
                #for c in range(24):
                #        print("*", end="")
        elif a>=3 and a<15 and (a not in middle) :
                space(24)
                #for c in range(24):
                #        print(" ", end="")
        elif a in middle:
                if a in star2:
                        space(11)
                        #for c in range(11):
                        #        print(" ", end="")
                        print("**",end="")
                        space(11)
                        #for c in range(11):
                        #        print(" ", end="")
                else:
                        space(10)
                        #for c in range(10):
                        #        print(" ", end="")
                        print("****",end="")
                        space(10)
                        #for c in range(10):
                        #        print(" ", end="")
        elif a>=15 and a<18:
                stars(24)
                #for c in range(24):
                #        print("*", end="")
        else :
                space(24)
                #for c in range(24):
                #        print(" ", end="")


        if a<3:
                stars(6)
                #for f in range(6):
                #        print("*", end="")
        elif a>=3 and a<15:
                space(6)
                #for f in range(6):
                #        print(" ", end="")
        elif a>=13:
                stars(6)
                #for f in range(6):
                #        print("*", end="")
        print("")
j=57
for a in range (1,6) :
        space(40)
        #for space in range(40):
        #        print(" ", end="")
        space(space_last)
        #for b in range(space_last):
        #        print(" ", end="")
        space_last = space_last-1
        i=i-1
        stars(i)
        #for c in range(i):
        #        print("*", end="")
        space(j)
        #for d in range (j):
        #        print(" ",end="")
        j=j+4
        k=k-1
        stars(k)
        #for e in range (k):
        #        print("*",end="")
        print("")
print()
print()
print()



