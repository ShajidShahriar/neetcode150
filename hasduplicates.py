"""
Problem: Check if a list contains duplicate elements.

Approach:
1. **Vanilla Method (Brute Force)**: Uses nested loops, leading to O(n^2) time complexity.
2. **Set Method**: Utilizes a set to remove duplicates and compare lengths, achieving O(n) time complexity.
3. **Hash Map Method**: Uses a dictionary to count occurrences, also achieving O(n) time complexity.

Key Concepts Learned:
- Set: An unordered collection of unique elements.
- Hash Map/Dictionary: A key-value data structure for fast lookups.
- Counter: A specialized dictionary from the collections module for counting hashable items.

Uncomment any of the solutions below to test.
"""

# """
# First Method: Brute Force Approach (O(n^2) Time Complexity)
# Iterates through each element and compares it with the rest of the list.
# """
# def hasDuplicate(nums):
#     for number in nums:
#         nums.remove(number)  # Modifies the list in place, risky for large inputs.
#         for item in nums:
#             if number == item:
#                 return True  # Duplicate found
#     return False  # No duplicates found


# """
# Second Method: Set Approach (O(n) Time Complexity)
# Converts the list to a set to remove duplicates, then compares lengths.
# """
# def hasDuplicate(nums):
#     unique_elements = set(nums)  # Set automatically removes duplicates
#     return len(nums) != len(unique_elements)  # If lengths differ, duplicates exist

# print(hasDuplicate([1, 2, 3, 4, 2, 3]))  # Output: True


# """
# Third Method: Hash Map Approach (O(n) Time Complexity)
# Uses a dictionary to count occurrences of each element.
# Returns True immediately when a duplicate is found.
# """
# def hasDuplicates(nums):
#     count_dict = {}  # Initialize an empty dictionary to count occurrences
#     for num in nums:
#         if num in count_dict:
#             return True  # Duplicate found
#         else:
#             count_dict[num] = 1  # Add number to the dictionary

#     return False  # No duplicates found

# print(hasDuplicates([1, 2, 2, 3, 4]))  # Output: True
