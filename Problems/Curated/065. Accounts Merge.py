'''
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 

Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j] <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.

'''

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        
        email_to_account = defaultdict(list)
        
        visited = [False] * len(accounts)
        
        for i, account in enumerate(accounts):
            
            for email in account[1:]:
                email_to_account[email].append(i)
                
                
        def dfs(i, emails):
            if visited[i]:
                return
            
            visited[i] = True
            
            
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                
                for nei in email_to_account[email]:
                    if not visited[nei]:
                        dfs(nei, emails)
            
            return emails
        
        res = [ ]
        for i, account in enumerate(accounts):
            if not visited[i]:
                acc = account[0]
                res.append([acc] + sorted(list(dfs(i, set()))))
        return res
    
    '''
    Time : O(NKlogNK), where N is the 
    number of accounts and K is the maximum length of an account
    In the worst case, all the emails
    will end up belonging to a single person.
    The total number of emails will be N*K, 
    and we need to sort these emails.
    DFS traversal will take NK operations as
    no email will be traversed more than once.
    
    Space : O(NK) Building the adjacency 
    list will take O(NK) space. In the end,
    visited will contain all of the emails 
    hence it will use O(NK) space.
    Also, the call stack for DFS will use O(NK) space
    in the worst case.

The space complexity of the sorting algorithm
depends on the implementation of each programming language.
For instance, in Java, Collections.sort() dumps the specified list into an array this will take O(NK) space then Arrays.sort()
for primitives is implemented as a variant of quicksort
algorithm whose space complexity is O(logNK). In C++ sort() function provided by STL is a hybrid of Quick Sort, Heap Sort, and Insertion Sort with the worst-case space complexity of O(logNK).
    
    
    
    '''