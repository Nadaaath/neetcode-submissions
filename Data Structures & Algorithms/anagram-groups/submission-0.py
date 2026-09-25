class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D={}
        for word in strs:
            s=''.join(sorted(word))
            if s in D:
                D[s].append(word)
            else:
                D[s]=[word]
        return list(D.values())

                

                

            
 