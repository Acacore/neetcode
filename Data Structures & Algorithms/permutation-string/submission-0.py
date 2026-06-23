class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        # If s1 is longer than s2, a permutation is impossible
        if len_s1 > len_s2:
            return False

        count_char_s1 = {}
        count_char_s2 = {}

        # 1. Count characters for s1
        for i in s1:
            count_char_s1[i] = count_char_s1.get(i, 0) + 1

        # 2. Count characters for the VERY FIRST window of s2 (index 0 to len_s1)
        for i in range(len_s1):
            char = s2[i]
            count_char_s2[char] = count_char_s2.get(char, 0) + 1

        # Check the first window immediately
        if count_char_s1 == count_char_s2:
            return True

        # 3. Slide the window across the rest of s2
        # This matches your range structure perfectly!
        for i in range(1, len_s2 - len_s1 + 1):
            # The character that just left the window on the left side
            char_out = s2[i - 1]
            # The character that just entered the window on the right side
            char_in = s2[i + len_s1 - 1]

            # Update the dictionary for the incoming character
            count_char_s2[char_in] = count_char_s2.get(char_in, 0) + 1

            # Update the dictionary for the outgoing character
            if count_char_s2[char_out] == 1:
                del count_char_s2[char_out]
            else:
                count_char_s2[char_out] -= 1

            # Check if our optimized dictionary matches s1
            if count_char_s1 == count_char_s2:
                return True

        return False