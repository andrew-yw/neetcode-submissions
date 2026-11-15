class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        L_peak = [0] * n
        R_peak = [0] * n
        area = 0

        for i in range(n):
            if i == 0:
                L_peak[i] = 0
            else:
                L_peak[i] = max(L_peak[i-1], height[i-1])
        
        for i in range(-1, -n-1, -1):
            if i == -1:
                R_peak[i] = 0
            else:
                R_peak[i] = max(R_peak[i+1], height[i+1])
        
        for i in range(n):
            area += max(min(L_peak[i], R_peak[i])-height[i], 0)

        return area
