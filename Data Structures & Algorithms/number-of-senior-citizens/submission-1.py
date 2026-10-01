class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ages=[individual[11:13] for individual in details]
        return sum(1 for age in ages if int(age)>60)
 
        