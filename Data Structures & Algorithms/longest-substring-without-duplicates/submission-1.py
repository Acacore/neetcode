class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_s = set()
        n = len(s)
        left = 0
        j = 0
        max_length = 0

        for right in range(n):
            if s[right] in set_s:
                while s[right] in set_s:
                    set_s.remove(s[left])
                    left+=1
           
            set_s.add(s[right])
            max_length = max(max_length, len(set_s))

        return max_length

        