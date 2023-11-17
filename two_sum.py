# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
print(twoSum([2,7,11,15], 9))

# Alternative approach
def two_sum(nums, target):
    two_sum = {}
    for i in nums:
        if target - i in two_sum:
            return [two_sum[target - i], nums.index(i)]
        else:
            two_sum[i] = nums.index(i)

print(two_sum([2,7,11,15], 9))

# third approach
def two_sum(nums, target):
    two_sum = {}
    for i,n in enumerate(nums):
        if target - n in two_sum:
            return [two_sum[target - n], i] 
        else:
            two_sum[n] = i

print(two_sum([2,7,11,15], 9))      