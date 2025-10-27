class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        i=0
        res=0
        while i<len(bank):
            iC=bank[i].count('1')
            j=i+1
            if iC!=0:
                while j<len(bank):
                    jC=bank[j].count('1')
                    if jC!=0:
                        res+=iC*jC
                        break 
                    else:
                        j+=1
                i=j
            else:
                i+=1
        return res