class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        n = row*col
        root  = [i for i in range(n)]
        rank = [1]*n

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x,y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX]> rank[rootY]:
                    root[rootY]=rootX
                elif rank[rootY]> rank[rootX]:
                    root[rootX]= rootY
                else:
                    root[rootY]=rootX
                    rank[rootX]+=1


        components = collections.defaultdict(list)
        lookup = {}

        def get_row_num(i,j):
            return col*i+j
        def check_if_on_edge(i,j):
            if i==0:
                return "E"
            if i+1 == row:
                return "E"
            if j==0:
                return "E"
            if j+1 == col:
                return "E"            


        for i in range(row):
            for j in range(col):
              if board[i][j] == 'O': 
                if get_row_num(i,j) in lookup:
                    continue
                lookup[get_row_num(i,j)]= check_if_on_edge(i,j)
                
                if i!=row-1:
                    if board[i+1][j] == 'O' and get_row_num(i+1,j) in lookup:
                        union(get_row_num(i,j),get_row_num(i+1,j))
                if i>0:        
                    if board[i-1][j] == 'O' and get_row_num(i-1,j) in lookup:
                        union(get_row_num(i,j),get_row_num(i-1,j))
                if j!=col-1:        
                    if board[i][j+1] == 'O' and get_row_num(i,j+1) in lookup:
                        union(get_row_num(i,j),get_row_num(i,j+1))
                if j>0 :        
                    if board[i][j-1] == 'O' and get_row_num(i,j-1) in lookup:
                        union(get_row_num(i,j),get_row_num(i,j-1)) 



        for i in range(row):
            for j in range(col):
                num = get_row_num(i,j)
                if board[i][j]!='X':
                    components[find(num)].append((i,j,lookup[num]))
                
                    
                
        delete = set()
        for i in components:
            temp = []
            for j in components[i]:
                    if board[j[0]][j[1]] != 'X' and j[2]!="E":
                        temp.append(j)
                    else:
                        delete.add(i)

        for i in delete:
            del components[i]      


        for i in components:
            for j in components[i]:
                board[j[0]][j[1]]= 'X' 
