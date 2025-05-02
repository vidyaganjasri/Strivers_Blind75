'''
1. Using Auxiliary Space (Not In-place):
You create a new matrix of the same size.
For each element at position matrix[i][j], you place it in the new matrix at rotated[j][n - i - 1].
Time Complexity: O(n²)
Space Complexity: O(n²) (due to the extra matrix)
'''

'''
2. In-place Rotation (Transpose + Reverse):
Step 1: Transpose the matrix
Swap matrix[i][j] with matrix[j][i] (only for j > i to avoid re-swapping).
Step 2: Reverse each row
Time Complexity: O(n²)
Space Complexity: O(1) (in-place)
'''

def rotate(self, matrix):
        
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        '''
        res = []
        for i in range(len(matrix)):
            curr = []
            for j in range(len(matrix)):
                curr.append(matrix[len(matrix)-j-1][i])
            res.append(curr)

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = res[i][j]
                
        
        return matrix
        '''
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j], matrix[j][i]= matrix[j][i],matrix[i][j]
        
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        return matrix
