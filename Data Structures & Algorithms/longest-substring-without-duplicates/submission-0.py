class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        left = 0
        right = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left = left + 1

            seen.add(s[right])
            length = right - left + 1
            maxlength = max(maxlength,length)
        return maxlength