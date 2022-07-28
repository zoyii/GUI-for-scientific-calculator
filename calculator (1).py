from tkinter import *
import tkinter.messagebox
import math
root = Tk()
root.geometry("650x400+300+300")
root.title("Scientific Calculator")

# Button on press


def btn1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')

def btn2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')

def btn3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def btn4_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')

def btn5_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')

def btn6_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')

def btn7_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')

def btn8_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')

def btn9_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')

def btn0_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')

def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)

def btnp_clicked():
    pos = len(disp.get())
    disp.insert(pos, '+')

def btnm_clicked():
    pos = len(disp.get())
    disp.insert(pos, '-')

def btnml_clicked():
    pos = len(disp.get())
    disp.insert(pos, '*')

def btnd_clicked():
    pos = len(disp.get())
    disp.insert(pos, '/')

def btnc_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '0')

def sin_clicked():
     if:
        ans = float(disp.get())
        ans = math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    else:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def cos_clicked():
    try:
        ans = float(disp.get())
        ans = math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")



def tan_clicked():
    try:
        ans = float(disp.get())
        ans = math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def arcsin_clicked():
    try:
        ans = float(disp.get())
        ans = math.asin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def arccos_clicked():
    try:
        ans = float(disp.get())
        ans = math.acos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def arctan_clicked():
    try:
        ans = float(disp.get())
        ans = math.atan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def pow_clicked():
    pos = len(disp.get())
    disp.insert(pos, '**')

def round_clicked():
    try:
        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def logarithm_clicked():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def fact_clicked():
    try:
        ans = float(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def sqr_clicked():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def dot_clicked():
    pos = len(disp.get())
    disp.insert(pos, '.')

def pi_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))


def e_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))

def bl_clicked():
    pos = len(disp.get())
    disp.insert(pos, '(')

def br_clicked():
    pos = len(disp.get())
    disp.insert(pos, ')')

def del_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])


def sign_clicked():
    try:
        ans = float(disp.get())
        ans = ans*-1
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def ln_clicked():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def square_clicked():
    try:
        ans = float(disp.get())
        ans = ans*ans
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

def btneq_clicked(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)

    except:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

# Label

disp = Entry(root, font="Verdana 20", justify=RIGHT,cursor="arrow")
disp.bind("<Return>", btneq_clicked)
disp.bind("<Escape>", btnc_clicked)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.bind("<Key-.>", key_event)
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH)


# Row 1 Buttons
btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=TRUE, fill=BOTH)

pi_btn = Button(btnrow1, text="π",font="Segoe 18",command=pi_clicked)
pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

fact_btn = Button(btnrow1, text=" x! ", font="Segoe 18",command=fact_clicked)
fact_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sin_btn = Button(btnrow1, text="sin", font="Segoe 18",  command=sin_clicked)
sin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cos_btn = Button(btnrow1, text="cos", font="Segoe 18",  command=cos_clicked)
cos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tan_btn = Button(btnrow1, text="tan", font="Segoe 18",  command=tan_clicked)
tan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn1 = Button(btnrow1, text="1", font="Segoe 23",  command=btn1_clicked)
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow1, text="2", font="Segoe 23", command=btn2_clicked)
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow1, text="3", font="Segoe 23", command=btn3_clicked)
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnp = Button(btnrow1, text="+", font="Segoe 23",  command=btnp_clicked)
btnp.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 2 Buttons

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)

e_btn = Button(btnrow2, text="e", font="Segoe 18 ",command=e_clicked)
e_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sqr_btn = Button(btnrow2, text=" √x ", font="Segoe 18 ",command=sqr_clicked)
sqr_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sinh_btn = Button(btnrow2, text="sin−1", font="Segoe 11 bold", command=arcsin_clicked)
sinh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cosh_btn = Button(btnrow2, text="cos-1", font="Segoe 11 bold", command=arccos_clicked)
cosh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tanh_btn = Button(btnrow2, text="tan-1", font="Segoe 11 bold", command=arctan_clicked)
tanh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4 = Button(btnrow2, text="4", font="Segoe 23", command=btn4_clicked)
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow2, text="5", font="Segoe 23",command=btn5_clicked)
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(btnrow2, text="6", font="Segoe 23",command=btn6_clicked)
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnm = Button(btnrow2, text="-", font="Segoe 23",command=btnm_clicked)
btnm.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 3 Buttons

btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

sign_btn = Button(btnrow3, text="+/-", font="Segoe 12 bold",command=sign_clicked)
sign_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

round_btn = Button(btnrow3, text="Round", font="Segoe 12 ",command=round_clicked)
round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

ln_btn = Button(btnrow3, text="ln", font="Segoe 18", command=ln_clicked)
ln_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

logarithm_btn = Button(btnrow3, text="log", font="Segoe 17",command=logarithm_clicked)
logarithm_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

pow_btn = Button(btnrow3, text="x^y", font="Segoe 17", command=pow_clicked)
pow_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn7 = Button(btnrow3, text="7", font="Segoe 23",command=btn7_clicked)
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow3, text="8", font="Segoe 23",command=btn8_clicked)
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow3, text="9", font="Segoe 23", command=btn9_clicked)
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnml = Button(btnrow3, text="*", font="Segoe 23", command=btnml_clicked)
btnml.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 4 Buttons

btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

square_btn = Button(btnrow4, text="x^2", font="Segoe 12 bold",command=square_clicked)
square_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

bl_btn = Button(btnrow4, text=" ( ", font="Segoe 21",command=bl_clicked)
bl_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

br_btn = Button(btnrow4, text=" ) ", font="Segoe 21", command=br_clicked)
br_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

dot_btn = Button(btnrow4, text=" • ", font="Segoe 21",command=dot_clicked)
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnc = Button(btnrow4, text="C", font="Segoe 23", command=btnc_clicked)
btnc.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow4, text="⌫", font="Segoe 16",command=del_clicked)
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Segoe 23", command=btn0_clicked)
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneq = Button(btnrow4, text="=", font="Segoe 23", command=btneq_clicked)
btneq.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnd = Button(btnrow4, text="/", font="Segoe 23", command=btnd_clicked)
btnd.pack(side=LEFT, expand=TRUE, fill=BOTH)

root.mainloop()
