class BIT:
    def __init__(self, nums):
        self.n = len(nums) + 1
        self.tree = [0 for i in range(self.n)]
        self.nums = [0] + nums
        
        for i in range(1, self.n):
            self.tree[i] = self.nums[i]
            
        for i in range(1, self.n):
            parent = i + (i & -i)
            if parent < self.n:
                self.tree[parent] += self.tree[i]
    
    def update(self, i, val):
        
        upd = val - self.nums[i]
        self.nums[i] = val
        while i < self.n:
            self.tree[i] += upd
            i += i & -i
    
    def query(self, i):
        total = 0
        while i != 0:
            total += self.tree[i]
            i -= i & -i
        return total
    
n, q = map(int, input().split())
nums = list(map(int, input().split()))
tree = BIT(nums)
for _ in range(q):
    q, a, b = map(int, input().split())
    if q == 1:
        tree.update(a, b)
    else:
        print(tree.query(b) - tree.query(a - 1))