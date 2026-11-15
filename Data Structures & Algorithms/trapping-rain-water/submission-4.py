class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        L, R = 0, 0
        area = 0
        while left < right:
            L = max(L, height[left])
            R = max(R, height[right])

            if L <= R:
                area += L - height[left]
                left += 1
            else:
                area += R - height[right]
                right -= 1
            
        return area