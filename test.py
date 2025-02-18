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


class segtree:

    def __init__(self , n , function=max, bound=0):

        self.st = [bound] * (2 * n)
        self.size = n
        self.function = function
        self.bound = bound
 
    def update(self , x , value):

        x += self.size

        self.st[x] = value

        while(x > 1):
            
            x >>= 1
            self.st[x] = self.function(self.st[2 * x] , self.st[2 * x + 1])
 
    def query(self , x , y):

        x += self.size
        y += self.size + 1

        ans = self.bound
        while(x < y):

            if(x & 1):
                ans = self.function(ans , self.st[x])

                x += 1

            if(y & 1):

                y -= 1

                ans = self.function(ans , self.st[y])

            x //= 2
            y //= 2

        return ans


n, q = ints()
a = ints()

queries = [ints()[::-1] for i in range(q)]

sorted_queries = sorted(queries, reverse=True)

store = {}
for i in range(n):
    if a[i] not in store:
        store[a[i]] = []
    store[a[i]].append(i)

ans = {}

st = segtree(n)

minn = min(a)

for v in sorted(store.keys()):
    while sorted_queries and sorted_queries[-1][0] < v:
        x, y = sorted_queries.pop()
        ans[(x, y)] = st.query(0, y-1)

    inds = store[v]
    while inds:
        i = inds.pop()
        maxx = st.query(0, i)
        st.update(i, maxx + 1)


while sorted_queries:
    x, y = sorted_queries.pop()
    ans[(x, y)] = st.query(0, y-1)

for x, y in queries:
    print(ans[(x, y)])