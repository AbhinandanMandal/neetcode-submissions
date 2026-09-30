class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """  
        # Bruteforce approach, time complexity O(n^2)
        for i in range(len(arr)-1):
            arr[i]=max(arr[i+1:])
        arr[-1]=-1
        return arr
        """
        # Efficient approach
        rightMax=-1
        for i in range(len(arr)-1, -1, -1):
            newMax=max(rightMax, arr[i])
            arr[i]=rightMax
            rightMax=newMax
        return arr



        