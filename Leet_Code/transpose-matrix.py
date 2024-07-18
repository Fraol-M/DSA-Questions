class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[] for i in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                result[j].append(matrix[i][j])
        return result

