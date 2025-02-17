"""made three solutions(in no particular oder)
previous concepts are used here
 uncomment to run """

"""2nd solution"""
# strs = ["act", "pots", "tops", "cat", "stop", "hat"]
# anagram_dict = {}
# for text in strs:
#     char_count = [0] * 26
#     for letter in text:
#         alphabet = 'abcdefghijklmnopqrstuvwxyz'
#         index = alphabet.index(letter)
#         char_count[index] += 1
#
#     key = tuple(char_count)
#
#     if key not in anagram_dict:
#         anagram_dict[key] = []
#
#     anagram_dict[key].append(text)
#
# print(list(anagram_dict.values()))

"""2nd solution but better"""
# from collections import defaultdict
#
# def groupAnagrams(strs):
#     anagram_dict = defaultdict(list)  # Automatically initializes new keys with an empty list
#
#     for text in strs:
#         char_count = [0] * 26
#         for letter in text:
#             index = ord(letter) - ord('a')  # Use ord to calculate the index
#             char_count[index] += 1
#
#         key = tuple(char_count)
#         anagram_dict[key].append(text)  # No need to check if key exists
#
#     return list(anagram_dict.values())

# # Example usage
# strs = ["act", "pots", "tops", "cat", "stop", "hat"]
# print(groupAnagrams(strs))


"""3rd solution"""

# anagram={}
#
# for word in strs:
#     sorted_word=''.join(sorted(word))
#
#
#     if sorted_word in anagram:
#         anagram[sorted_word].append(word)
#
#     else:
#         anagram[sorted_word]=[word]
#
#
#
#
# print(anagram)
#
# anagram_groups = list(anagram.values())
#
# print(anagram_groups)
