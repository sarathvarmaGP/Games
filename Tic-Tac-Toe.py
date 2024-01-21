import tkinter.messagebox
from tkinter import *
play = Tk()
play.geometry('400x400')
play.title('Tic-Tac-Toe')
play.configure(bg='lightblue')

def btnclick(buttons):
    global playerA, playerB, bclick, turns
    if buttons['text'] == ' ' and bclick == True:
        buttons['text']='X'
        bclick=False
        turns +=1
        possibilities()
    elif buttons['text'] == ' ' and bclick ==False:
        buttons['text'] = 'O'
        bclick = True
        turns += 1
        possibilities()
    else:
        tkinter.messagebox.showwarning('Tic-Tac-Toe', 'Button already Clicked')
def possibilities():
    if(b1['text']=='X' and b2['text']=='X' and b3['text']=='X' or
            b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or
            b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X' or
            b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or
            b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or
            b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X' or
            b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or
            b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X'):
        tkinter.messagebox.showinfo('Tic-Tac-Toe', p1.get()+'Wins..!!!')
    elif(b1['text']=='O' and b2['text']=='O' and b3['text']=='O' or
            b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or
            b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or
            b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or
            b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' or
            b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O' or
            b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or
            b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O'):
        tkinter.messagebox.showinfo('Tic-Tac-Toe', p2.get() + 'Wins..!!!')
    elif turns==10:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Match Draw')
Label(play, text='Tic-Tac-Toe', font=('calibri', 25)).place(x=200, y=20)
Label(play, text='Enter Player 1 Name: ', font=('calibri', 15), bg='lightblue').place(x=50, y=80)
Label(play, text='Enter Player 2 Name: ', font=('calibri', 15), bg='lightblue').place(x=50, y=130)
playerA=StringVar()
playerB=StringVar()
p1=StringVar()
p2=StringVar()
buttons=StringVar()
bclick= True
turns= 1
Entry(play, textvariable=p1, font=('calibri', 15)).place(x=300, y=80)
Entry(play, textvariable=p2, font=('calibri', 15)).place(x=300, y=130)
b1=Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='7', command=lambda:btnclick(b1))
b1.place(x=100, y=200)
b2=Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='7', command=lambda:btnclick(b2))
b2.place(x=215, y=200)
b3=Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='7', command=lambda:btnclick(b3))
b3.place(x=330, y=200)
b4=Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='7', command=lambda:btnclick(b4))
b4.place(x=100, y=300)
b5=Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='7', command=lambda:btnclick(b5))
b5.place(x=215, y=300)
b6=Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='7', command=lambda:btnclick(b6))
b6.place(x=330, y=300)
b7=Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='7', command=lambda:btnclick(b7))
b7.place(x=100, y=400)
b8=Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='7', command=lambda:btnclick(b8))
b8.place(x=215, y=400)
b9=Button(play, text=' ', font=('calibri', 20, 'bold'), bg='gray', fg='white', width='7', command=lambda:btnclick(b9))
b9.place(x=330, y=400)

play.mainloop()