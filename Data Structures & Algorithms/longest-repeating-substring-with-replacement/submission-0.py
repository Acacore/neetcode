class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left, right = 0, n-1
        counts = {}
        max_freq = 0
        max_len = 0

        for right in range(n):
            counts[s[right]] = counts.get(s[right], 0 ) + 1
            max_freq = max(max_freq, counts[s[right]])

            if (right -left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            max_len = max(max_freq, right -left + 1)

        
        return max_len
