class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for elmt in strs:
            code += f"{len(elmt)}#{elmt}"
        return code

    def decode(self, s: str) -> List[str]:
        i = 0
        decode = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            
            word = s[j +1 :j+1+length]
            decode.append(word)
            i = j+1+length
        return decode
            
                 
        

