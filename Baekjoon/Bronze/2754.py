import sys
input = sys.stdin.readline

N= input()
scroe = 0.0

if(N[0]=='A'):
    scroe = 4.0
elif(N[0]=='B'):    
    scroe = 3.0
elif(N[0]=='C'):
    scroe = 2.0
elif(N[0]=='D'):
    scroe = 1.0
else:
    scroe = 0.0

if(N[1]=='+'):
    scroe += 0.3
elif(N[1]=='-'):
    scroe -= 0.3
    
print(scroe)