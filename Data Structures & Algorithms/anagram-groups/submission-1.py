class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter={}
        for s in strs:
            s_string=tuple(sorted(s))
            if s_string in counter:
                counter[s_string].append(s)
            else:
                counter[s_string]=[s]
        
        return(list(counter.values()))