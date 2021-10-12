# 2. Static Range Minimum Queries
class SparseTable:
    def __init__(self, nums):
        self.size = len(nums)
        self.log_table = [0] * (self.size + 1)
        for i in range(2, len(self.log_table)):
            self.log_table[i] = self.log_table[i // 2] + 1
        #print(self.log_table)
        self.sparse_table = [[0] * self.size for _ in range(self.log_table[-1] + 1)]
        self.sparse_table[0] = nums
        
        for row in range(1, len(self.sparse_table)):
            i = 0
            while i + (1 << row) <= self.size:
                self.sparse_table[row][i] = min(self.sparse_table[row - 1][i],\
                                                self.sparse_table[row - 1][i + (1 << (row - 1))])
                i += 1
        #print(self.sparse_table)
    def query(self, left, right):
        log = self.log_table[right - left]
        return min(self.sparse_table[log][left], self.sparse_table[log][right - (1 << log)])
n, q = map(int, input().split())
nums = list(map(int, input().split()))
ST = SparseTable(nums)
for _ in range(q):
    a, b = map(int, input().split())
    print(ST.query(a - 1, b + 1 - 1))