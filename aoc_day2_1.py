X=1
Y=2
Z=3
sol=0
while(True):
    try:
        a,b=input().split()
        if(a=="A"):
            if(b=="X"):
                sol=sol+X+3
            elif(b=="Y"):
                sol=sol+Y+6
            else:
                sol=sol+Z+0
        elif(a=="B"):
            if(b=="X"):
                sol=sol+X+0
            elif(b=="Y"):
                sol=sol+Y+3
            else:
                sol=sol+Z+6
        else:
            if(b=="X"):
                sol=sol+X+6
            elif(b=="Y"):
                sol=sol+Y+0
            else:
                sol=sol+Z+3
    except EOFError:
        print(sol)
        break
