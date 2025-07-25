'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

https://leetcode.com/problems/permutation-in-string/description/
'''


# The solution is exactly same as find_all_anagrams
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_cache = {}
        s2_cache = {}

        for i in range(len(s1)):
            s1_cache[s1[i]] = 1 + s1_cache.get(s1[i], 0)
            s2_cache[s2[i]] = 1 + s2_cache.get(s2[i], 0)

        if s1_cache == s2_cache:
            return True
        
        left_pointer = 0
        for right_pointer in range(len(s1), len(s2)):
            s2_cache[s2[right_pointer]] = 1 + s2_cache.get(s2[right_pointer], 0)
            s2_cache[s2[left_pointer]] -= 1

            if s2_cache[s2[left_pointer]] == 0:
                s2_cache.pop(s2[left_pointer])

            left_pointer += 1

            if s1_cache == s2_cache:
                return True


        return False
                
