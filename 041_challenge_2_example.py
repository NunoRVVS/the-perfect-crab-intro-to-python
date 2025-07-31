# Video alternative: https://vimeo.com/954334009/67af9910fc#t=0

# Nice work on that last one! You might well want to consider taking the
# assessment at this point.

# However, if you did want some more challenge, here it is.

# We're going to tackle something really sophisticated. We're going to build a
# tic tac toe game!

# This will introduce us to lists of lists. Here's one:

a_list_of_lists = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25]
]


# And to get items out we index in twice:
a_list_of_lists[0][0] # Evaluates to 1
a_list_of_lists[0][1] # Evaluates to 2
a_list_of_lists[0][2] # Evaluates to 3
a_list_of_lists[1][0] # Evaluates to 4
# Et cetera.

# Looks kind of like a grid right? We can use it to represent a tic-tac-toe
# board:

completed_board = [
  ["X", "O", "X"],
  ["O", "X", "O"],
  ["O", "X", "O"]
]

# We're going to implement a little game. We'll need three functions:

# 1. A function to format the board for the user.
# 2. A function to make a move.
# 3. A function to check if the game is over.


# Let's test it out:

starter_board = [
  [".", ".", ".", ".", "."],
  [".", ".", ".", ".", "."],
  [".", ".", ".", ".", "."],
  [".", ".", ".", ".", "."],
  [".", ".", ".", ".", "."]
]

# print("Our starting board:")
# print(print_board(starter_board))

# And try it out:

# print("After a move:")
# print(print_board(make_move(starter_board, 0, 0, "X")))

# Now let's write a few functions to check if the game is over:
def generate_groups_to_check(board_size):
  groups = []
  for row in range(0, board_size):
    row_group = []
    col_group = []
    for col in range(0, board_size):
      row_group.append((row, col))
      col_group.append((col, row))
    groups.append(row_group)
    groups.append(col_group)
  diag_fwd = []
  diag_bwd = []
  for i in range(0, board_size):
    diag_fwd.append((i, i))
    diag_bwd.append((i, board_size - i - 1))
  groups.append(diag_bwd)
  groups.append(diag_fwd)
  return groups

def play_game(board_size):
  board = make_blank_board(board_size)
  player = "X" # We'll start with player X
  while not is_game_over(board, board_size):
    print(print_board(board))
    print("It's " + player + "'s turn.")
        # `input` asks the user to type in a string
    # We then need to convert it to a number using `int`
    row = int(input("Enter a row: "))
    column = int(input("Enter a column: "))
    if not is_move_valid(board, row, column):
      print("Invalid move! Try again.")
      continue
    board = make_move(board, row, column, player)
    if player == "X":
      player = "O"
    else:
      player = "X"
  print(print_board(board))
  print("Game over!")

def make_blank_board(board_size):
  grid = []
  for row in range(0, board_size):
    row = ["."] * board_size
    grid.append(row)
  return grid

# Exercise 1 This function checks if a move is valid
def is_move_valid(board, row, column):
  return board[row][column] == "."

def print_board(board):
  formatted_rows = []
  for row in board:
    formatted_rows.append(" ".join(row))
  grid = "\n".join(formatted_rows)
  return grid

def make_move(board, row, column, player):
  board[row][column] = player
  return board

def get_cells_by_list(board, coords):
  cells = []
  for coord in coords:
    cells.append(board[coord[0]][coord[1]])
  return cells

# This function will check if the group is fully placed with player marks, no
# empty spaces.
def is_group_complete(board, coords):
  cells = get_cells_by_list(board, coords)
  return "." not in cells

# This function will check if the group is all the same
# player mark: X X X or O O O
def are_all_cells_the_same(board, coords):
  cells = get_cells_by_list(board, coords)
  return cells[0] == cells[1] and cells[1] == cells[2]

def is_game_over(board, board_size):
  # board = make_blank_board(board_size)
  groups_to_check = generate_groups_to_check(board_size)
  if is_game_draw(board):
    return True
  # We go through our groups
  for group in groups_to_check:
    # If any of them are empty, they're clearly not a winning row, so we skip
    # them.
    if is_group_complete(board, group):
      if are_all_cells_the_same(board, group):
        return True # We found a winning row!
  return False # If we get here, we didn't find a winning row

def is_game_draw(board):
  for row in board:
    if "." in row:
      return False
    print("It's a draw!")
  return True # If we get here, the board is full and no one has won, so it's a draw

# And try it out:
print("Game time!")
play_game(3)

# @TASK Run this file to play the game.

# Once you're done, move on to 042_challenge_2_exercise.py
