import tkinter as tk
import math 
root=tk.Tk()
root.geometry("644x900")
root.maxsize(644,900)
root.minsize(644,900)
root.title("calculator app was made by jp gamer")
try:
    icon_image=tk.PhotoImage(file="OIP.png")
    root.iconphoto(True,icon_image)
except tk.TclError:
    pass
def _handle_click(event):
    global sevalue
    text=event.widget.cget("text")
    print(text)
# ab ham text jab == to ho to ham aab conditions lagate hai ab ham pehle if condition lagake cheack karte hai agar 
# sevalue int hai to value ko int sevalue karenge or else me value ko eval karte hai jo ki operations ko perform karta hai 
# or uske baad ham bahar sevalue ko set karenge value se or phir screen ko update karenge 
    if text=="=":
        if sevalue.get().isdigit():
            value=int(sevalue.get())
        else:
            value=eval(screen.get())
        sevalue.set(value)
        screen.update()
    elif text=="C":
        sevalue.set("")
        screen.update()
    elif text=="-+":
        if sevalue.get().startswith("-"):
            sevalue.set(sevalue.get()[1:])
        else:
            sevalue.set("-" + sevalue.get())
        sevalue.set(sevalue.get())
        screen.update()
    elif text=="on":
        sevalue.set("")
        screen.update()
    elif text=="<--":
        sevalue.set(sevalue.get()[:-1])
        screen.update()
    elif text=="√":
        sevalue.set(str(math.sqrt(float(sevalue.get()))))
        screen.update()
    elif text=="%":
        sevalue.set(str(float(sevalue.get()) / 100))
        screen.update()
    else:
        sevalue.set(sevalue.get()+text)
        screen.update()
def click(event):
    # galat expression (5/0, khali screen par = ...) par app crash nahi hoga
    try:
        if sevalue.get()=="Error":
            sevalue.set("")
        _handle_click(event)
    except Exception:
        sevalue.set("Error")
sevalue=tk.StringVar()
sevalue.set("")
screen=tk.Entry(root,textvariable=sevalue,font="lucida 40 bold")
screen.pack(fill=tk.X, ipadx=20, ipady=20)
frame1=tk.Frame(root,bg="grey")
# button=tk.Button(frame1,text="1",font="lucida 35 bold")
# button.pack()
frame1.pack(fill=tk.X, ipadx=20, ipady=20)
button1=tk.Button(frame1,text="1",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=25,pady=25,relief="sunken",bd=3)
button1.grid(row=3,column=0,pady=(180,0))
button1.bind("<Button-1>",click)
button2=tk.Button(frame1,text="2",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=25,pady=25,relief="sunken",bd=3)
button2.grid(row=3,column=1,pady=(180,0))
button2.bind("<Button-1>",click)
button3=tk.Button(frame1,text="3",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=25,pady=25,relief="sunken",bd=3)
button3.grid(row=3,column=2,pady=(180,0))
button3.bind("<Button-1>",click)
button4=tk.Button(frame1,text="4",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=25,pady=25,relief="sunken",bd=3)
button4.grid(row=4,column=0)
button4.bind("<Button-1>",click)
button5=tk.Button(frame1,text="5",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=25,pady=25,relief="sunken",bd=3)
button5.grid(row=4,column=1)
button5.bind("<Button-1>",click)    
button6=tk.Button(frame1,text="6",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=25,pady=25,relief="sunken",bd=3)
button6.grid(row=4,column=2)
button6.bind("<Button-1>",click)
button7=tk.Button(frame1,text="7",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=25,pady=25,relief="sunken",bd=3)
button7.grid(row=5,column=0)
button7.bind("<Button-1>",click)
button8=tk.Button(frame1,text="8",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=25,pady=25,relief="sunken",bd=3)
button8.grid(row=5,column=1)
button8.bind("<Button-1>",click)    
button9=tk.Button(frame1,text="9",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=25,pady=25,relief="sunken",bd=3)
button9.grid(row=5,column=2)
button9.bind("<Button-1>",click)
button00=tk.Button(frame1,text="00",font=("Arial",25),fg="black", borderwidth=4,bg="white",padx=20,pady=30,relief="sunken",bd=3)
button00.grid(row=6,column=0)
button00.bind("<Button-1>",click)
button0=tk.Button(frame1,text="0",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=25,pady=25,relief="sunken",bd=3)
button0.grid(row=6,column=1)
button0.bind("<Button-1>",click)    
buttondot=tk.Button(frame1,text=".",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=30,pady=25,relief="sunken",bd=3)
buttondot.grid(row=6,column=2)
buttondot.bind("<Button-1>",click)
buttonx=tk.Button(frame1,text="*",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=30,pady=25,relief="sunken",bd=3)
buttonx.grid(row=3,column=3,pady=(180,0))
buttonx.bind("<Button-1>",click)
button_equals=tk.Button(frame1,text="=",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=25,pady=25,relief="sunken",bd=3)
button_equals.grid(row=3,column=4,pady=(180,0))
button_equals.bind("<Button-1>",click)
button_plus=tk.Button(frame1,text="+",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=25,pady=25,relief="sunken",bd=3)
button_plus.grid(row=3,column=5,pady=(180,0))
button_plus.bind("<Button-1>",click)
button_minus=tk.Button(frame1,text="-",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=32,pady=25,relief="sunken",bd=3)
button_minus.grid(row=4,column=3)
button_minus.bind("<Button-1>",click)
button_divide=tk.Button(frame1,text="/",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=32,pady=25,relief="sunken",bd=3)
button_divide.grid(row=4,column=4)
button_divide.bind("<Button-1>",click)
button_clear=tk.Button(frame1,text="C",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=23,pady=25,relief="sunken",bd=3)
button_clear.grid(row=4,column=5)
button_clear.bind("<Button-1>",click)
button_backspace=tk.Button(frame1,text="<--",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=13,pady=25,relief="sunken",bd=3)
button_backspace.grid(row=5,column=3)
button_backspace.bind("<Button-1>",click)
button_percent=tk.Button(frame1,text="%",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=20,pady=25,relief="sunken",bd=3)
button_percent.grid(row=5,column=4)
button_percent.bind("<Button-1>",click)
button_sqrt=tk.Button(frame1,text="√",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=25,pady=25,relief="sunken",bd=3)
button_sqrt.grid(row=5,column=5)
button_sqrt.bind("<Button-1>",click)
button_power=tk.Button(frame1,text="^",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=28,pady=25,relief="sunken",bd=3,
command=lambda: sevalue.set(sevalue.get() + "**"))
button_power.grid(row=6,column=3)
button_power.bind("<Button-1>")
buttonplusminus=tk.Button(frame1,text="-+",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=20,pady=25,relief="sunken",bd=3)
buttonplusminus.grid(row=6,column=4)
buttonplusminus.bind("<Button-1>",click)
button0n=tk.Button(frame1,text="on",font=("Arial",30),fg="black", borderwidth=4,bg="white",padx=15,pady=25,relief="sunken",bd=3)
button0n.grid(row=6,column=5)
button0n.bind("<Button-1>",click)
root.mainloop()