'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

https://leetcode.com/problems/can-place-flowers/description/
'''

# This works but very slow.
def can_place_flowers_1(arr, n):
    if n == 0:
        return True
    
    for i in range(len(arr)):
        if n == 0:
            return True
        
        if i == 0 and arr[i] == 0 and i + 1 <= len(arr) - 1 and arr[i + 1] == 0:
            arr[i] = 1
            n -= 1
        elif i == len(arr) - 1 and arr[i] == 0 and arr[i - 1] == 0:
            arr[i] = 1
            n -= 1
        elif arr[i] == 0 and arr[i - 1] == 0 and  i + 1 <= len(arr) - 1 and arr[i + 1] == 0:
            arr[i] = 1
            n -= 1
    print(arr)
    return n <= 0

arr = [0]
n = 1
# print(can_place_flowers_1(arr, n))


def can_place_flowers_2(arr, n):
    f = [0] + arr + [0]

    for i in range(1, len(f) - 1):
        if f[i] == 0 and f[i-1] == 0 and f[i+1] == 0:
            f[i] = 1
            n -= 1
    return n <= 0

    
print(can_place_flowers_2(arr, n))
