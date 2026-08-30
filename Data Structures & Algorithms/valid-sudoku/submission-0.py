class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colhash = {i:[] for i in range(9)}
        rowhash = {i:[] for i in range(9)}
        sqhash = {i:[] for i in range(9)}

        for i in range(9):
            for j in range(9):
                cur = board[i][j]

                if cur == '.':
                    continue
                if cur not in colhash[j]:
                    colhash[j].append(cur)
                else: return False

                if cur not in rowhash[i]:
                    rowhash[i].append(cur)
                else: return False

                sq = (i//3)*3+(j//3)
                if cur not in sqhash[sq]:
                    sqhash[sq].append(cur)
                else: return False
                
        return True