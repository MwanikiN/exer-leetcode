# Given an integer array nums of length n and an integer target, 
# find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')
    for i, n in enumerate(nums):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = n + nums[l] + nums[r]
            if abs(s - target) < abs(closest - target):
                closest = s
            if s > target:
                r -= 1
            else:
                l += 1
    return closest

print(threeSumClosest([-1,2,1,-4], 1))
print(threeSumClosest([0,0,0], 1))
print(threeSumClosest([1,1,1,0], -100))
print(threeSumClosest([1,1,1,0], 100))
