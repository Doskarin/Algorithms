class SegmentTree:

    def __init__(self, nums):
        self.nums = nums
        self.size = 1
        self.n = len(self.nums)
        
        while self.size < self.n:
            self.size *= 2
        self.tree = [float('inf')] * (2 * self.size - 1)

        self.build(0, 0, self.n - 1)

        self.lazy = [0] * (2 * self.size - 1)

    def build(self, pos, l, r):
        if l == r:
            self.tree[pos] = self.nums[l]
            return

        m = l + (r - l) // 2
        self.build(2*pos + 1, l, m)
        self.build(2*pos + 2, m + 1, r)

        self.tree[pos] = min(self.tree[2*pos + 1], self.tree[2*pos + 2])

    # Update index in the initial array by certain delta (val) 
    def update(self, i, val):
        self.nums[i] += val
        self._update(i, val, 0, self.n - 1, 0)

    #Update helper function
    # i - index we need to update
    # val - delta by which we update
    # l, r - initial array boundaries
    # pos - index in our tree
    def _update(self, i, val, l, r, pos):

        if i < l or i > r:
            return

        if l == r:
            self.tree[pos] += val
            return

        m = l + (r - l) // 2

        self._update(i, val, l, m, 2*pos + 1)
        self._update(i, val, m + 1, r, 2*pos + 2)
        self.tree[pos] = min(self.tree[2*pos + 1], self.tree[2*pos + 2])

    def rangeMinQuery(self, ql, qr):
        return self._rangeMinQuery(0, self.n - 1, ql, qr, 0)

    def _rangeMinQuery(self, l, r, ql, qr, pos):
        # Complete overlap
        if l >= ql and r <= qr:
            return self.tree[pos]

        # No overlap
        if ql > r or qr < l:
            return float('inf')

        m = l + (r - l) // 2

        return min(
            self._rangeMinQuery(l, m, ql, qr, 2*pos + 1),
            self._rangeMinQuery(m + 1, r, ql, qr, 2*pos + 2)
            )

    def updateRangeLazy(self, startRange, endRange, val):
        self._updateRangeLazy(startRange, endRange, val, 0, self.n - 1, 0)

    def _updateRangeLazy(self, startRange, endRange, val, l, r, pos):
        if l > r:
            return
        
        if self.lazy[pos] != 0:
            self.tree[pos] += self.lazy[pos]
            if l != r:
                self.lazy[2*pos + 1] += self.lazy[pos]
                self.lazy[2*pos + 2] += self.lazy[pos]
            self.lazy[pos] = 0

        if startRange > r or endRange < l:
            return

        if startRange <= l and endRange >= r:
            self.tree[pos] += val
            if l != r:
                self.lazy[2*pos + 1] += val
                self.lazy[2*pos + 2] += val

            return

        m = l + (r - l) // 2

        self._updateRangeLazy(startRange, endRange, val, l, m, 2*pos + 1)
        self._updateRangeLazy(startRange, endRange, val, m + 1, r, 2*pos + 2)
        self.tree[pos] = min(self.tree[2*pos + 1], self.tree[2*pos + 2])

    def rangeMinQueryLazy(self, ql, qr):
        return self._rangeMinQueryLazy(0, self.n - 1, ql, qr, 0)

    def _rangeMinQueryLazy(self, l, r, ql, qr, pos):
        if l > r:
            return float('inf')

        if self.lazy[pos] != 0:
            self.tree[pos] += self.lazy[pos]
            if l != r:
                self.lazy[2*pos + 1] += self.lazy[pos]
                self.lazy[2*pos + 2] += self.lazy[pos]
            self.lazy[pos] = 0

        if ql > r or qr < l:
            return float('inf')

        if ql <= l and qr >= r:
            return self.tree[pos]

        m = l + (r - l) // 2

        return min(
            self._rangeMinQueryLazy(l, m, ql, qr, 2*pos + 1), 
            self._rangeMinQueryLazy(m + 1, r, ql, qr, 2*pos + 2)
            )


    

if __name__ == "__main__":
    arr = [-1, 3, 2, 7, 9, 0, 14, -3]
    st = SegmentTree(arr)
    print(st.tree)
    print(st.rangeMinQuery(0,7))
    st.updateRangeLazy(7,7, 103)
    print(st.tree)
    st.updateRangeLazy(5,7, 300)
    print(st.tree)
    print(st.rangeMinQueryLazy(7,7))