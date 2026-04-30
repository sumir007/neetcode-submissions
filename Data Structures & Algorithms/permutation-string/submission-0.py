class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen1 = {}
        seen2 = {}
        left = 0

        for c in s1:
            seen1[c] = seen1.get(c,0) + 1

        for right in range(len(s2)):
            seen2[s2[right]] = seen2.get(s2[right],0) + 1
            if right - left + 1 > len(s1):
                seen2[s2[left]] -= 1
                if seen2[s2[left]] == 0:
                    del seen2[s2[left]]
                left += 1
            if seen1 == seen2:
                return True
        return False