class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l=text.split(' ')
        re=0
        for w in l:
            f=1
            for c in brokenLetters:
                if c in w:
                    f=0
                    break
            if f:
                re+=1
        return re