'''
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
 

Constraints:

1 <= people.length <= 5 * 104
1 <= people[i] <= limit <= 3 * 104

https://leetcode.com/problems/boats-to-save-people/description/
'''

# This fails half of the test cases.
def boats_to_save_people_1(arr, limit):
    boats = 0
    curr_limit = 0
    
    arr.sort()
    print(arr)
    for index, value in enumerate(arr):
        if curr_limit + value > limit:
            boats += 1
            curr_limit = value
        else:
            curr_limit += value
            
        if index == len(arr) - 1 and curr_limit >= limit:
            boats += 1

    return boats if boats > 0 else 1
    
people = [5,1,4,2]

limit = 6
# print(boats_to_save_people_1(people, limit))



def boats_to_save_people_2(arr, limit):
    arr.sort()
    print(arr)
    
    l,r = 0, len(arr) - 1
    boats = 0
    
    while l <= r:
        remaining_space = limit - arr[r]
        r -= 1
        boats += 1
        
        if l <= r and remaining_space >= arr[l]:
            l += 1
    return boats
people = [5,1,4,2]

limit = 6
print(boats_to_save_people_2(people, limit))
