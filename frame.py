from tkinter import *
from tkinter import messagebox

# creating window for game
window = Tk()
window.title("TicTacToe")
window.resizable(False, False)


def play():
    play.clicked = 1
    play.count = 0
    play.flag = 0

    # label for photos
    play.X = PhotoImage(file="X.png")
    play.O = PhotoImage(file="O.png")

    def images():
        labelphoto_b1 = Label(window)
        labelphoto_b2 = Label(window)
        labelphoto_b3 = Label(window)
        labelphoto_b4 = Label(window)
        labelphoto_b5 = Label(window)
        labelphoto_b6 = Label(window)
        labelphoto_b7 = Label(window)
        labelphoto_b8 = Label(window)
        labelphoto_b9 = Label(window)
        return labelphoto_b9, labelphoto_b8, labelphoto_b7, labelphoto_b6, labelphoto_b5, labelphoto_b4, labelphoto_b3, labelphoto_b2, labelphoto_b1

    # create buttons
    b1 = Button(window, text=" ", bg="#ADD8E6", font=("Gilroy", 30), height=3, width=6,
                command=lambda: b_click(b1, 2, 0))
    b2 = Button(window, text=" ", bg="#ADD8E6", font=("Gilroy", 30), height=3, width=6,
                command=lambda: b_click(b2, 2, 1))
    b3 = Button(window, text=" ", bg="#ADD8E6", font=("Gilroy", 30), height=3, width=6,
                command=lambda: b_click(b3, 2, 2))
    b4 = Button(window, text=" ", bg="#0096FF", font=("Gilroy", 30), height=3, width=6,
                command=lambda: b_click(b4, 1, 0))
    b5 = Button(window, text=" ", bg="#0096FF", font=("Gilroy", 30), height=3, width=6,
                command=lambda: b_click(b5, 1, 1))
    b6 = Button(window, text=" ", bg="#0096FF", font=("Gilroy", 30), height=3, width=6,
                command=lambda: b_click(b6, 1, 2))
    b7 = Button(window, text=" ", bg="#0000FF", font=("Gilroy", 30), height=3, width=6,
                command=lambda: b_click(b7, 0, 0))
    b8 = Button(window, text=" ", bg="#0000FF", font=("Gilroy", 30), height=3, width=6,
                command=lambda: b_click(b8, 0, 1))
    b9 = Button(window, text=" ", bg="#0000FF", font=("Gilroy", 30), height=3, width=6,
                command=lambda: b_click(b9, 0, 2))
    btn = Button(window, text="RESET", font=("Consolas", 15),bg="#F0FFFF", height=2, width=6, command=lambda: play())
    exit = Button(window, text="EXIT", font=("Consolas", 15),bg="#F0FFFF", height=2, width=6, command=window.destroy)

    messagebox.showinfo("Starts", "X Starts First!")

    # disable_buttons
    def disable_buttons():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)

    # grid buttons
    b7.grid(row=0, column=0)
    b8.grid(row=0, column=1)
    b9.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b1.grid(row=2, column=0)
    b2.grid(row=2, column=1)
    b3.grid(row=2, column=2)
    btn.grid(row=3, column=0)
    exit.grid(row=3, column=2)

    # winning conditions
    def winner():
        if b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':  # 1 5 9
            messagebox.showinfo("WIN", "X WINS!")
            play.flag = 1
            disable_buttons()
        elif b7['text'] == 'X' and b5['text'] == 'X' and b3['text'] == 'X':  # 7 5 3
            messagebox.showinfo("WIN", "X WINS!")
            play.flag = 1
            disable_buttons()
        elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':  # 7 8 9
            messagebox.showinfo("WIN", "X WINS!")
            play.flag = 1
            disable_buttons()
        elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':  # 4 5 6
            messagebox.showinfo("WIN", "X WINS!")
            play.flag = 1
            disable_buttons()
        elif b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':  # 1 2 3
            messagebox.showinfo("WIN", "X WINS!")
            play.flag = 1
            disable_buttons()
        elif b7['text'] == 'X' and b4['text'] == 'X' and b1['text'] == 'X':  # 7 4 1
            messagebox.showinfo("WIN", "X WINS!")
            play.flag = 1
            disable_buttons()
        elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':  # 2 5 8
            messagebox.showinfo("WIN", "X WINS!")
            play.flag = 1
            disable_buttons()
        elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':  # 3 6 9
            messagebox.showinfo("WIN", "X WINS!")
            play.flag = 1
            disable_buttons()
        elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':  # 1 5 9
            messagebox.showinfo("WIN", "O WINS!")
            play.flag = 1
            disable_buttons()
        elif b7['text'] == 'O' and b5['text'] == 'O' and b3['text'] == 'O':  # 7 5 3
            messagebox.showinfo("WIN", "O WINS!")
            play.flag = 1
            disable_buttons()
        elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':  # 7 8 9
            messagebox.showinfo("WIN", "O WINS!")
            play.flag = 1
            disable_buttons()
        elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':  # 4 5 6
            messagebox.showinfo("WIN", "O WINS!")
            play.flag = 1
            disable_buttons()
        elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':  # 1 2 3
            messagebox.showinfo("WIN", "O WINS!")
            play.flag = 1
            disable_buttons()
        elif b7['text'] == 'O' and b4['text'] == 'O' and b1['text'] == 'O':  # 7 4 1
            messagebox.showinfo("WIN", "O WINS!")
            play.flag = 1
            disable_buttons()
        elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':  # 2 5 8
            messagebox.showinfo("WIN", "O WINS!")
            play.flag = 1
            disable_buttons()
        elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':  # 3 6 9
            messagebox.showinfo("WIN", "O WINS!")
            play.flag = 1
            disable_buttons()

    # button clicked
    def b_click(b, r, c):
        labelphoto_b9, labelphoto_b8, labelphoto_b7, labelphoto_b6, labelphoto_b5, labelphoto_b4, labelphoto_b3, labelphoto_b2, labelphoto_b1 = images()
        if b["text"] == ' ' and play.clicked == 1:
            b['text'] = 'X'
            if r == 0 and c == 0:
                labelphoto_b7.config(image=play.X)
                labelphoto_b7.grid(row=r, column=c)
            elif r == 0 and c == 1:
                labelphoto_b8.config(image=play.X)
                labelphoto_b8.grid(row=r, column=c)
            elif r == 0 and c == 2:
                labelphoto_b9.config(image=play.X)
                labelphoto_b9.grid(row=r, column=c)
            elif r == 1 and c == 0:
                labelphoto_b4.config(image=play.X)
                labelphoto_b4.grid(row=r, column=c)
            elif r == 1 and c == 1:
                labelphoto_b5.config(image=play.X)
                labelphoto_b5.grid(row=r, column=c)
            elif r == 1 and c == 2:
                labelphoto_b6.config(image=play.X)
                labelphoto_b6.grid(row=r, column=c)
            elif r == 2 and c == 0:
                labelphoto_b1.config(image=play.X)
                labelphoto_b1.grid(row=r, column=c)
            elif r == 2 and c == 1:
                labelphoto_b2.config(image=play.X)
                labelphoto_b2.grid(row=r, column=c)
            elif r == 2 and c == 2:
                labelphoto_b3.config(image=play.X)
                labelphoto_b3.grid(row=r, column=c)

            play.clicked = 0
            play.count += 1
            winner()
        elif b['text'] == ' ' and play.clicked == 0:
            b['text'] = 'O'
            if r == 0 and c == 0:
                labelphoto_b7.config(image=play.O)
                labelphoto_b7.grid(row=r, column=c)
            elif r == 0 and c == 1:
                labelphoto_b8.config(image=play.O)
                labelphoto_b8.grid(row=r, column=c)
            elif r == 0 and c == 2:
                labelphoto_b9.config(image=play.O)
                labelphoto_b9.grid(row=r, column=c)
            elif r == 1 and c == 0:
                labelphoto_b4.config(image=play.O)
                labelphoto_b4.grid(row=r, column=c)
            elif r == 1 and c == 1:
                labelphoto_b5.config(image=play.O)
                labelphoto_b5.grid(row=r, column=c)
            elif r == 1 and c == 2:
                labelphoto_b6.config(image=play.O)
                labelphoto_b6.grid(row=r, column=c)
            elif r == 2 and c == 0:
                labelphoto_b1.config(image=play.O)
                labelphoto_b1.grid(row=r, column=c)
            elif r == 2 and c == 1:
                labelphoto_b2.config(image=play.O)
                labelphoto_b2.grid(row=r, column=c)
            elif r == 2 and c == 2:
                labelphoto_b3.config(image=play.O)
                labelphoto_b3.grid(row=r, column=c)
            play.clicked = 1
            play.count += 1
            winner()
        else:
            messagebox.showerror("Error", "Not Valid!")
        if play.count == 9 and play.flag == 0:
            messagebox.showinfo("WIN", "TIE!")
            disable_buttons()


play()

window.mainloop()
