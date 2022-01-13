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
    count = 0
    board = [[1,2,3], 
                        [4,5,6], 
                        [7,8,9],]
    while answer != True:
        
        
        print("TIC TAC TOE")
        board = sequence_board(board)
        
 
        #User 1 turn
        d = int(input("insert a number for X user "))
        
        if d in board[0]:
            board[0][d-1] = "X"            
        elif d in board[1]:
            print(board[1])
            board[1][d-4] = "X"
        elif d in board[2]:
            board[2] [d-7] = "X"
      
        
        print("TIC TAC TOE")
        board = sequence_board(board)
        if count == 4:
              print("Well played, but no one wins")
              answer = True
              break

        answer = check_board(board)

        if answer == True:
                print("user X Wins")
                break
         
        answer = check_board_column(board)
        if answer == True:
            print("user X Wins")
            break 
        answer = check_board_diagonal(board)
        if answer == True:
            print("user X Wins")
            break 
         
     
        #User 2  turn     
        d = int(input("insert a number for O user: "))
        
        if d in board[0]:
            board[0][d-1] = "O"            
        elif d in board[1]:
            print(board[1])
            board[1][d-4] = "O"
        elif d in board[2]:
            board[2] [d-7] = "O"

        print("TIC TAC TOE")
        board = sequence_board(board)
        
        
        answer = check_board(board)

        if answer == True:
                print("user O Wins")
                break
        answer = check_board_column(board)
        if answer == True:
            print("user O Wins")
            break 
        answer = check_board_diagonal(board)
        if answer == True:
            print("user O Wins")
            break 
        count +=1 
        print(count)
        if count == 5:
              print("no one wins")
              answer = True
        
     
    
def sequence_board (board):
    for row in board:
            print(row)
            print("+-+-+-+-+-+-+-")

    return board

def check_board (board):
   """This will validate if X or O are three in the row to send True."""

   for i in board:
        row_1 = board[0]
        row_2 = board[1]
        row_3 = board[2]
   for j in row_1:
        index_1 = row_1[0]
        index_2 = row_1[1]
        index_3 = row_1[2]

   for k in row_2:
        index_4 = row_2[0]
        index_5 = row_2[1]
        index_6 = row_2[2]

   for l in row_3:
        index_7 = row_3[0]
        index_8 = row_3[1]
        index_9 = row_3[2]
        
   

   if index_1 == index_2== index_3:
        
        
           result = True
        
        
   elif index_4 == index_5 == index_6:
        
       result = True

   elif index_7 == index_8 == index_9:
       
        result = True
    
   else:
            result = False
    
          
     
   return result

    
 
def check_board_column(board):
    
    result = None
    for i in board:
        row_1 = board[0]
        row_2 = board[1]
        row_3 = board[2]
    for j in row_1:
        index_1 = row_1[0]
        index_2 = row_1[1]
        index_3 = row_1[2]

    for k in row_2:
        index_4 = row_2[0]
        index_5 = row_2[1]
        index_6 = row_2[2]

    for l in row_3:
        index_7 = row_3[0]
        index_8 = row_3[1]
        index_9 = row_3[2]
        
   

    if index_1 == index_4 == index_7:
        
        
           result = True
        
        
    elif index_2 == index_5 == index_8:
        
       result = True

    elif index_3 == index_6 == index_9:
       
        result = True
    
    else:
            result = False
    
          
     
    return result

def check_board_diagonal(board):
    
    
    result = None
    for i in board:
        row_1 = board[0]
        row_2 = board[1]
        row_3 = board[2]
    for j in row_1:
        index_1 = row_1[0]
        index_2 = row_1[1]
        index_3 = row_1[2]

    for k in row_2:
        index_4 = row_2[0]
        index_5 = row_2[1]
        index_6 = row_2[2]

    for l in row_3:
        index_7 = row_3[0]
        index_8 = row_3[1]
        index_9 = row_3[2]
        
   

    if index_1 == index_5 == index_9:
        
           print("true")
           result = True
        
        
    elif index_3 == index_5 == index_7:
        
       result = True
 
    
    else:
            
            result = False
    
          
     
    return result



if __name__ == "__main__":
 main()