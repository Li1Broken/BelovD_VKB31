from itertools import combinations

n, r, c = map(int, input().split())
n = [int(input()) for line in range(n)]

print(min(max(x[(i + 1) * c - 1] - x[i * c] for i in range(r))
          for x in map(sorted, combinations(n, r * c))))
