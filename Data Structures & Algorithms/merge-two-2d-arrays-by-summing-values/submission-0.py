class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """
        Two pointer algorithm of this problem
        ------------------------------------------------------------------------------
        Initialize Pointers and Result List:
            Create an empty list res to store the merged output.
            Initialize two pointers, i = 0 for nums1 and j = 0 for nums2.
            Store the lengths of both arrays as n = len(nums1) and m = len(nums2).

        Iterate Through Both Arrays:
            While both pointers are within bounds (i < n and j < m):
            Extract the ID and value from the current elements: id1, val1 = nums1[i] and id2, val2 = nums2[j].

            Case 1 (IDs are equal):
                Add [id1, val1 + val2] to res (summing their values).
                Increment both i and j by 1.

            Case 2 (id1 < id2):
                Add [id1, val1] to res (since id1 is smaller and unique to nums1).
                Increment i by 1.

            Case 3 (id1 > id2):
                Add [id2, val2] to res (since id2 is smaller and unique to nums2).
                Increment j by 1.

        Handle Remaining Elements:
            If any elements are left over in nums1 (i.e., i < n), append all remaining elements from nums1 to res.
            If any elements are left over in nums2 (i.e., j < m), append all remaining elements from nums2 to res.

        Return Result:
            Return the fully merged res list in increasing ID order.
        """
        res=[]
        i,j = 0,0
        n,m = len(nums1), len(nums2)

        while i<n and j<m:
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]

            if id1 == id2:
                res.append([id1, val1+val2])
                i+=1
                j+=1
            elif id1>id2:
                res.append([id2, val2])
                j+=1
            else:
                res.append([id1, val1])
                i+=1
        
        # For remaining elements
        while i<n:
            res.append(nums1[i])
            i+=1
        while j<m:
            res.append(nums2[j])
            j+=1
        return res