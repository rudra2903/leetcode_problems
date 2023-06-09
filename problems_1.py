# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.



def twosum (nums , target):
    for i in range(len(nums)):
        for j in range(i+1 , len(nums)):
            if target - nums[i]== nums[j]:
                return [i,j]
    return None

test = [2,4,5,6,7,8,9]
target = 12
print(twosum(test , target))