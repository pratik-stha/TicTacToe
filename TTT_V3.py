from tkinter import *
from tkinter import messagebox
from math import inf as infinity
from random import choice
import platform
import time
from os import system

root=Tk()
#root.geometry("354x460")
root.title("Tic Tac Toe")

HUMAN = 1
COMP = -1

def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP)

def CheckWinner(state):
    if wins(state,HUMAN):
        print("Human Wins !!")
        messagebox.showinfo("Congratulations !!","Human Wins")
        diable_all_button()

    elif wins(state,COMP):
        print("Computer Wins !!")
        messagebox.showinfo("Congratulations !!","Computer Wins")
        diable_all_button()
    
    else:
        if len(empty_cells(state))==0:
            print("Draw !!")
            messagebox.showinfo( "Congratulations !!","Draw")
            diable_all_button()
        

    


def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(state))
    if depth == 0 or game_over(state):
        return


   # print(f'Computer turn [{c_choice}]')
   # render(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(state, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)


def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score

def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    global state
    print("AI talked")
    if valid_move(x, y):
        state[x][y] = player
        render(x,y)
        return True
    else:
        return False
    #render()

def diable_all_button():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)


def render(x,y):
    global state
    if x==0 and y==0:
        print("AI talked")
        b1["text"]="O"
    
    elif x==0 and y==1:
        print("AI talked")
        b2["text"]="O"

    elif x==0 and y==2:
        print("AI talked")
        b3["text"]="O"

    elif x==1 and y==0:
        print("AI talked")
        b4["text"]="O"

    elif x==1 and y==1:
        print("AI talked")
        b5["text"]="O"

    elif x==1 and y==2:
        print("AI talked")
        b6["text"]="O"

    elif x==2 and y==0:
        print("AI talked")
        b7["text"]="O"

    elif x==2 and y==1:
        print("AI talked")
        b8["text"]="O"

    elif x==2 and y==2:
        print("AI talked")
        b9["text"]="O"
    
    print(state)


def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


# Start the game over!
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count, state
    b1=Button(root,padx= 40, pady = 40,bd=4,bg="SystemButtonFace",text=" ",command=lambda: B_click(b1),font=("Courier New",16,'bold'))
    b2=Button(root,padx= 40, pady = 40,bd=4,bg="SystemButtonFace",text=" ",command=lambda: B_click(b2),font=("Courier New",16,'bold'))
    b3=Button(root,padx= 40, pady = 40,bd=4,bg="SystemButtonFace",text=" ",command=lambda: B_click(b3),font=("Courier New",16,'bold'))
    b4=Button(root,padx= 40, pady = 40,bd=4,bg="SystemButtonFace",text=" ",command=lambda: B_click(b4),font=("Courier New",16,'bold'))
    b5=Button(root,padx= 40, pady = 40,bd=4,bg="SystemButtonFace",text=" ",command=lambda: B_click(b5),font=("Courier New",16,'bold'))
    b6=Button(root,padx= 40, pady = 40,bd=4,bg="SystemButtonFace",text=" ",command=lambda: B_click(b6),font=("Courier New",16,'bold'))
    b7=Button(root,padx= 40, pady = 40,bd=4,bg="SystemButtonFace",text=" ",command=lambda: B_click(b7),font=("Courier New",16,'bold'))
    b8=Button(root,padx= 40, pady = 40,bd=4,bg="SystemButtonFace",text=" ",command=lambda: B_click(b8),font=("Courier New",16,'bold'))
    b9=Button(root,padx= 40, pady = 40,bd=4,bg="SystemButtonFace",text=" ",command=lambda: B_click(b9),font=("Courier New",16,'bold'))
    b1.grid(row="0", column="0")
    b2.grid(row="0", column="1")
    b3.grid(row="0", column="2")
    b4.grid(row="1", column="0")
    b5.grid(row="1", column="1")
    b6.grid(row="1", column="2")
    b7.grid(row="2", column="0")
    b8.grid(row="2", column="1")
    b9.grid(row="2", column="2")
    clicked = True
    count = 0
    state=[[0,0,0],[0,0,0],[0,0,0]] 
 
def B_click(b):
    global clicked,HumanTurn,state

    if b["text"]== " " and HumanTurn == True:
        if b==b1 and state[0][0]==0:
            b["text"]='X'
            state[0][0]=HUMAN
            print(state)
            
        elif b==b2 and state[0][1]==0:
            b["text"]='X'
            state[0][1]=HUMAN
            print(state)

        elif b==b3 and state[0][2]==0:
            b["text"]='X'
            state[0][2]=HUMAN
            print(state)

        elif b==b4 and state[1][0]==0:
            b["text"]='X'
            state[1][0]=HUMAN
            print(state)

        elif b==b5 and state[1][1]==0:
            b["text"]='X'
            state[1][1]=HUMAN
            print(state)

        elif b==b6 and state[1][2]==0:
            b["text"]='X'
            state[1][2]=HUMAN
            print(state)

        elif b==b7 and state[2][0]==0:
            b["text"]='X'
            state[2][0]=HUMAN
            print(state)

        elif b==b8 and state[2][1]==0:
            b["text"]='X'
            state[2][1]=HUMAN
            print(state)

        elif b==b9 and state[2][2]==0:
            b["text"]='X'
            state[2][2]=HUMAN
            print(state)
        
        else:
            print("Click valid spot !!")   

    HumanTurn =False
    CheckWinner(state)
    ai_turn('O','X')
    CheckWinner(state)
    HumanTurn = True
 


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(state):
        return True
    else:
        return False

def main():
    # Create menue
    global state, HumanTurn
    state = [[0,0,0],[0,0,0],[0,0,0]]
    HumanTurn = True
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Create Options Menu
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Reset Game", command=reset)


    reset()
    root.mainloop()
    

if __name__ == "__main__":
    main()

