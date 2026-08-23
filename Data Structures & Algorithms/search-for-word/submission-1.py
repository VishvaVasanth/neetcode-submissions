class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row = len(board)
        col = len(board[0])

        path = set()

        def back(r,c,i):
            if len(word)==i:
                return True
            
            if( r<0 or c < 0 or c>=col or r >=row or ((r,c) in path) or word[i] != board[r][c]):
                return False
            path.add((r,c))
            res = (back(r+1,c,i+1) or back(r-1,c,i+1) or back(r,c+1,i+1) or back(r,c-1,i+1))
            path.remove((r,c))
            return res

        

        for r in range(row):
            for c in range(col):

                if back(r,c,0):
                    return True
        return False

        
        