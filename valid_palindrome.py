"""Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters"""
import re

def validpalindrome(s):
    s_split=''.join(s.split()).lower()
    text=re.sub(r"[^\w\s]","",s_split)
    print(text)
    n=len(text)
    if n==0:
        return True
    left,right=0,n-1

    while left<right:
        if text[left]!=text[right]:
            return False

        left+=1
        right-=1

    return True

s = "race a car"
print(validpalindrome(s))

