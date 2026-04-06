class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        l = len(nums)
        for idx, val in enumerate(nums):
            diff = target - nums[idx]
            if diff in nums_dict:
                diff_idx = nums_dict.get(diff)
                result = [idx, diff_idx] if idx<=diff_idx else [diff_idx,idx]
                return result
            nums_dict[val]=idx
        
    