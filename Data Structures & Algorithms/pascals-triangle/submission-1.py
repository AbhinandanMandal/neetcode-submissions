class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # Quite interesting problem is this
        # res=[[1]]
        # for i in range(numRows-1):
        #     temp=[0]+res[-1]+[0] # Taking the last list from res and adding [0] in the front and back
        #     row=[]
        #     for j in range(len(res[-1])+1):
        #         row.append(temp[j]+temp[j+1]) # Pointer system for adding
        #     res.append(row)
        # return res

        res=[[1]]
        for i in range(numRows-1):
            temp = [0]+res[-1]+[0]
            row=[]
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res
        