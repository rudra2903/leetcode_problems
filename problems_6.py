# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

def singleelement(nums):
    for num in nums:
        freq = 0
        for x in nums:
            if x == num:
                freq +=1
            else:
                freq = 1
        if freq == 1:
            loner = num
            print(loner)


li = [2,2,3,2]
singleelement(li)