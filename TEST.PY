from tkinter import *

def quit():
    window.destroy()

def clearall():
    canvas.delete(ALL)

def buttonclick(event):
    global calcvalue
    global savedvalue
    if event.x >10 and event.x <70 and event.y >50 and event.y <110 : pressed = "7" 
    if event.x >90 and event.x <150 and event.y >50 and event.y <110 : pressed = "8"
    if event.x >170 and event.x <230 and event.y >50 and event.y <110 : pressed = "9"
    if event.x >250 and event.x <310 and event.y >50 and event.y <110 : pressed = "/"
#Upper Middle Row
    if event.x >10 and event.x <70 and event.y >120 and event.y <180 : pressed = "4"
    if event.x >90 and event.x <150 and event.y >120 and event.y <180 : pressed = "5"
    if event.x >170 and event.x <230 and event.y >120 and event.y <180 : pressed = "6"
    if event.x >250 and event.x <310 and event.y >120 and event.y <180 : pressed = "*"
#Lower Middle Row
    if event.x >10 and event.x <70 and event.y >190 and event.y <250 : pressed = "1"
    if event.x >90 and event.x <150 and event.y >190 and event.y <250 : pressed = "2"
    if event.x >170 and event.x <230 and event.y >190 and event.y <250 : pressed = "3"
    if event.x >250 and event.x <310 and event.y >190 and event.y <250 : pressed = "-"
#Bottom Row
    if event.x >10 and event.x <70 and event.y >260 and event.y <320 : pressed = "0"
    if event.x >90 and event.x <150 and event.y >260 and event.y <320 : pressed = "="
    if event.x >170 and event.x <230 and event.y >260 and event.y <320 : pressed = "C"
    if event.x >250 and event.x <310 and event.y >260 and event.y <320 : pressed = "+"

    calcvalue=pressed
    displayupdate()
    canvas.update()


def displayupdate():
    canvas.create_rectangle(10,10,310,40, fill="white", outline="black")
    canvas.create_text(290,25, text=calcvalue,font="Times 20 bold",anchor=E)

def main():
    global window
    global tkinter
    global canvas
    window = Tk()
    window.title("Simple Calculator")
    Button(window, text="Quit", width=5, command=quit).pack()
    canvas = Canvas(window, width=320, height=340, bg = 'beige')
    canvas.bind("<Button-1>", buttonclick)

#Display
    global calcvalue
    canvas.create_rectangle(10,10,310,40, fill="white", outline="black")
    canvas.create_text(290,25, text="0",font="Times 20 bold")
    canvas.pack()


#Add the numbers
    #Top Row
    canvas.create_rectangle(10,50,70,110, fill="yellow", outline="black")
    canvas.create_text(40,80,text="7",font="Times 30 bold")

    canvas.create_rectangle(150,50,90,110, fill="yellow", outline="black")
    canvas.create_text(120,80,text="8",font="Times 30 bold")

    canvas.create_rectangle(230,50,170,110, fill="yellow", outline="black")
    canvas.create_text(200,80,text="9",font="Times 30 bold")

    canvas.create_rectangle(310,50,250,110, fill="powder blue", outline="black")
    canvas.create_text(280,80,text="/",font="Times 30 bold")

    #Upper Middle Row

    canvas.create_rectangle(10,180,70,120, fill="yellow", outline="black")
    canvas.create_text(40,150,text="4",font="Times 30 bold")

    canvas.create_rectangle(90,180,150,120, fill="yellow", outline="black")
    canvas.create_text(120,150,text="5",font="Times 30 bold")

    canvas.create_rectangle(170,180,230,120, fill="yellow", outline="black")
    canvas.create_text(200,150,text="6",font="Times 30 bold")

    canvas.create_rectangle(250,180,310,120, fill="powder blue", outline="black")
    canvas.create_text(280,150,text="*",font="Times 30 bold")

    #Lower Middle Row

    canvas.create_rectangle(10,250,70,190, fill="yellow", outline="black")
    canvas.create_text(40,220,text="1",font="Times 30 bold")

    canvas.create_rectangle(90,250,150,190, fill="yellow", outline="black")
    canvas.create_text(120,220,text="2",font="Times 30 bold")

    canvas.create_rectangle(170,250,230,190, fill="yellow", outline="black")
    canvas.create_text(200,220,text="3",font="Times 30 bold")

    canvas.create_rectangle(250,250,310,190, fill="powder blue", outline="black")
    canvas.create_text(280,220,text="-",font="Times 30 bold")

    #Bottom Row

    canvas.create_rectangle(10,320,70,260, fill="yellow", outline="black")
    canvas.create_text(40,290,text="0",font="Times 30 bold")

    canvas.create_rectangle(90,320,150,260, fill="darkgreen", outline="black")
    canvas.create_text(120,290,text="=",font="Times 30 bold")

    canvas.create_rectangle(170,320,230,260, fill="darkgreen", outline="black")
    canvas.create_text(200,290,text="C",font="Times 30 bold")

    canvas.create_rectangle(250,320,310,260, fill="powder blue", outline="black")
    canvas.create_text(280,290,text="+",font="Times 30 bold")



    canvas.pack()