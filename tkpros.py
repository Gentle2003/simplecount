from tkinter import *

root = Tk()
root.title("TKGAME")
#root.state("zoomed") uncomment this if you want your tkinter to be at zoomed state when you run the program
root.geometry('600x600')
r = 0


#Count Function
def count():
    global r
    r += 1
    print(r)
    Label(root , text=r, fg="red", bg="cyan", font=("Algeria", 63)).place(x=293, y=200)

#Add Button
btn1 = Button(text = "ADD", font = ("Times New Roman", 15), command = count).place(x = 290, y = 300)



root.mainloop()