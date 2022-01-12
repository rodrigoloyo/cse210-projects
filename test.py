"""Assigment:Tic-Tac-Toe 
   Author Names: Rodrigo Loyo"""

def main():
    print("Welcome to Tic-Tac-TOE")
    print("""
    Love is a game of tic-tac-toe,
    Constantly waiting for the next x or o.

    - Lang Leav -

    """)
    answer = None
    board = [[1,2,3], 
                        [4,5,6], 
                        [7,8,9],]
    while answer != True:
        print("function")
        board = sequence_board(board)
        print("normal")
        print("TIC TAC TOE")
        for row in board:
            print(row)
            print("+-+-+-+-+-+-+-")
        #User 1 turn
        d = int(input("insert a number for X user "))
        
        if d in board[0]:
            board[0][d-1] = "X"
            
        elif d in board[1]:
            print(board[1])
            board[1][d-4] = "X"
        elif d in board[2]:
            board[2] [d-7] = "X"

        
        print("function")
        board = sequence_board(board)
        print("normal")
        print("TIC TAC TOE")
        for row in board:
            print(row)
            print("+-+-+-+-+-+-+-")

        #User 2  turn     
        d = int(input("insert a number for O user: "))
        
        if d in board[0]:
            board[0][d-1] = "O"
            
        elif d in board[1]:
            print(board[1])
            board[1][d-4] = "O"
        elif d in board[2]:
            board[2] [d-7] = "O"

        board = sequence_board(board)
        print("function")
        print("TIC TAC TOE")
        print("normal")
        for row in board:
            print(row)
            print("+-+-+-+-+-+-+-")

        answer = check_board(board)
    
def sequence_board (board):
    for row in board:
            print(row)
            print("+-+-+-+-+-+-+-")

    return board

def check_board (board):
  """This will validate if X or O are three in the row to send True."""
   for x in board[0]:
       if  "X" != x:
           print("test")

       result = False
       break
   else:
       result = True

   return result
    

if __name__ == "__main__":
 main()