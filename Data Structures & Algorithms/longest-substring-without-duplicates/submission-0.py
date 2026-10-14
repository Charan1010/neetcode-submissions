class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        left = 0
        right = 0
        max_len = 0

        while right < len(s):

            if s[right] in char_set:
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left+= 1
            char_set.add(s[right])
            if len(char_set) > max_len:
                max_len = len(char_set)
            right += 1

        return max_len
        