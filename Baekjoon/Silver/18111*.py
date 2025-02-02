import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
freq = [0] * 257  # 0 ~ 256 높이별 블록 개수

for _ in range(N):
    for height in map(int, input().split()):
        freq[height] += 1
print(freq)
# prefix[i]: 0 ~ i까지의 블록 개수 합
# prefix_sum[i]: 0 ~ i까지 (높이 * 개수) 합
prefix = [0] * 257
prefix_sum = [0] * 257
prefix[0] = freq[0]
prefix_sum[0] = 0  # 0 * freq[0]
for i in range(1, 257):
    prefix[i] = prefix[i - 1] + freq[i]
    prefix_sum[i] = prefix_sum[i - 1] + i * freq[i]

best_time = float('inf')
best_height = 0

# h를 256부터 0까지 확인 (동일 시간일 경우 더 높은 h 선택)
for h in range(256, -1, -1):
    # 추가해야 할 블록 수:
    # h보다 낮은 높이의 블록들을 h로 맞추려면: sum_{i=0}^{h-1} (h - i)*freq[i]
    add = h * (prefix[h - 1] if h > 0 else 0) - (prefix_sum[h - 1] if h > 0 else 0)

    # 제거해야 할 블록 수:
    # h보다 높은 높이의 블록들을 h로 맞추려면: sum_{i=h+1}^{256} (i - h)*freq[i]
    removal = (prefix_sum[256] - prefix_sum[h]) - h * (prefix[256] - prefix[h])
    
    # 제거한 블록과 현재 인벤토리로 추가할 블록을 보충할 수 있어야 함
    if removal + B < add:
        continue

    time = removal * 2 + add  # 제거: 2초, 추가: 1초
    if time < best_time:
        best_time = time
        best_height = h

print(best_time, best_height)
