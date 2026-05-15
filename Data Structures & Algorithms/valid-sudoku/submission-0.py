class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for c in range(9):
            for d in range(9):
                val = board[c][d]
                if val == ".":
                    continue
                box_idx = ( c//3) * 3 + (d // 3)

                if val in rows[c] or val in cols[d] or val in boxes[box_idx]:
                    return False
                
                
                rows[c].add(val)
                cols[d].add(val)
                boxes[box_idx].add(val)


        return True