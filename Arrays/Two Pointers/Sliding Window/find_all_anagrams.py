'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
'''


def find_all_anagrams(s, t):
    if len(s) < len(t):
        return []
    s_cache = {}
    t_cache = {}
    n = len(t) - 1
    for i in range(n + 1):
        t_cache[t[i]] = 1 + t_cache.get(t[i], 0)
        s_cache[s[i]] = 1 + s_cache.get(s[i], 0)
    
    result = [0] if s_cache == t_cache else []
    left = 0
    for i in range(n + 1, len(s)):
        s_cache[s[i]] = 1 + s_cache.get(s[i], 0)
        s_cache[s[left]] -= 1
        
        if s_cache[s[left]] == 0:
            s_cache.pop(s[left])
        
        
        if s_cache == t_cache:
            result.append(left + 1)
        left += 1
        
        
    return result
    
s = "abab"
t = "ab"
print(find_all_anagrams(s,t))