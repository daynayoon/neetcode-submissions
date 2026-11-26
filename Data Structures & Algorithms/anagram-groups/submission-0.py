class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[]]
        res = defaultdict(list)
        for s in strs:
            res["".join(sorted(s))].append(s)
        
        return list(res.values())