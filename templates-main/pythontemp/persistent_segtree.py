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

"""
"""


def add(a, b):
    return a + b

class PersistentSegmentTree:
    def __init__(self, left_ind, right_ind, function=add, bound=0) -> None:
        self.left_ind = left_ind
        self.right_ind = right_ind
        self.function = function
        self.bound = bound
        self.value = bound

        if left_ind == right_ind:
            self.left = None
            self.right = None
        
        else:
            mid = (left_ind + right_ind) // 2
            self.left = PersistentSegmentTree(left_ind, mid, function, bound)
            self.right = PersistentSegmentTree(mid + 1, right_ind, function, bound)

    def update(self, index, val):

        if self.left_ind == self.right_ind:
            self.value = val
            return
        
        mid = (self.left_ind + self.right_ind) // 2
        if index <= mid:
            self.left.update(index, val)
        else:
            self.right.update(index, val)
        
        self.value = self.function(self.left.value, self.right.value)

    
    def persistent_update(self, index, val):
        if self.left_ind == self.right_ind:
            new_node = PersistentSegmentTree(self.left_ind, self.right_ind, self.function, self.bound)
            new_node.value = val
            return new_node
        
        mid = (self.left_ind + self.right_ind) // 2
        new_node = PersistentSegmentTree(self.left_ind, self.right_ind, self.function, self.bound)

        if index <= mid:
            new_node.left = self.left.persistent_update(index, val)
            new_node.right = self.right
        else:
            new_node.left = self.left
            new_node.right = self.right.persistent_update(index, val)
        
        new_node.value = self.function(new_node.left.value, new_node.right.value)
        return new_node
    

    def query(self, left, right):
        if right < self.left_ind or left > self.right_ind:
            return self.bound
        
        if left <= self.left_ind and right >= self.right_ind:
            return self.value
        
        return self.function(self.left.query(left, right), self.right.query(left, right))


    def get_copy(self):
        new_node = PersistentSegmentTree(0, 0)
        new_node.left_ind = self.left_ind
        new_node.right_ind = self.right_ind
        new_node.function = self.function
        new_node.bound = self.bound
        new_node.value = self.value
        new_node.left = self.left
        new_node.right = self.right
        return new_node




n = int(input())
a = ints()

prev_st = PersistentSegmentTree(0, n-1)
store = {0: prev_st}

arr = [(a[i], i) for i in range(n)]
arr.sort()



for v, i in arr:
    curr_st = prev_st.get_copy()
    curr_st = curr_st.persistent_update(i, v)

    store[v] = curr_st
    prev_st = curr_st


b = sorted(set(a))

q = int(input())

ans = []
prev = 0
for t in range(q):
    l, r, k = ints()
    l ^= prev
    r ^= prev
    k ^= prev

    ind = bisect.bisect_right(b, k)
    k = b[ind-1]

    curr_st = store[k]
    prev = curr_st.query(l-1, r-1)

    ans.append(prev)

for i in ans:
    print(i)