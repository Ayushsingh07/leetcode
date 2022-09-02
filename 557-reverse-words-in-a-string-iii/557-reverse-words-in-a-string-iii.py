class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(" ")
        t=[]
        s1=""
        for i in l:
            s1+=i[::-1]
            s1+=" "
        return s1[:len(s1)-1]
            
            