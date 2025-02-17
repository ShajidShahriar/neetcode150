"""
Problem: Check if two strings are anagrams.

Approach:
1. **Sorted Method**: Sort both strings and compare them. This has O(n log n) time complexity due to the sorting step.
2. **Counter Method**: Use a dictionary to count the occurrences of each character in both strings, then compare the dictionaries. This has O(n) time complexity.

Key Concepts Learned:
- Anagram: A word or phrase formed by rearranging the letters of another (e.g., "listen" and "silent").
- Sorting: Rearranges elements in a specific order (alphabetical in this case).
- Dictionary (Hash Map): Stores data in key-value pairs, useful for counting occurrences efficiently.

Uncomment any of the solutions below to test.
"""

# """
# First Method: Sorted Approach (O(n log n) Time Complexity)
# Converts both strings to lowercase (for case-insensitive comparison),
# sorts them, and checks if they are equal.
# """
# def isAnagram(s: str, t: str):
#     s = s.lower()  # Convert both strings to lowercase to ignore case sensitivity
#     t = t.lower()
#
#     if len(s) != len(t):
#         return False  # If lengths differ, they can't be anagrams
#
#     elif sorted(s) == sorted(t):
#         return True  # If sorted strings are the same, they are anagrams
#     else:
#         return False  # Otherwise, they are not anagrams
#
# print(isAnagram("silent", "listen"))  # Output: True


# """
# Second Method: Counter Approach (O(n) Time Complexity)
# Counts occurrences of each character in both strings using a dictionary.
# If both dictionaries are the same, the strings are anagrams.
# """
# def counter(text: str):
#     letter_count = {}  # Initialize an empty dictionary to store character counts
#     for char in text:
#         if char in letter_count:
#             letter_count[char] += 1  # Increment the count if character already exists
#         else:
#             letter_count[char] = 1  # Initialize the count if character is new
#     return letter_count  # Return the dictionary of character counts
#
#
# def isAnagram(s: str, t: str):
#     return counter(s) == counter(t)  # Compare character counts of both strings
#
# print(isAnagram("silent", "listen"))  # Output: True
# print(isAnagram("silent", "lister"))  # Output: False
