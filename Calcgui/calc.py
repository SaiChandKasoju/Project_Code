from tkinter import *

root = Tk()

root.title("Chandu's_Calculator")
root.configure(background="blue")

e=Entry(root, width=50, borderwidth=1)


def clicked(num):
    c=e.get()
    e.delete(0, END)
    global x
    x=str(c)+str(num)
    e.insert(0, x)

def calc():
    if "+" in x:
        m=x.split("+")
        t=0
        for i in m:
            t+=int(i)
    if "-" in x:
        m=x.split("-")
        t=int(m[0])
        m=m[1:]
        for i in m:
            t-=int(i)
    if "/" in x:
        m=x.split("/")
        t=int(m[0])/int(m[1])
    if "*" in x:
        m=x.split("*")
        t=1
        for i in m:
            t*=int(i)
    e.delete(0, END)
    e.insert(0, t)

def cl():
    e.delete(0, END)


button_1=Button(root, text="9", padx=40, pady=20, command=lambda: clicked("9"))
button_2=Button(root, text="8", padx=40, pady=20, command=lambda: clicked("8"))
button_3=Button(root, text="7", padx=42, pady=20, command=lambda: clicked("7"))
button_4=Button(root, text="6", padx=40, pady=20, command=lambda: clicked("6"))
button_5=Button(root, text="5", padx=40, pady=20, command=lambda: clicked("5"))
button_6=Button(root, text="4", padx=42, pady=20, command=lambda: clicked("4"))
button_7=Button(root, text="3", padx=40, pady=20, command=lambda: clicked("3"))
button_8=Button(root, text="2", padx=40, pady=20, command=lambda: clicked("2"))
button_9=Button(root, text="1", padx=42, pady=20, command=lambda: clicked("1"))
button_0=Button(root, text="0", padx=40, pady=20, command=lambda: clicked("0"))
button_add=Button(root, text="+", padx=38, pady=20, command=lambda: clicked("+"))
button_sub=Button(root, text="-", padx=40, pady=20, command=lambda: clicked("-"))
button_mul=Button(root, text="*", padx=40, pady=20, command=lambda: clicked("*"))
button_div=Button(root, text="/", padx=42, pady=20, command=lambda: clicked("/"))
button_equals=Button(root, text="=", padx=39, pady=20, command=calc)
button_clear=Button(root, text="Clear", padx=29, pady=20, command=cl)



e.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_equals.grid(row=4, column=1)
button_div.grid(row=4, column=2)
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_clear.grid(row=4, column=3)





root.mainloop()