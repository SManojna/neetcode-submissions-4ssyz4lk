class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first sort the numbers 
        # we need sum of 3 muns = 0 , so in one loop consider from left and loop through elements till we see 0 or first positive number 
        # if no 0 or non -negative them 0 
        #consider 2 pointer technique and use l and r such that l<r and thier sum is poitive of our first number , lop thoughh and add the numebrs to a list 

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
