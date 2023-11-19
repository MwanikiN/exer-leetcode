# Given an array nums of n integers, return an array of all the unique 
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.


# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

def four_sum(nums, target):
    nums.sort()
    res = set()
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            left = j + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[j] + nums[left] + nums[right] == target:
                    res.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
    return list(res)

print(four_sum([1,0,-1,0,-2,2], 0))
print(four_sum([2,2,2,2,2], 8))

# alternative approach
def four_sum(nums, target):
    nums.sort()
    n = len(nums)
    four_sum = []

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1
            while left < right:
                if nums[i] + nums[j] + nums[left] + nums[right] == target:
                    four_sum.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
    
    return four_sum

print(four_sum([1,0,-1,0,-2,2], 0))
print(four_sum([2,2,2,2,2], 8))