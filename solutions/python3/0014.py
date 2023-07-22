class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0 or len(strs[0]) == 0:
            return ""
        longest_substr = strs[0]
        max_len = len(strs[0])

        for string_elem in strs[1:]:
            if len(string_elem) == 0:
                return ""
            if string_elem[0] != longest_substr[0]:
                return ""
            j = 1
            while j < min(max_len, len(string_elem)):
                if string_elem[j] != longest_substr[j]:
                    longest_substr = longest_substr[:j]
                    max_len = j
                j += 1
            if j < max_len:
                longest_substr = string_elem
                max_len = j
        return longest_substr
