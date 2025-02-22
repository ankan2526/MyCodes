# author: ankan2526
 
import sys,math,heapq,bisect,random,itertools
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
 
ints = lambda : list(map(int,input().split()))
def gprint(ans=''):global t;print(f"Case #{t+1}:",ans)
p = 10**9+7
inf = 10**20+7
adj = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = "abcdefghijklmnopqrstuvwxyz"
ANS = []



'''
'''

n = int(input())

a = [input().strip() for i in range(n)]

ans = [[inf for i in range(n)] for j in range(n)]

for i in range(n):
    ans[i][i] = 0

for i in range(n):
    for j in range(n):
        if a[i][j] != '-' and i != j:
            ans[i][j] = 1

for i in range(n):
    for j in range(n):
        if i == j:
            ans[i][j] = 0
            continue

        visited = [[False for i in range(n)] for j in range(n)]
        visited[i][j] = True

        queue = [(i, j, 0)]
        found = False
        while queue:
            q = []
            for x, y, l in queue:
                if ans[x][y] != inf:
                    if ans[x][y] == -1:
                        continue
                    else:
                        ans[i][j] = min(ans[i][j], l+ans[x][y])
                        found = True
                        continue
                for u in range(n):
                    if u == y and a[x][u] != '-' and not visited[u][y]:
                        ans[i][j] = min(l+1, ans[i][j])
                        found = True
                        q.append((x, u, l+1))
                    for v in range(n):
                        if a[x][u] == a[v][y] and a[x][u] != '-' and not visited[u][v]:
                            visited[u][v] = True
                            if u == v:
                                ans[i][j] = min(l+2, ans[i][j])
                                found = True
                            q.append((u, v, l+2))
            if found:
                break
            queue = q
        
        if not found:
            ans[i][j] = -1

for i in range(n):
    print(*ans[i])