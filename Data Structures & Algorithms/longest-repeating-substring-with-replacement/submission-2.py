class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxstring = 0
        maxf = 0
        seen = {}
        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right], 0) + 1
            maxf = max(maxf,seen[s[right]])

            while (right - left + 1) - maxf > k:
                seen[s[left]] -= 1
                left += 1
            maxstring = max(maxstring,right-left+1)
        return maxstring
