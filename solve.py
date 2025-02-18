'''
calculate answer for every subarray
'''

class fenwicktree:

    def __init__(self , n):
        self.BITTree = [0] * (n + 1)
        self.size = n

    def getsum(self , i):
        s = 0 
        i = i+1
        while i > 0:
            s += self.BITTree[i]
            i -= i & (-i)

        return s

    def query(self , l , r):
        if l > r:
            return 0

        return self.getsum(r) - self.getsum(l - 1)
 
    def update(self , i , v):
   
        i += 1
        while i <= self.size:
            self.BITTree[i] += v
            i += i & (-i)



def solve(left, right):
    if left >= right:
        return 0
    if dp[left][right] != -1:
        return dp[left][right]
    
    ans = 0
    maxx = 0

    global n
    ft = fenwicktree(n+1)
    for i in range(left+1, right+1):
        ft.update(a[i], 1)
    
    for i in range(left+1, right):
        ft.update(a[i], -1)
        maxx = max(maxx, a[i-1])
        c = ft.query(a[i], maxx)
        c += solve(left, i-1) + solve(i+1, right)
        ans = max(ans, c)
    dp[left][right] = ans
    return ans

n = int(input())
a = [int(input()) for i in range(n)]
dp = [[-1 for i in range(n)] for j in range(n)]

print(solve(0, n-1))
