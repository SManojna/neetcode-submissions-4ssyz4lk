class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # list of strs
        # iterate through strs 
            # for each string -> check for the chars
            # put them in a dict -> chars of string and assign to list of strings
        # get all the values of the dict  and return 
        ana_map = {}
        for s in strs:
            sor_str = "".join(sorted(s))
            print(sor_str)
            if sor_str in ana_map:
                # append the str to the lis t
                ana_map[sor_str].append(s)
            else:
                ana_map[sor_str]=[s]
        print(ana_map)
        # sor_ana_map = sorted(ana_map)
        # print(sor_ana_map)
        ans = []
        for i in ana_map:
            ans.append(sorted(ana_map[i]))
        print(ans)
        return ans


        