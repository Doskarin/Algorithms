# Range Xor Queries
#added some more comments for git status
class xor_prefix:
    def __init__(self, nums):
        self.n = len(nums)
        self.prefix = [0] * self.n
        self.prefix[0] = nums[0]
        for i in range(1, self.n):
            self.prefix[i] = self.prefix[i - 1] ^ nums[i]
        self.prefix = [0] + self.prefix
    
    def query(self, left, right):
        return self.prefix[right] ^ self.prefix[left - 1]

n, q = map(int, input().split())
arr = list(map(int, input().split()))
l = xor_prefix(arr)
for _ in range(q):
    left, right = map(int, input().split())
    print(l.query(left, right))