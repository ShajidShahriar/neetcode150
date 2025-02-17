"""this problem fucked me up like  crazy and its considered as an easy problem  ,what?
well i made two solutions , first one is kinda brute forcing your way in with relatively worse time complexity,
second one  uses hashmaps and runs much faster (o1 complexity)
uncomment the part to test


some basic things i need to focus more , how to use hashmaps and basic logic
"""


"""first method"""
# nums = [5,5
# output=[]
# target = 10
#
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]== target:
#             output.append(i)
#             output.append(j)
#             print(output)


"""second method"""
# def twosum(nums,target):
#     hashmap = {}
#
#     for i in range(len(nums)):
#         difference=target-nums[i]
#         if difference in hashmap:
#             return [hashmap[difference],i]
#             break
#         else:
#             hashmap[nums[i]]=i
#
# print(twosum([5,5],10))



"""needs revision """