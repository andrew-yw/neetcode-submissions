class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter, defaultdict
        #check rows
        nrows = len(board)
        ncols = len(board[0])

        for i in range(nrows):
            row = {}
            for j in range(ncols):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in row:
                    return False
                else:
                    row[board[i][j]] = 1
        

        #check columns
        for i in range(ncols):
            column = {}
            for _ in range(nrows):
                if board[_][i] == '.':
                    continue
                
                if board[_][i] in column:
                    return False
                else:
                    #initialise this number
                    column[board[_][i]] = 1
        
        #check box
        box = defaultdict(set)
        for i in range(nrows):
            for j in range(ncols):
                box_number = (i//3+1, j//3+1)
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in box[box_number]:
                    return False
                else:
                    box[box_number].add(board[i][j])
        
        return True
                
                
                
                    


            
                