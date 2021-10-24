class SegmentTree:
    def __init__(self, nums):
        #Initialize the tree with size = 2 * n, where is the size of original array
        self.n = len(nums)
        self.tree = [0] * self.n + nums
        
        #Fill in the nodes
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        #Fill in the parents --> This can include functions like min, max, sum, gcd etc.
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])
    
    def query(self, left, right):
        left += self.n
        right += self.n
        mMin = float('inf')
        while left < right:
            
            if (left & 1):
                mMin = min(mMin, self.tree[left])
                left += 1
            if (right & 1):
                right -= 1
                mMin = min(mMin, self.tree[right])
                 
            left //= 2
            right //= 2
        return mMin
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])
            
n, q = map(int, input().split())
nums = list(map(int, input().split()))
tree = SegmentTree(nums)
for _ in range(q):
    q, a, b = map(int, input().split())
    if q == 1:
        tree.update(a - 1, b)
    else:
        print(tree.query(a - 1,b))