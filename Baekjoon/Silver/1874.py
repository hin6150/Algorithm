import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input().strip()) for i in range(N)]
temp = [i for i in range(N+1)]

idx = 0
i = 0

answer = []

while(1):
    if temp[idx] != arr[i]:
        idx+=1
        answer.append("+")
        
        if(idx >= len(temp)):
            break
        
    elif temp[idx] == arr[i]:
        temp.pop(idx)
        idx-=1
        i+=1
        answer.append("-")
        
        if(temp == [0]):
            break

if(idx >= len(temp)):
    print("NO")
else:
    for i in range(len(answer)):
        print(answer[i])