class SegmentTree:
 
    def __init__(self, n):
        self.size = 1
        #always power of two
        while self.size < n:
            self.size *= 2
 
        self.tree = [(float('inf'), 0)] *(2*self.size - 1)
 
    def combine(self, a, b):
        if a[0] < b[0]:
            return a
        elif a[0] > b[0]:
            return b
        else:
            return a[0], a[1] + b[1]
    def _build(self, i, v):
        self.build(i, v, 0, 0, self.size)

    def build(self, i, v, x, start, end):
        if end - start == 1:
            self.tree[x] = (v, 1)
            return
        
        mid = start + (end - start) // 2
 
        if i < mid:
            self.build(i, v, 2*x + 1, start, mid)
        else:
            self.build(i, v, 2*x + 2, mid, end)
 
        self.tree[x] = self.combine(self.tree[2*x + 1], self.tree[2*x + 2])
 
    
    
    
    def _query(self, left, right):
        return self.query(left, right, 0, 0, self.size)
    
    def query(self, left, right, x, start, end):
        if start >= right or end <= left:
            return (float('inf'), 0)
 
        if start >= left and end <= right:
            return self.tree[x]
 
        mid = start + (end - start) // 2
        s2 = self.query(left, right, 2*x + 2, mid, end)
 
        s1 = self.query(left, right, 2*x + 1, start, mid)
        
 
        return self.combine(s1, s2)
 
import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
arr = list(map(int, input().split()))
 
st = SegmentTree(n)
for i in range(len(arr)):
    st._build(i, arr[i])
 
for _ in range(m):
    op, x, y = map(int, input().split())
    if op == 1:
        st._build(x, y)
    else:
        a,b = st._query(x, y)
        print(a, b)