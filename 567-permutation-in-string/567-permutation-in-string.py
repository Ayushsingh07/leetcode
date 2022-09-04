from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        perm=dict(Counter(s1))
        start=0
        res=""
        hashmap={}
        for end in range(len(s2)):
            hashmap[s2[end]]=hashmap.get(s2[end],0)+1
            if(end-start+1==k):
                if(hashmap==perm):
                    return True
                else:
                    hashmap[s2[start]]=hashmap[s2[start]]-1
                    if(hashmap[s2[start]]==0):
                        del hashmap[s2[start]]
                    if(start!=end and s2[end] not in hashmap):
                        hashmap[s2[end]]=1
                    start+=1
                
            
        return False