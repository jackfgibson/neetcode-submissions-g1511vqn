class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
        # **implementing counter by hand**
        # c, cc = {}, {}
        # if len(s)==len(t):
        #     for x in range(len(s)):
        #         if s[x] in c:
        #             c[s[x]]+=1
        #         else:
        #             c[s[x]]=1
        #         if t[x] in cc:
        #             cc[t[x]]+=1
        #         else:
        #             cc[t[x]]=1
        #     return c==cc
        # return False