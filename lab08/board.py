

class TicTacToeBoard:
    def __init__(self):
        self.restart()

    def get(self, row: int, col: int):
        return self._board[row][col]
    
    def is_empty(self, row: int, col: int):
        return True if self._board[row][col] == '-' else False
    
    def place(self,marker: str, row: int, col: int):
        if marker == 'X' or marker == 'O':
            self._board[row][col] = marker
            return True
        return False
    
    def is_full(self):
        for row in self._board:
            for col in row:
                
                if col != 'X' and col != 'O':
                    return False
        return True
    
    def is_winner(self,marker: str):
        #Horisontell
        for row in self._board:
            if all(i == row[0] for i in row) and row[0] == marker:
                return True
        #Vertikal
        for i in range(3):
            if all(row[i] == self._board[0][i] for row in self._board) and row[i] == marker:
                return True
        #Diagonal
        if (self._board[0][0] == self._board[1][1] == self._board[2][2] or self._board[0][2] == self._board[1][1] == self._board[2][0]) and marker == self._board[1][1]:
            return True
        return False

            
                


    def restart(self):
        self._board = [
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]
        ]

    def print_board(self):
        for row in self._board:
            for col in row:
                print(col, end =" ")
            print()
if __name__ == '__main__':

    t = TicTacToeBoard()
    t.place('X',0,0)
    print(t.print_board())
