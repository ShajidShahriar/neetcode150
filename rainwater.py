"""You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars."""

height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
def rainwater(height):
    if not height:return 0

    left,right=0,len(height)-1
    left_max=height[left]
    right_max=height[right]
    result=0

    while left < right :
        if left_max < right_max:
            left+=1
            trapped = max(0, left_max - height[left])
            result+=trapped
            left_max =max(left_max,height[left])
        else:
            right-=1
            trapped = max(0, right_max - height[right])
            result+=trapped
            right_max=max(right_max,height[right])




    return result




