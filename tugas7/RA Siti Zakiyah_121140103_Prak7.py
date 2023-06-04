from tkinter import *

window = Tk()
image1=PhotoImage(file="image1.png")
image2=PhotoImage(file="image2.png")
image3=PhotoImage(file="image3.png")
image4=PhotoImage(file="image4.png")
image5=PhotoImage(file="image5.png")
image6=PhotoImage(file="image6.png")

window.configure(bg="white")
window.geometry("1400x900")
window.title("Jawaban dari setiap keluhanmu")
    
def pushed1():
    gambar1 = Label(window, image=image1).pack()

def pushed2():
    gambar2 = Label(window, image=image2).pack()
    
def pushed3():
    gambar3 = Label(window, image=image3).pack()
    
def pushed4():
    gambar4 = Label(window, image=image4).pack()
    
def pushed5():
    gambar5 = Label(window, image=image5).pack()
    
def pushed6():
    gambar6 = Label(window, image=image6).pack()
    
#tombol
btn1 = Button(window, text = "aku cape", command = pushed1,  height = 1, width = 10, bg = "black", fg = "white", font = "Times 10", borderwidth = 10).pack()
btn2 = Button(window, text = "aku sedih", command = pushed2,  height = 1, width = 10, bg = "black", fg = "white", font = "Times 10", borderwidth = 10).pack()
btn3 = Button(window, text = "aku ga bisa", command = pushed3,  height = 1, width = 10, bg = "black", fg = "white", font = "Times 10", borderwidth = 10).pack()
btn4 = Button(window, text = "aku stress banget", command = pushed4,  height = 1, width = 10, bg = "black", fg = "white", font = "Times 10", borderwidth = 10).pack()
btn5 = Button(window, text = "aku ga sanggup", command = pushed5,  height = 1, width = 10, bg = "black", fg = "white", font = "Times 10", borderwidth = 10).pack()
btn6 = Button(window, text = "kayanya sia sia", command = pushed6,  height = 1, width = 10, bg = "black", fg = "white", font = "Times 10", borderwidth = 10).pack()

window.mainloop()

