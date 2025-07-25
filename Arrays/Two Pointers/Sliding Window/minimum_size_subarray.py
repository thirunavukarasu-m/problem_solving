'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

https://leetcode.com/problems/minimum-size-subarray-sum/description/
'''

def minimum_size_subarray(target, arr):
    prefix_sum = 0
    
    left, right = 0,0
    min_length = float('inf')
    while right < len(arr):
        prefix_sum += arr[right]
        while prefix_sum >= target:
            min_length = min(min_length, (right - left) + 1)
            prefix_sum -= arr[left]
            left += 1
        right += 1
    
    return min_length if min_length != float('inf') else 0
        

target = 7
nums = [2,3,1,2,4,3]
print(minimum_size_subarray(target, nums))