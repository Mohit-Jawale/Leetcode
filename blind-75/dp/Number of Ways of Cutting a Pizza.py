class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        
        dp = [[[ -1 for k in range(11)]for j in range(51)]for i in range(51)]
        MOD = pow(10,9)+7
        row = len(pizza)
        col = len(pizza[0])
        apples = [[0 for c in range(col+1)]for r in range(row+1)]

        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                apples[i][j] = apples[i][j+1]+ apples[i+1][j] - apples[i+1][j+1] +int(pizza[i][j]=='A')
                

        def count(r,c,cuts):
            if dp[r][c][cuts] != -1:
                return dp[r][c][cuts]
            if cuts == 0:
                if apples[r][c]>0:
                    dp[r][c][cuts] = 1
                else:
                    dp[r][c][cuts]= 0
                return dp[r][c][cuts]            

            rowsum = 0 
            colsum = 0
            #row cuts
            for i in range(r+1,row):
                if apples[r][c]-apples[i][c]>0 and apples[i][c]>=cuts:
                    rowsum = (rowsum + count(i,c,cuts-1))%MOD

            for j in range(c+1,col):
                if apples[r][c]-apples[r][j]>0 and apples[r][j]>=cuts:
                    colsum = (colsum+ count(r,j,cuts-1))%MOD


            dp[r][c][cuts] = rowsum +colsum
            return dp[r][c][cuts]

        return(count(0,0,k-1))
        
