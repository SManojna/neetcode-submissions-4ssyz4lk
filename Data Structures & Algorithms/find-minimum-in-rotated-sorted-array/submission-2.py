class Solution:
    def findMin(self, nums: List[int]) -> int:
        # need o(logn) time appraoch 
        # look for pattterns 
        # if nums[l]< nums[mid]-> search in right part
        # if nums[mid]<nums[r]-> search in left part 
        l, r = 0, len(nums)-1
        
        while l<r:
            mid = l+(r-l)//2
            if nums[mid]<nums[r]:
                # search for pattern in right half 
                r=mid
            else:
                l=mid+1
        return nums[l]
            

            
        