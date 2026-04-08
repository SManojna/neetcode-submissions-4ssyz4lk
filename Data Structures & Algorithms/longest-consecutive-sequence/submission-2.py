class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # try visualizing on number chart
        # create a set 
        # so the ones which are in seq will be togetehr ont he numebr set and we will see that there will not be any number in the 
        #beginning fof the sequence 

        # creating a set 
        num_set = set(nums)
        longest = 0 
        # legth -> length of curr seq, longest -> len of the longest seq observed so far 
        for n in num_set:
            if (n-1) not in num_set:
                # this means this number can be potential start of a seq 
                length = 0 
                while (n+length) in num_set:
                    # loop thoug to find the seq numbers in the set 
                    length +=1
                longest =  max(longest, length)
        return longest
        
        