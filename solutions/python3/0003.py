class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest = 1
        substr = s[0]
        for i in range(1, len(s)):
            if not s[i] in substr:
                substr += s[i]
            else:
                if len(substr) > longest:
                    longest = len(substr)
                substr += s[i]
                substr = substr[substr.index(s[i]) + 1:]
            if len(substr) > longest:
                longest = len(substr)
        return longest
