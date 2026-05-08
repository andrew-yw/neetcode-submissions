class Solution:
    from collections import Counter, defaultdict
    def longestConsecutive(self, nums: List[int]) -> int:
        set_numbers = set(nums)

        max_length = 0

        for n in set_numbers:
            if (n-1) not in set_numbers:
                current_num = n
                current_streak = 1
                while (current_num + 1) in set_numbers:
                    current_num += 1
                    current_streak += 1
                max_length = max(max_length, current_streak)
            
        return max_length
        
    


            
            

