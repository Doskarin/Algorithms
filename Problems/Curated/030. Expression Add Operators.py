'''
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Explanation: Both "1*0+5" and "10-5" evaluate to 5.
Note that "1-05" is not a valid expression because the 5 has a leading zero.
Example 4:

Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]
Explanation: "0*0", "0+0", and "0-0" all evaluate to 0.
Note that "00" is not a valid expression because the 0 has a leading zero.
Example 5:

Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
 

Constraints:

1 <= num.length <= 10
num consists of only digits.
-2^31 <= target <= 2^31 - 1


'''

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        
        res = [ ]
        
        def dfs(path, i, cur_sum, last):
            
            if i == len(num):
                if cur_sum == target:
                    res.append(path)
                    
            for j in range(i + 1, len(num) + 1):
                temp = int(num[i:j])
                
                if j == i + 1 or (j > i + 1 and num[i] != "0"):
                    
                    if last is None:
                        dfs(num[i:j], j, temp, temp)
                    else:
                        dfs(path + "+" + num[i:j], j, cur_sum + temp, temp)
                        dfs(path + "-" + num[i:j], j, cur_sum - temp, -temp)
                        dfs(path + "*" + num[i:j], j, cur_sum - last + last*temp, last*temp)
                        
        dfs("", 0, 0, None)
        
        return res
    
    '''
    
    Time : O(N*4^N), 
    At every step along the way,
    we consider exactly 4 different choices
    or 4 different recursive paths. 
    The base case is when the value of index
    reaches N i.e. the length of the nums array.
    Hence, our complexity would be O(4^N)
    For the base case we use .join() operation
    in Python and that takes O(N) time.
    Here N represents the length of our expression. In the worst case,
    each digit would be an operand and 
    we would have N digits and N−1 operators.
    So O(N). This is for one expression.
    In the worst case, we can have O(4^N) valid expressions.
    Overall time complexity = O(N*4^N)
    
    Space : O(N),
    For both Python and Java implementations
    we have a list data structure that 
    we update on the fly and only for valid 
    expressions do we create a new string 
    and add to our answers array. So, the 
    space occupied by the intermediate list 
    would be O(N) since in the worst case
    the expression would be built out 
    of all the digits as operands.
    '''