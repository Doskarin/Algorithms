'''
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.

'''

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        from collections import defaultdict
        
        d = defaultdict(list)

        for string in strings:
            
            key = ()
            for i in range(len(string) - 1):
                
                circular_key = 26 + (ord(string[i + 1]) - ord(string[i]))
                key += (circular_key % 26,)
                
            d[key].append(string)
            
        return d.values()
    
    '''
    Time : would be O(ab) where a is the total number of strings and
    b is the length of the longest string in strings.
    Space : would be O(n), as the most space we would use is the space
    required for strings and the keys of our hashmap.
    
    '''