"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
"""
def threeSum(nums):
    nums.sort()
    result=[]

    for i,num in enumerate(nums):

        if i > 0 and num == nums[i-1]:
            continue

        left,right= i,len(nums)-1

        while left<right:
            if num+nums[left]+nums[right] > 0:
                right-=1
            elif num+nums[left]+nums[right]<0:
                left+=1
            else:
                result.append([num,nums[left],nums[right]])
                left+=1
                while nums[left] == nums[left -1] and left < right:
                    left+=1


    return result

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))