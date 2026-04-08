
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first implement a hashmap to see count of all the intergers in nums 
        # implement a hashmap with counr and list of integers with the count 
        # based on the required frequency, append them the nums to list and display the list 

        nums_count = defaultdict(int)
        for n in nums:
            nums_count[n] +=1
        count_nums = defaultdict(list)
        for num, count in nums_count.items():
            count_nums[count].append(num)
        res = []
        for i in range (len(nums),0,-1):
            if count_nums[i]!=[] and k>0:
                for cn in count_nums[i]:
                    if k>0:
                        res.append(cn)
                        k-=1

        return res
        