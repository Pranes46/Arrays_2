class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        dirs = [[0,1],[1,0],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]  #direction array
        
        m = len(board)   #row
        n = len(board[0]) #column
        
        for i in range(m):
            for j in range(n):
                count = 0
                
                
                for r,c in dirs:
                    nr = r+i
                    nc = c+j
                    
                    if nr>=0 and nr<m and nc>=0 and nc<n:
                        if board[nr][nc]==-1 or board[nr][nc]==1:
                            count+=1
                            
                if board[i][j]==1:
                    if count<2 or count>3:
                        board[i][j] =-1
                                
                else:
                    if count==3:
                        board[i][j] =2
                            
        for i in range(m):
            for j in range(n):
                if board[i][j] ==-1:
                    board[i][j]=0
                    
                else:
                    if board[i][j] ==2:
                        board[i][j] = 1
                                    
       
                                
         