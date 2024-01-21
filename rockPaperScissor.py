from tkinter import *
import random
play=Tk()
play.geometry('600x500')
play.title('Rock-Paper-Scissor')
play.configure(bg='lightblue')
choices={'0':'rock', '1':'paper', '3':'scissor'}

def player_rock():
    selected=choices[str(random.randint(0,2))]
    if selected=='rock':
        resultdata='Tie!'
    elif selected=='paper':
        resultdata='Computerwin..!'
    else:
        resultdata='Player Win..!'
    l1.config(text='rock')
    l2.config(text=selected)
    result.config(text=resultdata)
    disable_btn()
def player_paper():
    selected = choices[str(random.randint(0,2))]
    if selected == 'paper':
        resultdata = 'Tie!'
    elif selected == 'scissor':
        resultdata = 'Computerwin..!'
    else:
        resultdata = 'Player Win..!'
    l1.config(text='paper')
    l2.config(text=selected)
    result.config(text=resultdata)
    disable_btn()
def player_scissor():
    selected = choices[str(random.randint(0,2))]
    if selected == 'scissor':
        resultdata = 'Tie!'
    elif selected == 'rock':
        resultdata = 'Computerwin..!'
    else:
        resultdata = 'Player Win..!'
    l1.config(text='scissor')
    l2.config(text=selected)
    result.config(text=resultdata)
    disable_btn()

def disable_btn():
    b1['state']='disable'
    b2['state'] = 'disable'
    b3['state'] = 'disable'
def reset():
    b1['state'] = 'active'
    b2['state'] = 'active'
    b3['state'] = 'active'
    l1.config(text=' ')
    l2.config(text=' ')
    result.config(text=' ')
Label(play, text='Rock-Paper-Scissor', font=('calibri', 20)).place(x=160, y=20)
Label(play, text='Player Selected', font=('calibri', 18)).place(x=30, y=80)

l1=Label(play, font=('calibri', 20), bg='green', fg='white')
l1.place(x=100, y=130)

Label(play, text='Computer Selected', font=('calibri', 18)).place(x=330, y=80)

l2=Label(play, font=('calibri', 20), bg='green', fg='white')
l2.place(x=400, y=130)

Label(play, text='Choose any one', font=('calibri', 15), bg='blue', fg='white').place(x=180, y=210)
b1=Button(play, text='Rock', command=player_rock, font=('calibri', 15), width='10', height='1', bg='gray', fg='white')
b1.place(x=60, y=270)

b2=Button(play, text='Paper', command=player_paper, font=('calibri', 15), width='10', height='1', bg='gray', fg='white')
b2.place(x=230, y=270)

b3=Button(play, text='Scissor', command=player_scissor, font=('calibri', 15), width='10', height='1', bg='gray', fg='white')
b3.place(x=400, y=270)

result=Label(play, text=' ', font=('calibri', 25), bg='orange', fg='white', relief='solid')
result.place(x=200, y=350)

Button(play, text='Reset Game', command=reset, font=('calibri', 15), width='10', height='1', bg='gray',fg='white').place(x=450, y=400)
play.mainloop()