class Node:
    def __init__(self):
        self.set = NO_OPERATION
        self.sum = NEUTRAL_ELEMENT

class SegmentTree:

    global NO_OPERATION, NEUTRAL_ELEMENT
    NO_OPERATION = float('-inf')
    NEUTRAL_ELEMENT = 0

    def op_modify(self, a, b, ln):
        if b == NO_OPERATION:
            return a
        return b * ln
    
    def op_sum(self, a, b):
        return a + b

    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        
        self.tree = [Node()] * (2 * self.size - 1)

    def propagate(self, x, lx, rx):
        if self.tree[x].set == NO_OPERATION or rx - lx == 1:
            return

        m = lx + (rx - lx) // 2
        self.tree[2*x + 1].set = self.op_modify(self.tree[2*x + 1].set, self.tree[x].set, 1)
        self.tree[2*x + 1].sum = self.op_modify(self.tree[2*x + 1].sum, self.tree[x].set, m - lx)
        self.tree[2*x + 2].set = self.op_modify(self.tree[2*x + 2].set, self.tree[x].set, 1)
        self.tree[2*x + 2].sum = self.op_modify(self.tree[2*x + 2].sum, self.tree[x].set, rx - m)

        self.tree[x].set = NO_OPERATION

    def _mult(self, l, r, v, x, lx, rx):
        self.propagate(x, lx, rx)

        if l >= rx or lx >= r:
            return
        
        if lx >= l and rx <= r:
            self.tree[x].set = self.op_modify(self.tree[x].set, v, 1)
            self.tree[x].sum = self.op_modify(self.tree[x].sum, v, rx - lx)
        
        m = lx + (rx - lx) // 2

        self._mult(l, r, v, 2*x + 1, lx, m)
        self._mult(l, r, v, 2*x + 2, m, rx)
        self.tree[x].sum = self.op_sum(self.tree[2*x + 1].sum, self.tree[2*x + 2].sum)
    
    def mult(self, l, r, v):
        self._mult(l, r, v, 0, 0, self.size)


    def _query(self, l, r, x, lx, rx):
        self.propogate(x, lx, rx)
        if l >= rx or lx >= r:
            return NEUTRAL_ELEMENT

        if lx >= l and rx <= r:
            print(self.tree[x].sum)
            return self.tree[x].sum

        m = lx + (rx - lx) // 2

        s1 = self._query(l, r, 2*x + 1, lx, m)
        s2 = self._query(l, r, 2*x + 2, m, rx)

        return self.op_sum(s1, s2)


    def query(self, l, r):
        return self._query(l, r, 0, 0, self.size)


n, m = map(int, input().split())
st = SegmentTree(n)
print(len(st.tree))
for _ in range(m):
    op, l, r, v = map(int, input().split())
    if op == 1:
        st.mult(l, r, v)
    else:
        print(st.query(l, r))

    

















