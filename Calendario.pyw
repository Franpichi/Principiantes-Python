from tkinter import *
from tkinter import messagebox

# VAriables

#-----------Funcion de busqueda de fecha-------------------#




#---Esta mal definida----#

def fechaSolicitada():
    buscarFecha.set("")




# Meto la Raiz

raiz=Tk()
año=StringVar()
mes=StringVar()
buscarFecha=StringVar()
fecha=StringVar()







raiz.title("Tu Calendario")

raiz.config(bg="Green")

raiz.config(bd="10")

raiz.config(relief="groove")
Label(raiz, text="Bienvenido a Tu Calendario", bg="Green", font=("Comic Sans MS",19)).pack(anchor=("center"))

# Meto el Frame

miFrame=Frame()
miFrame.pack(side="top", anchor="n")
miFrame.config(bg="light green")
miFrame.config(cursor="pirate")
miFrame.config(width="650", height="350")
miFrame.config(relief="sunken")
miFrame.config(bd=10)

Label(miFrame, text="Busca el dia").pack(anchor=("center"))
Label(miFrame, text="Aquí vas a encontrar la fecha que quieras").pack(anchor=("center"))

Label(miFrame, text="Elija Año:", fg="Blue").pack()
cajaAgno=Entry(miFrame, textvariable=año).pack()

Label(miFrame, text="Elija Mes:", fg="Red").pack()
cajaAgno=Entry(miFrame, textvariable=mes).pack()

 
botonFecha = Button(miFrame, text="Buscar Fecha", command=fechaSolicitada, fg="White", bg="Black", cursor="hand2").pack()
cajaAgno=Entry(miFrame, textvariable=buscarFecha).pack()






# Meto el Calendario







raiz.mainloop()
