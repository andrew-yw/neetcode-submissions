class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        freq_dict = defaultdict(int)
        for n in nums:
            freq_dict[n] += 1
        
        sorted_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse = True))

        first_k_keys = list(sorted_dict)[:k]

        return first_k_keys
