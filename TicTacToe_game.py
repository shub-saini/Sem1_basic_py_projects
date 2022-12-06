# Define the board
board = [[' ', ' ', ' '], 
         [' ', ' ', ' '], 
         [' ', ' ', ' ']] 
  
# Define the players 
player1 = 'X'
player2 = 'O' 
 
# Define current player
current_player = player1
  
# Define a function to print the board
def print_board(): 
    print('   |   |')
    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])
    print('   |   |')

# Define a function to check if the game has been won
def check_game_won(): 
    # Check rows
    row_winner = check_rows() 
    # Check columns
    column_winner = check_columns() 
    # Check diagonals 
    diagonal_winner = check_diagonals() 
    if row_winner: 
        # There was a win 
        winner = row_winner 
    elif column_winner: 
        # There was a win 
        winner = column_winner 
    elif diagonal_winner: 
        # There was a win 
        winner = diagonal_winner 
    else: 
        # There was no win 
        winner = None

    return winner

# Define a function to check the rows
def check_rows(): 
    # Set the global variable 
    global game_still_going 
    # Check if any of the rows have all the same value (and is not empty) 
    row_1 = board[0][0] == board[0][1] == board[0][2] != ' '
    row_2 = board[1][0] == board[1][1] == board[1][2] != ' '
    row_3 = board[2][0] == board[2][1] == board[2][2] != ' '
    # If any row does have a match, flag that there is a win 
    if row_1 or row_2 or row_3: 
        game_still_going = False
    # Return the winner 
    if row_1: 
        return board[0][0] 
    elif row_2: 
        return board[1][0] 
    elif row_3: 
        return board[2][0] 
    # Or return None if there was no winner 
    else: 
        return None

# Define a function to check the columns
def check_columns(): 
    # Set the global variable 
    global game_still_going 
    # Check if any of the columns have all the same value (and is not empty) 
    column_1 = board[0][0] == board[1][0] == board[2][0] != ' '
    column_2 = board[0][1] == board[1][1] == board[2][1] != ' '
    column_3 = board[0][2] == board[1][2] == board[2][2] != ' '
    # If any column does have a match, flag that there is a win 
    if column_1 or column_2 or column_3: 
        game_still_going = False
    # Return the winner 
    if column_1: 
        return board[0][0] 
    elif column_2: 
        return board[0][1] 
    elif column_3: 
        return board[0][2] 
    # Or return None if there was no winner 
    else: 
        return None

# Define a function to check the diagonals
def check_diagonals(): 
    # Set the global variable 
    global game_still_going 
    # Check if any of the diagonals have all the same value (and is not empty) 
    diagonal_1 = board[0][0] == board[1][1] == board[2][2] != ' '
    diagonal_2 = board[0][2] == board[1][1] == board[2][0] != ' '
    # If any diagonal does have a match, flag that there is a win 
    if diagonal_1 or diagonal_2: 
        game_still_going = False
    # Return the winner 
    if diagonal_1: 
        return board[0][0] 
    elif diagonal_2: 
        return board[0][2]
    # Or return None if there was no winner 
    else: 
        return None

# Define a function to check if the board is full
def check_board_full(): 
    # Set the global variable 
    global game_still_going 
    # Check if any of the squares are empty 
    if " " in board[0] or " " in board[1] or " " in board[2]: 
        return False
    # If none of the squares are empty, flag that the game is over
    else: 
        game_still_going = False
        return True

# Define a function to switch players
def switch_player(): 
    # Set the global variable 
    global current_player 
    # If the current player was X, then change it to O 
    if current_player == 'X': 
        current_player = 'O'
    # If the current player was O, then change it to X 
    elif current_player == 'O': 
        current_player = 'X'

# Define a function to play the game
def play_game(): 
    # Set the global variable 
    global current_player 
    # Print out the board 
    print_board() 
    # Check if the game has been won 
    game_won = check_game_won() 
    # Check if the board is full
    board_full = check_board_full() 
    # Keep playing the game until it is won or the board is full 
    while game_won == None and not board_full: 
        # Get the current player's position 
        if current_player == 'X': 
            position = player_x_position() 
        elif current_player == 'O': 
            position = player_o_position() 
        # Place the position on the board 
        place_marker(position) 
        # Print the board 
        print_board() 
        # Check if the game has been won 
        game_won = check_game_won() 
        # Check if the board is full 
        board_full = check_board_full() 
        # Switch players 
        switch_player() 
    # Check if there was a winner 
    if game_won: 
        print(game_won + ' won!') 
    elif board_full: 
        print('Tie!')

# Define a function for player X's position
def player_x_position(): 
    # Prompt player 1 
    print('Player 1: Choose your position (1-9)') 
    # Ask player 1 to enter his/her position 
    position = input() 
    # Check if the position is available 
    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']: 
        print('Invalid position. Please choose a valid position (1-9).') 
        position = input() 
    # Convert the position to a list index 
    position = int(position) - 1 
    # Check if the position is empty 
    while board[position//3][position%3] != ' ': 
        print('Position already taken. Please choose another position.') 
        position = int(input()) - 1 
    return position 

# Define a function for player O's position 
def player_o_position(): 
    # Prompt player 2 
    print('Player 2: Choose your position (1-9)') 
    # Ask player 2 to enter his/her position 
    position = input() 
    # Check if the position is available 
    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']: 
        print('Invalid position. Please choose a valid position (1-9).') 
        position = input() 
    # Convert the position to a list index 
    position = int(position) - 1 
    # Check if the position is empty 
    while board[position//3][position%3] != ' ': 
        print('Position already taken. Please choose another position.') 
        position = int(input()) - 1 
    return position 

# Define a function to place the marker
def place_marker(position): 
    # Set the global variable 
    global board, current_player 
    # Place the marker on the position for the current player 
    board[position//3][position%3] = current_player

# Call the play_game() function
play_game()