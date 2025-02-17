import collections


def longestConsecutive(nums):
    if not nums:
        return 0

    nums_set = set(nums)
    max_length=0
    for num in nums_set:
        if (num - 1) not in nums:
            current_num=num
            current_streak=1

            while current_num+1 in nums_set:
                current_num+=1
                current_streak+=1

            max_length=max(max_length,current_streak)
    return max_length
print(longestConsecutive([7, 3, 5, 8, 9, 4, 10]))
