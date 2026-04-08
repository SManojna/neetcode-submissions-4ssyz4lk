class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # division method 
        # calculate product of all the on -zero ints 
        # count the no of zeroes 
        # if the no of zeros >1, then all the nos =0, else only for the index where no is zero it is goign to be product 
        product = 1
        zeros = []
        res=[0 for i in range(0,len(nums))]
        for i in range(0, len(nums)):
            if nums[i] !=0:
                product *=nums[i]
            else:
                zeros.append(i)
        for i in range(0, len(nums)):
            if len(zeros)==0:
                res[i]= product//nums[i]
            elif len(zeros)==1:
                if nums[i]==0:
                    res[i]=product
                else:
                    res[i]=0
        return res


        