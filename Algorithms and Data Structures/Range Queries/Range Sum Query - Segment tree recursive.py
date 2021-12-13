class Node:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.total = 0

class SegmentTree:

    def __init__(self, nums):

        self.nums = nums
        self.root = self.build(0, len(self.nums) - 1)

    def build(self, left, right):

        if left == right:
            node = Node(left, right)
            node.total = self.nums[left]
            return node

        else:
            mid = left + (right - left) // 2

            node = Node(left, right)

            node.left = self.build(left, mid)
            node.right = self.build(mid + 1, right)

            node.total = node.left.total + node.right.total

            return node

    def query(self, node, left, right):

        if node.start == left and node.end == right:
            return node.total

        mid = node.start + (node.end - node.start) // 2

        if mid + 1 <= left:
            return self.query(node.right, left, right)

        elif right <= mid:
            return self.query(node.left, left, right)

        else:
            return self.query(node.left, left, mid) + self.query(node.right, mid + 1, right)

    def update(self, node, index, value):
        if node.start == node.end:
            node.total = value
            return node.total

        else:
            mid = node.start + (node.end - node.start) // 2

            if index <= mid:
                self.update(node.left, index, value)
            else:
                self.update(node.right, index, value)
            
            node.total = node.left.total + node.right.total

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    #ind   0 1 2 3 4 5

    ST = SegmentTree(arr)

    print(ST.query(ST.root, 0, 2), "Expected : 6 ")
    print(ST.query(ST.root, 2, 5), "Expected : 18")

    ST.update(ST.root, 0, 100)
    # arr = [100,2,3,4,5,6]

    print(ST.query(ST.root, 0, 2), "Expected : 105 ")

    ST.update(ST.root, 5, 1000)
    # arr = [100,2,3,4,5,1000]

    print(ST.query(ST.root, 2, 5), "Expected : 1012")

    print(ST.root.total, "Expected : 1114")






        

        