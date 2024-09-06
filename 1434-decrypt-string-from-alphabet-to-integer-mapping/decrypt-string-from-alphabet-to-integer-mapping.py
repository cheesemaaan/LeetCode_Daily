class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        result = []
        i = 0 
        n = len(s)
        while i < n:
            if i+2 < n and s[i+2] == "#":
                num=s[i:i+2]
                result.append(chr(int(num)+96))
                i+=3
            else:
                result.append(chr(int(s[i])+96))
                i+=1
        return ''.join(result)
        