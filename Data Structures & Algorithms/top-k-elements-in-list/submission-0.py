class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for i in range(k):
            most_freq = max(freq, key=freq.get)
            ans.append(most_freq)
            del freq[most_freq]
        return ans