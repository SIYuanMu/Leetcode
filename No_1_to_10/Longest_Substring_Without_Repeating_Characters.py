class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        max_len = 0
        count = 0
        current_str = ''

        for i in range(length):
            if s[i] not in current_str:
                current_str += s[i]
                count, i = count+1, i+1
            else:
                current_str = current_str[1+current_str.index(s[i]) :] + s[i]
                count = len(current_str)
            max_len = max(max_len, count)
        return max_len
