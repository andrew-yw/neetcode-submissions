class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        prefix_prod = {}
        suffix_prod = {}
        for i in range(len(nums)):
            prefix_prod[i] = total
            total = total*nums[i]
            
        
        total_b = 1
        for i in range(len(nums)-1,-1, -1):
            suffix_prod[i] = total_b
            total_b = total_b * nums[i]
            

        output = []
        for i in range(len(nums)):
            output.append(prefix_prod[i]*suffix_prod[i])
        
        return output