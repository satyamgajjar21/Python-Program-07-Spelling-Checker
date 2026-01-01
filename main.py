from textblob import TextBlob
from tkinter import *
# obj = TextBlob("dataa")
# print(obj.correct())

#func when button is pressed
def correct_spelling():
    get_data = enter1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    enter2.delete(0, END)
    enter2.insert(0,data)

#main window
def main_window():
    global enter1, enter2
    win = Tk()
    win.geometry("500x400")
    win.resizable(False, False)
    win.config(bg="Black")
    win.title("Spelling Checker By Satyam")

    label1 = Label(win, text="Incorrect Spelling : ",font=("Arial", 15), bg= "black", fg="white" )
    label1.place(x=100, y=20, height=40, width=300)

    enter1 = Entry(win, font=("Arial",25))
    enter1.place(x=50, y= 80, height=40, width=400)

    label2 = Label(win, text="Correct Spelling : ",font=("Arial", 15), bg= "black", fg="white" )
    label2.place(x=100, y=140, height=40, width=300)

    enter2 = Entry(win, font=("Arial",25))
    enter2.place(x=50, y= 200, height=40, width=400)

    button = Button(win, text="Check", font=("Arial", 15), bg="black", command=correct_spelling)
    button.place(x=150 , y=260 , height=40, width=200)

    win.mainloop()

main_window()