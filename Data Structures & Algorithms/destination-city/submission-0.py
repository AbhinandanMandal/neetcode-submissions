class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starting = []

        for i in range(len(paths)):
            starting.append(paths[i][0]) # adding first city into starting

        for j in range(len(paths)):
            if paths[j][1] not in starting:
                return paths[j][1]