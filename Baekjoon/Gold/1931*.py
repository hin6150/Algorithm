# 그리디 - 정렬기준이 중요하다. 어차피 빨리 끝나면 다음 화의를 잡을 수 있기에
# 다시풀기

import sys
input = sys.stdin.readline

N = int(input().strip())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[0]))

last_end = 0
count = 0
for s, e in arr:
    if s >= last_end:
        count += 1
        last_end = e
    
print(count)
