class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #l and r 
        # vol = min(heights[l],heights[r])*(r-l)
        # move forward with l or r whichever is lowest 

        l = 0
        r = len(heights)-1
        max_vol = 0
        while l<r:
            vol = min(heights[l],heights[r])*(r-l)
            # print(l,r, vol)
            max_vol = max(max_vol, vol)
            if (heights[l]<=heights[r]):
                l+=1
            else:
                r-=1
        return max_vol

        