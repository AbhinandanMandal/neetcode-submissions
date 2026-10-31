class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        final_prices = []
        n = len(prices)
        
        for i in range(n):
            discount = 0
            for j in range(i+1, n):
                if prices[i]>=prices[j]:
                    discount = prices[j]
                    break
            final_prices.append(prices[i] - discount)
        return final_prices
