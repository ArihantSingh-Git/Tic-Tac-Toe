import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font

a = tk.Tk()
a.title("Tic Tac Toe")
count = 0
clicked = True

#disable all buttons when WON
def disable_button():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)



#check if someone wins
def won():
    global winner
    winner = False
#check if X won
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="#2CEA48")
        b2.config(bg="#2CEA48")
        b3.config(bg="#2CEA48")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! X WON")
        disable_button()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="#2CEA48")
        b4.config(bg="#2CEA48")
        b7.config(bg="#2CEA48")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! X WON")
        disable_button()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="#2CEA48")
        b5.config(bg="#2CEA48")
        b9.config(bg="#2CEA48")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! X WON")
        disable_button()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b5.config(bg="#2CEA48")
        b2.config(bg="#2CEA48")
        b8.config(bg="#2CEA48")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! X WON")
        disable_button()

    elif b6["text"] == "X" and b9["text"] == "X" and b3["text"] == "X":
        b6.config(bg="#2CEA48")
        b9.config(bg="#2CEA48")
        b3.config(bg="#2CEA48")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! X WON")
        disable_button()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b5.config(bg="#2CEA48")
        b4.config(bg="#2CEA48")
        b6.config(bg="#2CEA48")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! X WON")
        disable_button()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="#2CEA48")
        b8.config(bg="#2CEA48")
        b9.config(bg="#2CEA48")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! X WON")
        disable_button()
    elif b5["text"] == "X" and b7["text"] == "X" and b3["text"] == "X":
        b5.config(bg="#2CEA48")
        b7.config(bg="#2CEA48")
        b3.config(bg="#2CEA48")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! X WON")
        disable_button()

    #check if O WON
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="#862CEA")
        b2.config(bg="#862CEA")
        b3.config(bg="#862CEA")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! O WON")
        disable_button()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="#862CEA")
        b4.config(bg="#862CEA")
        b7.config(bg="#862CEA")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! O WON")
        disable_button()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="#862CEA")
        b5.config(bg="#862CEA")
        b9.config(bg="#862CEA")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! O WON")
        disable_button()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b5.config(bg="#862CEA")
        b2.config(bg="#862CEA")
        b8.config(bg="#862CEA")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! O WON")
        disable_button()

    elif b6["text"] == "O" and b9["text"] == "O" and b3["text"] == "O":
        b6.config(bg="#862CEA")
        b9.config(bg="#862CEA")
        b3.config(bg="#862CEA")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! O WON")
        disable_button()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b5.config(bg="#862CEA")
        b4.config(bg="#862CEA")
        b6.config(bg="#862CEA")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! O WON")
        disable_button()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="#862CEA")
        b8.config(bg="#862CEA")
        b9.config(bg="#862CEA")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! O WON")
        disable_button()
    elif b5["text"] == "O" and b7["text"] == "O" and b3["text"] == "O":
        b5.config(bg="#862CEA")
        b7.config(bg="#862CEA")
        b3.config(bg="#862CEA")
        winner == True
        messagebox.showinfo("Tic Tac Toe" , "CONGRATULATIONS!!!! O WON")
        disable_button()



#function of a click
def click(b):
    global count , clicked
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        won()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        won()
    else:
        messagebox.showerror("Tic Tac" , "The box is already filled!!!!\n Baaka!!")

#btn = PhotoImage(file = "C:/Users/Shainee Singh/Desktop/tkinter gui/download.png")
#img_lab = Label(image = btn)

#start th game again
def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked,count
    clicked = True
    count = 0
    #buttons
    b1 = Button(a, text = " ", font = ("Helvetica" , 40) , command = lambda: click(b1),height=1,width=2)
    b2 = Button(a, text = " ", font = ("Helvetica" , 40) , command = lambda: click(b2),height=1,width=2)
    b3 = Button(a, text = " ", font = ("Helvetica" , 40) ,command = lambda: click(b3),height=1,width=2)

    b4 = Button(a, text = " ", font = ("Helvetica" , 40) ,command = lambda: click(b4),height=1,width=2)
    b5 = Button(a, text = " ", font = ("Helvetica" , 40) ,command = lambda: click(b5),height=1,width=2)
    b6 = Button(a, text = " ", font = ("Helvetica" , 40) ,command = lambda: click(b6),height=1,width=2)

    b7 = Button(a, text = " ", font = ("Helvetica" , 40) ,command = lambda: click(b7),height=1,width=2)
    b8 = Button(a, text = " ", font = ("Helvetica" , 40) ,command = lambda: click(b8),height=1,width=2)
    b9 = Button(a, text = " ", font = ("Helvetica" , 40) ,command = lambda: click(b9),height=1,width=2)

    b1.grid(row =0 , column =0)
    b2.grid(row =0 , column =1)
    b3.grid(row =0 , column =2)

    b4.grid(row =1 , column =0)
    b5.grid(row =1 , column =1)
    b6.grid(row =1 , column =2)

    b7.grid(row =2 , column =0)
    b8.grid(row =2 , column =1)
    b9.grid(row =2 , column =2)

#create menu
menu_tab = Menu(a)
a.config(menu=menu_tab)

#create Option menu to reset the game
option = Menu(menu_tab, tearoff=False)
menu_tab.add_cascade(label = "Options" , menu = option)
option.add_command(label = "Start Over" , command = reset)


reset()
a.mainloop()
