class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        array = [[1] *(i+1) for i in range(n)]
        for i in range(n):
            for j in range(1,i):
                array[i][j] = array[i-1][j] + array[i-1][j-1]
        
        return array