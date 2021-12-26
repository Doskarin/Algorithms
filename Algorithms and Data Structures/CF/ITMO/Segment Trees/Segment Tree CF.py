'''
A - Segment Tree for the Sum

In this task, you need to write a regular segment tree for the sum.

Input
The first line contains two integers n and m (1≤n,m≤100000), the size of the array and the number of operations.
The next line contains n numbers ai, the initial state of the array (0≤ai≤10^9). The following lines contain 
the description of the operations. The description of each operation is as follows:

1 i v: set the element with index i to v (0≤i<n, 0≤v≤10^9).
2 l r: calculate the sum of elements with indices from l to r−1 (0≤l<r≤n).
Output
For each operation of the second type print the corresponding sum.

'''

class SegmentTree:
 
    def __init__(self, n):
        self.n = n
        self.size = 1
 
        while self.size < n:
            self.size *= 2
 
        self.tree = [[float('inf'), 0]] *(2*self.size - 1)
 
    def _build(self, i, v):
        self.build(i, v, 0, 0, self.size)
    
    
    def build(self, i, v, x, start, end):
        if end - start == 1:
            if start < self.n:
                self.tree[x] = (self.tree[])
            
            self.tree[x][0] = v
            self.tree[x][1] = 1
            
            return
        
        mid = start + (end - start) // 2
 
        if i < mid:
            self.build(i, v, 2*x + 1, start, mid)
        else:
            self.build(i, v, 2*x + 2, mid, end)
 
        self.tree[x] = self.combine(self.tree[2*x + 1], self.tree[2*x + 2])

    def combine(self, s1, s2):
        if s1[0] < s2[0]:
            return s1
        elif s1[0] > s2[0]:
            return s2
        else:
            return s1[0], s1[1] + s2[1]
 
    def _query(self, left, right):
        return self.query(left, right, 0, 0, self.size)
    
    
    def query(self, left, right, x, start, end):
        if start >= right or end <= left:
            p = [None, None]
            p[0] = float('inf')
            p[1] = -1
            return p
 
        if start >= left and end <= right:
            return self.tree[x]
 
        mid = start + (end - start) // 2
 
        s1 = self.query(left, right, 2*x + 1, start, mid)
        s2 = self.query(left, right, 2*x + 2, mid, end)
        s = [0, 0]
        if s1[0] < s2[0]:
            s = s1
        elif s1[0] > s2[0]:
            s = s2
        else:
            s[0] = s1[0]
            s[1] = s1[1] + s2[1]
        
        return s


 
 
 
n, m = map(int, input().split())
arr = list(map(int, input().split()))
 
st = SegmentTree(n)
for i in range(len(arr)):
    st._build(i, arr[i])
print(st.tree)
for _ in range(m):
    op, x, y = map(int, input().split())
    if op == 1:
        st._update(x, y)
    else:
        ans = st._query(x, y)
        print(ans[0],ans[1])


        '''
        5 5 n,m
        5 4 2 3 5 arr
        2 0 3
        1 1 1
        2 0 3
        1 3 1
        2 0 5

        Expected :
        11
        8
        14
        '''