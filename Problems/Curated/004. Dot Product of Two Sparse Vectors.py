'''
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

 

Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
Example 2:

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
Example 3:

Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
 

Constraints:

n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 100


'''

class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = [(index, value) for index, value in enumerate(nums) if value != 0]
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        p1 = 0
        p2 = 0
        total = 0
        
        while p1 < len(self.vector) and p2 < len(vec.vector):
            
            if self.vector[p1][0] == vec.vector[p2][0]:
                
                total += self.vector[p1][1] * vec.vector[p2][1]
                p1 += 1
                p2 += 1
                
            elif self.vector[p1][0] < vec.vector[p2][0]:
                p1 += 1
            else:
                p2 += 1
        return total
    
    '''
    Time : O(n) for creating (index, value) pair of non-zero values
    if L1 and L2 number of non-zero elements for the two vectors
    O(L1 + L2) time complexity to calculate the dot product of two vectors
    
    Space : O(L) for creating (index, value) pairs for non-zero values, 
            O(1) for calculating the dot product

    '''
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)