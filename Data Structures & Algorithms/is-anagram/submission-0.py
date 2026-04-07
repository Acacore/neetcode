class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        if len(s) == len(t):
            for i in s:
                dict1[i]=s.count(i)
            for j in t:
                dict2[j]=t.count(j)

            if dict1 == dict2:
                return True
            else:
                return False
        else:
            return False
        