class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sor_nums = sorted(nums)
        print(sor_nums)
        l_list = []
        l = 1 if len(nums)>0 else 0
        for i in range(len(nums)):
            if sor_nums[i] == sor_nums[i-1]+1:
                print(sor_nums[i-1],sor_nums[i])
                l=l+1
                print(l)
            else:
                l_list.append(l)

        print(l_list)
        return l
        
        