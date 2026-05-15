class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s=s.replace(" ","")
        # forward = ("".join(s)).lower()
        # backward = ("".join(reversed(s))).lower()
        # print(backward)
        # print(forward)
        # if forward == backward:
        #     return True
        # return False
        forward = []
        for i in s:
            if i.isalnum():
                (forward.append(i.lower()))
    
        backward = list(reversed(forward))
        print(backward)
        if backward == forward:
            return True
    


        return False
        
        
        