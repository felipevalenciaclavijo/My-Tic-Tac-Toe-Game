'''
Tic-Tac-Toe: My Tic-Tac-Toe 
Author: Felipe Valencia
'''

grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turns = ["X"]

def main():

    game_result = [""]
    question_counter = 0

    while game_result[0] == "":

        game_result[0] = game_results(grid, question_counter)
        
        print_grid()
        
        if game_result[0] == "wins":
            if turns[0] == "O":
                print("X wins!")
                print("Good game. Thanks for playing!")
            else:
                print("O wins!")
                print("Good game. Thanks for playing!")
        elif game_result[0] == "draw":
            print("Draw!")
            print("Good game. Thanks for playing!")
        else:            
            question = str(input(f"{turns[0]}'s turn to choose a square (1-9): "))

            if question == "1":
                grid[0] = turns[0]
                question_counter += 1
            elif question == "2":
                grid[1] = turns[0]
                question_counter += 1
            elif question == "3":
                grid[2] = turns[0]
                question_counter += 1
            elif question == "4":
                grid[3] = turns[0]
                question_counter += 1
            elif question == "5":
                grid[4] = turns[0]
                question_counter += 1
            elif question == "6":
                grid[5] = turns[0]
                question_counter += 1
            elif question == "7":
                grid[6] = turns[0]
                question_counter += 1
            elif question == "8":
                grid[7] = turns[0]
                question_counter += 1
            elif question == "9":
                grid[8] = turns[0]
                question_counter += 1

        next = turn(turns)
        turns[0] = next

# FUNCTIONS

def print_grid():

    # Printed grid
    print()
    print(f"{grid[0]}|{grid[1]}|{grid[2]}")
    print("-+-+-")
    print(f"{grid[3]}|{grid[4]}|{grid[5]}")
    print("-+-+-")
    print(f"{grid[6]}|{grid[7]}|{grid[8]}")
    print()


def game_results(grid, question_counter):

    # Horizontal Wins
    if grid[0] == 'X' and grid[1] == 'X' and grid[2] == 'X':
        result = "wins"
    elif grid[0] == 'O' and grid[1] == 'O' and grid[2] == 'O':
        result = "wins"
    elif grid[3] == 'X' and grid[4] == 'X' and grid[5] == 'X':
        result = "wins"
    elif grid[3] == 'O' and grid[4] == 'O' and grid[5] == 'O':
        result = "wins"
    elif grid[6] == 'X' and grid[7] == 'X' and grid[8] == 'X':
        result = "wins"
    elif grid[6] == 'O' and grid[7] == 'O' and grid[8] == 'O':
        result = "wins"
    # Vertical Wins
    elif grid[0] == 'X' and grid[3] == 'X' and grid[6] == 'X':
        result = "wins"
    elif grid[0] == 'O' and grid[3] == 'O' and grid[6] == 'O':
        result = "wins"
    elif grid[1] == 'X' and grid[4] == 'X' and grid[7] == 'X':
        result = "wins"
    elif grid[1] == 'O' and grid[4] == 'O' and grid[7] == 'O':
        result = "wins"
    elif grid[2] == 'X' and grid[5] == 'X' and grid[8] == 'X':
        result = "wins"
    elif grid[2] == 'O' and grid[5] == 'O' and grid[8] == 'O':
        result = "wins"
    # Diagonal Wins
    elif grid[0] == 'X' and grid[4] == 'X' and grid[8] == 'X':
        result = "wins"
    elif grid[0] == 'O' and grid[4] == 'O' and grid[8] == 'O':
        result = "wins"
    elif grid[6] == 'X' and grid[4] == 'X' and grid[2] == 'X':
        result = "wins"
    elif grid[6] == 'O' and grid[4] == 'O' and grid[2] == 'O':
        result = "wins"
    # Draw
    elif question_counter == 9:
        result = "draw"
    # nothing happened yet
    else:
        result = ""

    return result

def turn(turns):
        if turns[0] == "X":
            next_turn = "O"
        if turns[0] == "O":
            next_turn = "X"

        return next_turn

if __name__ == "__main__":
    main()