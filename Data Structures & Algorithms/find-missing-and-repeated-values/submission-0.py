class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # 1. From 2D array to 1D array & length 1D array
        # 2. 1D array hash
        # 3. 1D array without repetating
        # 4. Finding missing value

        array = []
        miss_repeat=[]
        # 2D to 1D array
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                array.append(grid[i][j])

        # Array hash for repetation
        array_hash = {}
        for n in array:
            array_hash[n] = array_hash.get(n, 0)+1
        
        # repetating value
        for key, val in array_hash.items():
            if val>1:
                miss_repeat.append(key)

        # Missing value
        for i in range(1, len(array)+1):
            if i not in array:
                miss_repeat.append(i)
        return miss_repeat





        


