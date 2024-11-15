class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for brd in board:
            x = Counter(brd)
            del x["."]
            cpt = list(x.values())
            if any(value != 1 for value in cpt):
                return False
        
        for brd in range(len(board[0])):
            column_values = [row[brd] for row in board]
            x = Counter(column_values)
            del x["."]
            cpt = list(x.values())
            if any(value != 1 for value in cpt):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_matrix = [row[j:j+3] for row in board[i:i+3]]
                sub_matrix = [item for sublist in sub_matrix for item in sublist]
                
                x = Counter(sub_matrix)
                del x["."]
                
                cpt = list(x.values())
                if any(value != 1 for value in cpt):
                    return False
        return True