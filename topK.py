"""two solution ive made , learned bucket sort for learning a newer approach
 first solution is vanilla and slow , second one is more comprehensive but with better time constrain """


"""solution #1"""
from collections import Counter
# def topkcount(nums,k):
#
#     output=[]
#     count=Counter(nums)
#     print(count)
#     for key,value in count.items():
#         if value >= k:
#             output.append(key)
#
#
#     return output


"""solution #2 """
# def topkcount(nums,k):
#
#     count=Counter(nums)
#
#     buckets=[[] for item in range(len(nums)+1)]
#
#     for key,value in count.items():
#         buckets[value].append(key)
#
#
#     result=[]
#
#     for freq in range(len(buckets)-1,0,-1):
#         for num in buckets[freq]:
#             result.append(num)
#             if len(result)==k:
#                 return result
#
#
# print(topkcount([1,2,2,3,3,3],2))