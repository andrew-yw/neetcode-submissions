class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)-2):

            target = -nums[i]
            j = i+1
            k = len(nums)-1

            while j < k:
                total = nums[j]+nums[k]
                if total == target:
                    result.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1

                elif total < target:
                    j += 1
                else:
                    k -= 1

        return [list(i) for i in result]



