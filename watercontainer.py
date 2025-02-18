"""You are given an integer array heights where heights[i] represents the height of the ithith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store."""




def maxArea(heights):
    waterVols=[]



    left,right=0, len(heights) - 1

    while left<right:
        min_height=min(heights[left], heights[right])
        waterVols.append((right - left) * min_height)
        if min_height == heights[left]:
            left+=1
        elif min_height == heights[right]:
            right-=1
    return max(waterVols)
height = [1,7,2,5,4,7,3,6]

print(maxArea(height))
