# importing tkinter
from tkinter import*

# Creating a window
window = Tk()

# window dimensions
window.geometry("320x360")

# setting the title to calculator
window.title("PEMDAS Calculator")
# setting the background color to be purple
window.config(background='purple')

# creating a variable to store the number in the btns for it to be inserted to the screen (this also changes when another button is clicked)
button1 = ''
# stores when numbers is clicked
number = 0
# stores when symbols is clicked
symbol = 0
# creating a variable to store the symbols in the btns for it to be inserted to the screen (this also changes when another button is clicked)
symbols = ''

# creating a list of all the text in a keyboard. ( youll see why later on )
letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
           'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',
           ',','.',"'",'"','?','<','>','|','[',']','{','}',';',':','=',')','(','`','~','!','@','#','$','%','^','&',
           '*','|','1','2','3','4','5','6','7','8','9','0','*','+','-','_','/',"\\"]

# a function to get the text of the buttons that is clicked, adds one to number when clicked, resets symbol and if number is 1 delete anything thst was in the screen before
def num(btn):
    global button1
    global number
    global symbol
    button1 = int(btn['text'])
    number += 1
    symbol = 0
    if number == 1:
        entry.delete(0,END)


# a function to make sure that the symbol can only be shown ones by deleting any symbol that comes after it
def idk():
    global symbol
    global number
    if symbol >= 2 and number != (number + 1):
        entry.delete(len(entry.get()) - 3, END)

# a function to get the text of the symbol that is clicked, and to make sure that symbol cant show up on screen if the number is not clicked
def sym(btn):
    global symbols
    global symbol
    global number
    if number != 0:
        symbols = btn['text']
        symbol += 1
    idk()

# a function to add zero to the entry box (just because)
def start():
    entry.insert(END,0)
    



# inserts button1 and symbols to screen when clicked
def calc():
    entry.insert(END,button1)
def calc2():
    entry.insert(END,symbols)



# a fumction to evaluate all units in the entry box and also passing the idk  function (the one that deletes any symbol after one symbol is already on screen) in it
# this also checks for any syntax error (e.g presses the equals to button with only 1+) and inserts ERROR on screen
def equal():
    try:
        global number
        global symbol
        value = entry.get()
        equal_to = eval(value)
        entry.delete(0,END)
        entry.insert(0,equal_to)
        idk()
    except SyntaxError:
        entry.delete(0,END)
        entry.insert(END,'ERROR')
        



# deletes everything and sets number to zero again
def ace():
    global number
    
    entry.delete(0,END)
    entry.insert(END,'0')
    number = 0
    
    idk()

# deletes anytime the list of all text in keyboard is shown on screen 
def nolet(event):
    if entry.get() and entry.get()[-1] in letters:
        entry.delete(len(entry.get()) - 1, END)
        

# Creating an entry that displays what button the user presses
entry = Entry(window,font=('Arial',50),bd=5,bg='pink',disabledbackground='pink',disabledforeground='black', width=8)
entry.pack(side='top')
# binds the keys to nolet so the nolet only applies when a key is pressed
entry.bind('<KeyRelease>',nolet)
start()


# optional scroll bar?
"""
entryScroll = Scrollbar( orient=HORIZONTAL,activebackground='purple',)
entryScroll.pack(side='top')

entry['xscrollcommand'] = entryScroll.set
entryScroll['command'] = entry.xview
"""

# Creating all the buttons needed and putting it in a frame

# The frame
frame = Frame(window,bd=5,bg='purple')
frame.pack(side='top')

# Creating the buttons and adding their respective settings and commands
# they are also a grid format
one = Button(frame,text=' 1 ',font=("Consolas",25),width=3,padx=8,pady=1,bg='pink',activebackground='pink',command=lambda: [num(one), calc()])
one.grid(row=0,column=0)


two = Button(frame,text=' 2 ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink',command=lambda: [num(two), calc()])
two.grid(row=0,column=1)


three = Button(frame,text=' 3 ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink',command=lambda: [num(three), calc()])
three.grid(row=0,column=2)


plus = Button(frame,text=' + ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink',command=lambda: [sym(plus), calc2()])
plus.grid(row=0,column=3)


four = Button(frame,text=' 4 ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink',command=lambda: [num(four), calc()])
four.grid(row=1,column=0)


five = Button(frame,text=' 5 ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink',command=lambda: [num(five), calc()])
five.grid(row=1,column=1)


six = Button(frame,text=' 6 ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink',command=lambda: [num(six), calc()])
six.grid(row=1,column=2)


minus = Button(frame,text=' - ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink',command=lambda: [sym(minus), calc2()])
minus.grid(row=1,column=3)


seven = Button(frame,text=' 7 ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink',command=lambda: [num(seven), calc()])
seven.grid(row=2,column=0)


eight = Button(frame,text=' 8 ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink',command=lambda: [num(eight), calc()])
eight.grid(row=2,column=1)


nine = Button(frame,text=' 9 ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink',command=lambda: [num(nine), calc()])
nine.grid(row=2,column=2)


times = Button(frame,text=' * ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink',command=lambda: [sym(times), calc2()])
times.grid(row=2,column=3)


acee = Button(frame,text=' ac ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink',command=ace)
acee.grid(row=3,column=0)

zero = Button(frame,text=' 0 ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink',command=lambda: [num(zero), calc()])
zero.grid(row=3,column=1)


divide = Button(frame,text=' / ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink',command=lambda: [sym(divide), calc2()])
divide.grid(row=3,column=3)

equals = Button(frame,text=' = ',font=("Consolas",25),width=3,padx=8,bg='pink',activebackground='pink', command = equal)
equals.grid(row=3,column=2)

# displaying window
window.mainloop()