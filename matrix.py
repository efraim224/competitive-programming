class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        battleships = set()
        count = 0
        for row in range (0,len(board)):
            for column in range(0,len(board[0])):
                if board[row][column] == 'X':
                    if board[row][column] not in battleships:
                        count = count + 1
                        battleships.add((row,column)
                        for current_row in range((row + 1),len(board)):
                            if board[current_row][column] == 'X':
                                battleships.add((current_row,column)
                            else:
                                break
                        for current_col in range(0,len(board[0])):
                            if board[row][current_col] == 'X':
                                battleships.add((row,current_col))
                            else:
                                break;            
        return count
                