
'''
You are given an integer k and a string s that consists only of characters 'a' (a lowercase Latin letter) and '*' (an asterisk).

Each asterisk should be replaced with several (from 0 to k inclusive) lowercase Latin letters 'b'. Different asterisk can be replaced with different counts of letter 'b'.

The result of the replacement is called a BA-string.

Two strings a and b are different if they either have different lengths or there exists such a position i that ai≠bi.

A string a is lexicographically smaller than a string b if and only if one of the following holds:

a is a prefix of b, but a≠b;
in the first position where a and b differ, the string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
Now consider all different BA-strings and find the x-th lexicographically smallest of them.

Input
The first line contains a single integer t (1≤t≤2000) — the number of testcases.

The first line of each testcase contains three integers n, k and x (1≤n≤2000; 0≤k≤2000; 1≤x≤1018). n is the length of string s.

The second line of each testcase is a string s. It consists of n characters, each of them is either 'a' (a lowercase Latin letter) or '*' (an asterisk).

The sum of n over all testcases doesn't exceed 2000. For each testcase x doesn't exceed the total number of different BA-strings. String s contains at least one character 'a'.

Output
For each testcase, print a single string, consisting only of characters 'b' and 'a' (lowercase Latin letters) — the x-th lexicographically smallest BA-string.

Example
inputCopy
3
2 4 3
a*
4 1 3
a**a
6 3 20
**a***
outputCopy
abb
abba
babbbbbbbbb
Note
In the first testcase of the example, BA-strings ordered lexicographically are:

a
ab
abb
abbb
abbbb
In the second testcase of the example, BA-strings ordered lexicographically are:

aa
aba
abba
Note that string "aba" is only counted once, even though there are two ways to replace asterisks with characters 'b' to get it.

'''

# TO-DO