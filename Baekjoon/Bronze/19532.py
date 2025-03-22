import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

x = -1000
y = -1000
found = False

for i in range(-999, 1000):
    if b != 0:
        j = (c - a * i) // b
        if a * i + b * j == c and d * i + e * j == f:
            x = i
            y = j
            found = True
            break
    else:
        if a * i == c:
            for j in range(-999, 1000):
                if d * i + e * j == f:
                    x = i
                    y = j
                    found = True
                    break
    if found:
        break

print(x, y)
