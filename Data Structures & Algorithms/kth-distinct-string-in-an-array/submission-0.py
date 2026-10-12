class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr_hash={}
        for char in arr:
            arr_hash[char] = arr_hash.get(char, 0)+1
        distinct_str=[]
        for key,val in arr_hash.items():
            if val==1:
                distinct_str.append(key)
        if len(distinct_str)<k:
            return ""
        else:
            return distinct_str[k-1]


        