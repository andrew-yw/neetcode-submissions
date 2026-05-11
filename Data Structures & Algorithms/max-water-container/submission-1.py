class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #area = height * base = min(height[i], height[j])*(j-i)
        curr = 0
        for i in range(0, len(heights)):

            for j in range(i+1, len(heights)):
               
                area = min(heights[i], heights[j])*(j-i)
                if area > curr:
                    curr = area

        return curr