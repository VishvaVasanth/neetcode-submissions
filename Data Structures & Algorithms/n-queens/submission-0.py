class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDia = set()
        negDia = set()

        res = []
        board = [["."]*n for i in range(n)]

        def back(r):

            if n == r:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for  c in range(n):

                if c in col or (r-c) in negDia or (r+c) in posDia:
                    continue
                
                col.add(c)
                negDia.add(r-c)
                posDia.add(r+c)
                board[r][c] = "Q"
                back(r+1)
                col.remove(c)
                negDia.remove(r-c)
                posDia.remove(r+c)
                board[r][c] = "."

        back(0)
        return res