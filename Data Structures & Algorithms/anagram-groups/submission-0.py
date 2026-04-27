class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            keys = "".join(sorted(s))

            if keys not in groups:
                groups[keys]= []
            groups[keys].append(s)
        return list(groups.values())
        