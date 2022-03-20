
from tkinter import (Tk, LabelFrame, Entry, Label, END)

root = Tk()
root.title("Binary-Decimal Calculator")
# to use an icon uncomment the following line and include a path
# root.iconbitmap('path/icone.ico')
root.geometry("505x110+15+60")


def calculator_B_D(base,numero):#base = 2, from binary
    # numero = str(numero)  
    lista_numero=[]
    for i in range(len(numero)):
        lista_numero.append(int(numero[i]))
    dec=0
    for i in range(len(lista_numero)):
        a = lista_numero[-1-i]
        dec = dec + a*(base**i)
    return dec

def calculator_D_B(base,numero):#base = 2, for binary
    if numero=='':
        numero=0
    numero = int(numero)
    bina = ''
    while True:
        a = numero%base
        bina = bina+str(a)
        numero = numero//base
        if numero < base:
            bina = bina+str(numero)
            break   
    bina = bina[::-1]
    return bina 

##############################################
##############################################

##############################
# Between frame B_D
frame_B_D = LabelFrame(root, padx=5, pady=5)#padx and pady inside of the frame
# in frame text="..." is optional

frame_B_D.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")#padx and pady outside of the frame

#Bin: box and button 
bin_label = Label(frame_B_D, text = " Binary ", font=("", 14))
bin_label.grid(row=0, column=0, pady=5, padx=5, ipady=3)

bin_box = Entry(frame_B_D, width=23, font=("", 12))
bin_box.insert(0, "0")
bin_box.grid(row=1, column=0, pady=5, padx=5, ipady=3)


label = Label(frame_B_D, text = " = ")  
label.grid(row=1, column=1, pady=5, padx=5, ipady=3)


#Dec: box and button 
dec_label = Label(frame_B_D, text = " Decimal ", font=("", 14))
dec_label.grid(row=0, column=2, pady=5, padx=5, ipady=3)

dec_box = Entry(frame_B_D, width=23, font=("", 12))
dec_box.insert(0, "0")
dec_box.grid(row=1, column=2, pady=5, padx=5, ipady=3)

def conversor(a,b):
    if bin_box.get()!=a:
        numero = bin_box.get()
        dec_box.delete("0",END)
        dec_box.insert("0", calculator_B_D(2,numero))
    
    if dec_box.get()!=b:
        numero = dec_box.get()
        bin_box.delete("0",END)
        bin_box.insert("0", calculator_D_B(2,numero))

    a = bin_box.get() 
    b = dec_box.get()

    frame_B_D.after(500, lambda:conversor(a,b))

conversor('0', '0')


###############################

root.mainloop()
