from tkinter import *
import random
# R HARSHA
root = Tk()
root.title('PYTHON GUI')
p=0
q=0
def window1():
    # 1- rock
    # 2- paper
    # 3- scissor
    def clear():
        global p
        global q
        p=0
        q=0
        gui.destroy()
    def win():
        global p
        p=p+1
        Label(gui,font=("times", 20, "bold"),bg="#9979e2",width = 4,text=p).place(x=350, y=400)
    def lost():
        global q
        q=q+1
        Label(gui,font=("times", 20, "bold"),bg="#9979e2",width = 4,text=q).place(x=535, y=400)

    def rock():
        randomv="123"
        computer_choice=random.choice(randomv)
        if computer_choice == '1':
            Label(gui,font=("times", 20, "bold"),bg="#715656",width = 7,text="Rock").place(x=300,y=180)
            Label(gui,font=("times", 20, "bold"),bg="#715656",width = 7,text="Rock").place(x=565,y=180)
            Label(gui,font=("times", 20, "bold"),bg="cyan",width = 10,text="Tie :|").place(x=400,y=260)
        if computer_choice == '2':
            Label(gui,font=("times",20, "bold"),bg="#715656",width = 7,text="Rock").place(x=300,y=180)
            Label(gui,font=("times", 20, "bold"),bg="#ddd5d5",width = 7,text="Paper").place(x=565,y=180)
            Label(gui,font=("times", 20, "bold"),bg="#ff0000",width = 10,text="You Lost :(").place(x=400,y=260)
            lost()
        if computer_choice == '3':
            Label(gui,font=("times", 20, "bold"),bg="#715656",width = 7,text="Rock").place(x=300, y=180)
            Label(gui,font=("times", 20, "bold"),bg="#c67cd0",width = 7,text="Scissor").place(x=565, y=180)
            Label(gui,font=("times", 20, "bold"),bg="#18f78f",width = 10,text="You Win :)").place(x=400, y=260)
            win()

    def paper():
        randomv="123"
        computer_choice=random.choice(randomv)
        if computer_choice == '1':
            Label(gui,font=("times", 20, "bold"),bg="#ddd5d5",width = 7,text="Paper").place(x=300, y=180)
            Label(gui,font=("times", 20, "bold"),bg="#715656",width = 7,text="Rock").place(x=565, y=180)
            Label(gui,font=("times", 20, "bold"),bg="#18f78f",width = 10,text="You Win :)").place(x=400, y=260)
            win()
        if computer_choice == '2':
            Label(gui,font=("times", 20, "bold"),bg="#ddd5d5",width = 7,text="Paper").place(x=300, y=180)
            Label(gui,font=("times", 20, "bold"),bg="#ddd5d5",width = 7,text="Paper").place(x=565, y=180)
            Label(gui,font=("times", 20, "bold"),bg="cyan",width = 10,text="Tie :|").place(x=400, y=260)
        if computer_choice == '3':
            Label(gui,font=("times", 20, "bold"),bg="#ddd5d5",width = 7,text="Paper").place(x=300, y=180)
            Label(gui,font=("times", 20, "bold"),bg="#c67cd0",width = 7,text="Scissor").place(x=565, y=180)
            Label(gui,font=("times", 20, "bold"),bg="#ff0000",width = 10,text="You Lost :(").place(x=400, y=260)
            lost()
        
    def scissor():
        randomv="123"
        computer_choice=random.choice(randomv)
        if computer_choice == '1':
            Label(gui,font=("times", 20, "bold"),bg="#c67cd0",width = 7,text="Scissor").place(x=300, y=180)
            Label(gui,font=("times", 20, "bold"),bg="#715656",width = 7,text="Rock").place(x=565, y=180)
            Label(gui,font=("times", 20, "bold"),bg="#ff0000",width = 10,text="You Lost :(").place(x=400, y=260)
            lost()
        if computer_choice == '2':
            Label(gui,font=("times", 20, "bold"),bg="#c67cd0",width = 7,text="Scissor").place(x=300, y=180)
            Label(gui,font=("times", 20, "bold"),bg="#ddd5d5",width = 7,text="Paper").place(x=565, y=180)
            Label(gui,font=("times", 20, "bold"),bg="#18f78f",width = 10,text="You Win :)").place(x=400, y=260)
            win()
        if computer_choice == '3':
            Label(gui,font=("times", 20, "bold"),bg="#c67cd0",width = 7,text="Scissor").place(x=300, y=180)
            Label(gui,font=("times", 20, "bold"),bg="#c67cd0",width = 7,text="Scissor").place(x=565, y=180)
            Label(gui,font=("times", 20, "bold"),bg="cyan",width = 10,text="Tie :|").place(x=400, y=260)

    gui = Toplevel(root)
    gui.title("ROCK PAPER SCISSOR GAME")
    gui.geometry("950x700")
    message ='ROCK PAPER SCISSOR GAME'
    head = Message(gui,bg='#6680ff',font=("Castellar", 22, "bold"),text = message,width=700)
    head.place(x=250, y=0)
    rock_button=Button(gui,font=("times", 15, "bold"),activebackground="#fffa66",activeforeground="red",text="ROCK", command=rock).place(x=342, y=60)
    paper_button=Button(gui, font=("times", 15, "bold"),activebackground="#fffa66",activeforeground="red",text="PAPER", command=paper).place(x=442, y=60)
    scissor_button=Button(gui, font=("times", 15, "bold"),activebackground="#fffa66",activeforeground="red",text="SCISSOR", command=scissor).place(x=542, y=60)
    Exit_button=Button(gui, text="Exit Window",bg="#525047",fg="#e5e8ff",font=("times", 15, "bold"), command=clear).place(x=415, y=500)
    a=Label(gui,font=("times", 20, "bold"),text="Your choice").place(x=280, y=120)
    b=Label(gui,font=("times", 20, "bold"),text="Computer choice").place(x=525, y=120)
    c=Label(gui,font=("times", 20, "bold"),text="VS").place(x=470, y=180)
    c=Label(gui,font=("times", 20, "bold"),text="Your Score").place(x=310, y=350)
    c=Label(gui,font=("times", 20, "bold"),text="Computer Score").place(x=480, y=350)
    gui.resizable(False, False)
    gui.mainloop()

