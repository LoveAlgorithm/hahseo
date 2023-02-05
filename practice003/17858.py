import sys
n, m, a, c, x0 = map(int, sys.stdin.readline().rstrip().split())

x = [x0 for _ in range(n+1)]
for i in range(1, n+1):
    x[i] = ((a * x[i-1] + c) % m)

# x = x[1:]

cnt = 0
for num in range(1, n+1):
    lo, hi = 0, n-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if x[mid] == x[num]:
            cnt += 1
            break
        elif x[mid] < x[num]:
            lo = mid + 1
        else:
            hi = mid - 1

print(cnt)
