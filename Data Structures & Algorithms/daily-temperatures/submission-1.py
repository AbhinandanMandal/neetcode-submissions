class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        # This solution would be time limit exceeded
        results = []
        for i in range(len(temperatures)):
            day = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    day = j-i
                    break                    
            results.append(day)
        return results
        """
        # Another best approach
        results = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                results[prev_index] = i - prev_index
            stack.append(i)
        return results
            