# remove the values of the specified value in place
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# remove values in place
def remove_val(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)

print(remove_val([0,1,2,2,3,0,4,2], 2))

# alternative approach
def remove_val(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)

print(remove_val([0,1,2,2,3,0,4,2], 2))

# alternative approach
def remove_val(nums, val):
    for i in range(nums.count(val)):
        nums.remove(val)
    return len(nums)

print(remove_val([0,1,2,2,3,0,4,2], 2))
