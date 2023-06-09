# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
def foursum(num , target):
    
    num.sort()
    result = []

    for i in range(len(num)):
        for j in range(i+1,len(num)):
            for k in range(j+1, len(num)):
                for l in range(k+1,len(num)):
                    if num[i]+num[j]+num[k]+num[l] == target:
                        triplet = list([num[i],num[j],num[k],num[l]])
                        result.append(triplet)

    # result = sorted(result)
    print(result)

num = [1,0,-1,0,-2,2]
target = 2
foursum(num,target)