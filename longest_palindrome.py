# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

def longest_palindrome(s):
    if len(s) < 2:
        return s
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    for i in range(len(s)):
        palindrome_odd = expand_around_center(i, i)
        palindrome_even = expand_around_center(i, i + 1)
        longest = max(longest, palindrome_odd, palindrome_even, key=len)

    return longest

print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
print(longest_palindrome("a"))
print(longest_palindrome("ac"))
print(longest_palindrome("acb"))
print(longest_palindrome("acbb"))

def longestPalindrome(s):
    if len(s) < 2:
        return s

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        palindrome_odd = expand_around_center(i, i)
        if len(palindrome_odd) > len(longest):
            longest = palindrome_odd

        palindrome_even = expand_around_center(i, i + 1)
        if len(palindrome_even) > len(longest):
            longest = palindrome_even

    return longest
    
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("a"))
print(longestPalindrome("ac"))
print(longestPalindrome("acb"))