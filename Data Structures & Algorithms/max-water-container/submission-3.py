class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #area = height * base = min(height[i], height[j])*(j-i)

        i = 0
        j = len(heights)-1
        curr = 0
        while i < j:
            area = min(heights[i], heights[j])*(j-i)
            curr = max(curr, area)
            
            if heights[i]<heights[j]:
                i += 1
            else:
                j -= 1

        return curr