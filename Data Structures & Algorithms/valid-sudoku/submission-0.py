class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                nums = board[r][c]
                if nums == ".":
                    continue

                box= (r//3 * 3) + (c//3)

                if (nums in rows[r] or
                    nums in cols[c] or
                    nums in boxes[box]):
                    return False
                
                rows[r].add(nums)
                cols[c].add(nums)
                boxes[box].add(nums)
        return True
                    
                
