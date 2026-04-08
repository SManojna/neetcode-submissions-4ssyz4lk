class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using left product and right product 
        # intiialize res 
        res = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            res[i]=res[i-1]*nums[i-1]
        right_product = 1
        for i in range(len(nums)-2,-1,-1):
            right_product *=nums[i+1]
            res[i]=res[i]*right_product

        return res


        