# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

def threesum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = list([nums[i], nums[j], nums[k]])
                    result.append(triplet)

    # results = sorted(result)  
    print(result)


nums = [-1, 0, 1, 2, -1, -4]
threesum(nums)




# target = 0
# print(result)