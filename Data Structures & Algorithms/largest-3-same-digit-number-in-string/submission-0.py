class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        for i in range(len(num)-2):
            # If the corresponding 3 elements are same (condition is given)
            if num[i] == num[i+1] == num[i+2]:
                current = num[i:i+3] # taking the whole 3 current
                if current > max_good:
                    max_good = current
        return max_good