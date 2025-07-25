'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104

https://leetcode.com/problems/maximum-average-subarray-i/description/
'''

# This is very slow. 
def maximum_average_subarray_1_1(arr, k):
    left, right = 0,0
    prefix_sum = 0
    avg_value = float('-inf')
    while right < len(arr):
        prefix_sum += arr[right]
        if (right - left) + 1 == k:
            avg_value = max(avg_value, prefix_sum / k)
            prefix_sum -= arr[left]
            left += 1
        
        right += 1
    
    return avg_value
    
nums = [1,12,-5,-6,50,3]
k = 4
print(maximum_average_subarray_1_1(nums, k))

# This is faster.
def maximum_average_subarray_1_2(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum / k

print(maximum_average_subarray_1_2(nums, k))
