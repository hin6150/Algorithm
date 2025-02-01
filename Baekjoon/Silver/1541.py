import sys
import re

input = sys.stdin.readline

arr = re.split(r'([+-])', input().strip())

while(arr.count('+') > 0):
    index = arr.index('+')
    temp = int(arr[index+1]) + int(arr[index-1])
    arr.pop(index-1)
    arr.pop(index-1)
    arr.pop(index-1)
    arr.insert(index-1, temp)

answer = int(arr[0])
for i in range(2, len(arr), 2):
    answer -= int(arr[i])

print(answer)