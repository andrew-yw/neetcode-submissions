class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict 
        new_dict = defaultdict(list)
        
        for item in strs:
            fingerprint = [0]*26
            for i in item:
                index = ord(i)-ord('a')+1
                fingerprint[index] += 1
            
            fingerprint = tuple(fingerprint)
            new_dict[fingerprint].append(item)
        
        result = []
        for i in new_dict:
            result.append(new_dict[i])
        
        return result


        
    





            