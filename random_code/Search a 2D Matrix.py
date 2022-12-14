import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        i,j=0,0

        infinity = [math.inf]*len(matrix[0])
        matrix.append(infinity)
        for t in matrix:
            t.append(math.inf)

        print(matrix)
        while i < len(matrix):
            while j<len(matrix[0]):
                print(matrix[i][j])
                if matrix[i][j]==target:
                    return True
                elif matrix[i][j+1]<=target and matrix[i+1][j]<=target:
                    i+=1
                elif matrix[i][j+1]<=target and matrix[i+1][j]>target:
                    j+=1
                elif matrix[i][j+1]>target and matrix[i+1][j]>target:
                    return False
                elif matrix[i][j+1]>target and matrix[i+1][j]<=target:
                    i+=1
                else:
                    return False    
  
             
                                                

    


