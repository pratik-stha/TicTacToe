from tkinter import *
from tkinter import messagebox

root=Tk()
#root.geometry("354x460")
root.title("Tic Tac Toe")

clicked =True
count = 0

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


def CheckIfWon():
    global winner
    winner = False
    if(b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O" ):
        winner = True
        messagebox.showinfo("Winner", "Congratulations !!")
        diable_all_button()
    
    elif(b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X") or (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O" ):
        winner = True
        messagebox.showinfo("Winner", "Congratulations !!")
        diable_all_button()

    elif(b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X") or (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O" ):
        winner = True
        messagebox.showinfo("Winner", "Congratulations !!")
        diable_all_button()

    elif(b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O" ):
        winner = True
        messagebox.showinfo("Winner", "Congratulations !!")
        diable_all_button()
    
    elif(b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X") or (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O" ):
        winner = True
        messagebox.showinfo("Winner", "Congratulations !!")
        diable_all_button()

    elif(b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X") or (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O" ):
        winner = True
        messagebox.showinfo("Winner", "Congratulations !!")
        diable_all_button()

    elif(b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X") or (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O" ):
        winner = True
        messagebox.showinfo("Winner", "Congratulations !!")
        diable_all_button()

    elif(b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X") or (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O" ):
        winner = True
        messagebox.showinfo("Winner", "Congratulations !!")
        diable_all_button()

def B_click(b):
    global clicked,count
    if b["text"]== " " and clicked == True:
        b["text"]="X"
        clicked = False
        count += 1
    elif b["text"]== " " and clicked == False:
        b["text"]="O"
        clicked = True
        count += 1
    else:
        messagebox.showerror("Warning","Cannot be placed here")
    CheckIfWon()



# Start the game over!
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
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
 



# Create menue
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()

root.mainloop()