def window2():
    def main():
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(){[}]?.<>!@#$%^&*(){[}]?.<>"
        password = ""
        num=v.get()
        if var.get() == 0:
            for i in range(0, num):
                password = password + random.choice(lower)
        elif var.get() == 1:
            for i in range(0, num):
                password = password + random.choice(upper)
        elif var.get() == 2:
            for i in range(0, num):
                password = password + random.choice(digits)
        w = Label(gui,font=("times", 25, "bold"),width = 25,text=password).place(x=220, y=330)
        

    gui = Toplevel(root)     

    gui.title("Password Generator")
    gui.geometry("950x600")
    message ='PASSWORD GENERATOR'
    head = Message(gui,bg='#be62d0',font=("lucida calligraphy", 25, "bold"), text = message,width=4000)
    head.pack()
    var = IntVar()
    radio_weak = Radiobutton(gui, text="Weak",font=("times", 20),activeforeground="#3cddbc", variable=var, value=0).pack()
    radio_middle = Radiobutton(gui, text="Medium",font=("times", 20),activeforeground="#3cddbc", variable=var, value=1).pack()
    radio_strong = Radiobutton(gui, text="Strong",font=("times", 20),activeforeground="#3cddbc", variable=var, value=2).pack()
    v = IntVar()  
    scale = Scale(gui,font=("times", 25), variable=v,from_=5, to_=13,cursor="dot",length=300,width=20,troughcolor="#5cff7c",orient=HORIZONTAL)  
    scale.pack()
    Generate_button = Button(gui,font=("Engravers mt", 15 ),activebackground="#fffa66",activeforeground="red", text="Genetate Password", command=main).place(x=310,y=280)
    Exit_button=Button(gui,font=("calibre", 20 ),activebackground="#fffa66",activeforeground="red", text="Exit Window", command=gui.destroy).place(x=380,y=400)
    gui.resizable(False, False)
    gui.mainloop()

root.geometry("850x500")
root.configure(bg='#4778eb')
Label(root,font=("Jokerman",45),bg="#759af0",text="PYTHON  GUI  PROJECT").pack()
k=Button(root,font=("algerian",25 ),activebackground="#fffa66",activeforeground="red",text ="Rock Paper Scissor",command = window1).place(x=270,y=120)
j=Button(root,font=("algerian",25 ),activebackground="#fffa66",activeforeground="red",text ="Password Generator",command = window2).place(x=250,y=200)
Label(root,font=("Ink Free",35),bg="#4778eb",fg="#6ce0bd",text="R HARSHA").place(x=550,y=350)
root.resizable(False, False)
root.mainloop()