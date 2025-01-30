import math
import sys
input = sys.stdin.readline

def round_up_half(number):
    return math.floor(number + 0.5)

N = int(input())
value = round_up_half(N*.15)
arr =[]

for idx in range(N):
    arr.append(int(input()))

if N == 0:
    print(0)
else:
    arr.sort()
    finalArr=arr[0+value : len(arr)-value]
    print(round_up_half(sum(finalArr) / len(finalArr)))
    
