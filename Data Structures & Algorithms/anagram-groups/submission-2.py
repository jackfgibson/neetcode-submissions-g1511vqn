class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # visit each string
        # get Counter(string) and see if it exists in seen
        # if not, add it as a key, with the value being the index (curr # of groups)
        # if it does exist, add it to it's key's value's index in the array of answers
        groups = 0
        seen = {}
        ans = []
        for s in strs:
            hashable = "".join(sorted(s))
            if hashable not in seen:
                seen[hashable] = groups
                groups+=1
                ans.append([])
            ans[seen[hashable]].append(s)
        return ans