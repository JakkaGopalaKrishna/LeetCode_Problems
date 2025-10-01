class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty=0
        Number_of_bottles_drink=0
        while(numBottles+empty>=numExchange):
            Number_of_bottles_drink+=numBottles
            empty+=numBottles
            numBottles=empty//numExchange
            empty%=numExchange

        return Number_of_bottles_drink+numBottles