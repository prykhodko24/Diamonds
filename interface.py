import tkinter as tk
from tkinter import ttk
from learning import a
from learning import lasso

def counting(lasso,X_test):
    Y_pred = abs(lasso.predict(X_test))
    return str(Y_pred[0])

def x_test(carat_v,cut_v,color_v,clarity_v):
    a['G'] = 0
    a['Ideal'] = 0
    a['VVS1'] = 0
    a['carat']=carat_v

    b=a.copy(deep=True)
    b[cut_v]=1
    b[color_v]=1
    b[clarity_v]=1

    return b

def show():

    cut_v=cut.get()
    color_v=color.get()
    clarity_v=clarity.get()
    carat_v=float(carat.get())
    x=x_test(carat_v, cut_v, color_v, clarity_v)
    ans=counting(lasso, x)
    pohybka=1-0.8#r2_res
    tk.Label(win, text="Приблизна ціна:",bg='#BCCEFF',fg='black').grid(row=6,column=0)


    txt=str(round((float(ans)*(1-pohybka)),0))+'$ -'+str(round((float(ans)*(1+pohybka)),0))+"$"

    tk.Label(win, text=txt,bg='#BCCEFF',fg='black', width=20).grid(row=6,column=1)
    print(txt)

carats=[]
i=0.2
while i<=5:
    carats.append(round(i,2))
    i=i+0.01

win=tk.Tk()
win.config(bg='#BCCEFF')
log=tk.PhotoImage(file='photo.png')
win.iconphoto(False,log)
win.geometry("500x190+200+100")  # size,center
win.resizable(False, False)  # can't cange size(vert, horiz)

win.title('Ціна діаманту')
tk.Label(win, text='', bg='#BCCEFF', fg='black').grid(row=0,column=0)
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "white", background= "white")


tk.Label(win, text=" Якість зрізу", bg='#BCCEFF', fg='black').grid(row=1, column=0)
cuts=['Fair','Good', 'Very Good', 'Premium', 'Ideal']
cut=ttk.Combobox(win,values=cuts,state='readonly')
cut.current(1)
cut.grid(row=1, column=1)

tk.Label(win, text="Колір діаманту", bg='#BCCEFF', fg='black').grid(row=2, column=0)
colors=['D','E', 'F', 'G', 'H','I','J']
color=ttk.Combobox(win,values=colors,state='readonly')
color.current(0)
color.grid(row=2, column=1)

tk.Label(win, text="Прозорість діаманту", bg='#BCCEFF', fg='black').grid(row=3, column=0)
claritys=['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
clarity=ttk.Combobox(win,values=claritys,state='readonly')
clarity.current(0)
clarity.grid(row=3, column=1)

tk.Label(win, text="Розмір діаманту", bg='#BCCEFF', fg='black').grid(row=4, column=0)
carat=ttk.Combobox(win,values=carats,state='readonly')
carat.current(0)
carat.grid(row=4, column=1)

ttk.Button(win,text='Result',command=show).grid(row=5, column=1)

win.grid_columnconfigure(0,minsize=100)
win.grid_columnconfigure(1,minsize=100)
win.mainloop()