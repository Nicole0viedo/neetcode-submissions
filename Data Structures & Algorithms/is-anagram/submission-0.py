class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenS = dict()
        seenT = dict()

        for i in s:
            if i not in seenS:
                seenS[i] = 1
            else:
                seenS[i] +=1
        for i in t:
            if i not in seenT:
                seenT[i] = 1
            else:
                seenT[i] +=1
        
        if seenS == seenT:
            return True
        return False
            


        