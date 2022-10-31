class Solution:
    def totalNQueens(self, n: int) -> int:
        
        rows = set()
        cols = set()
        diffs = set()
        anti_diffs = set()
        
        def is_not_under_attack(row,col):
            
            diff = (row - col)
            anti_diff = (row+col)
            if row in rows or col in cols or diff in diffs or anti_diff in anti_diffs:
                return False
            else:
                    return True
            
        
        def place_queen(row,col):
            rows.add(row)
            cols.add(col)
            diffs.add((row-col))
            anti_diffs.add((row+col))
        
        def remove_queen(row,col):
            rows.remove(row)
            cols.remove(col)
            diffs.remove((row-col))
            anti_diffs.remove((row+col))
            
        
        def backtracking(row,count):
            
            for col in range(n):
                if is_not_under_attack(row,col):
                    place_queen(row,col)
                    
                    if row+1 == n:
                        count+=1
                    else:
                        count = backtracking(row+1,count)
                       
                    remove_queen(row,col) 
            
            return count
        
        return(backtracking(0,0))
                
