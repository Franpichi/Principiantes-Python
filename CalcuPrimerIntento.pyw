from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

raiz=Tk()

#Funciones Emergentes:

def infoActividad ():
    messagebox.showinfo("Información de Actividad", "Usted está utilizando este programa")

def infoAcercaDe ():
    messagebox.showwarning("Programa Numero 1", "Usted está en el primer programa que hice")

def infoActualizaciones ():
    messagebox.showwarning("Cuadro de Actualización", "No posee otra actualización")

def infoLicencia ():
    messagebox.showerror("Licencia", "No posee licencia de uso")

def infoSalir ():
    valor=messagebox.askokcancel("Salir", "¿Desea Salir?")
    if valor==True:
        raiz.destroy()

def infoCerrar ():
    valor2=messagebox.askokcancel("Cerrar", "¿Desea Cerrar?")
    if valor2==True:
        raiz.destroy()

def abrirFicheros ():
    filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros Excel", "*xlsx"),("Ficheros Textos", "*txt"),("Todos los Ficheros", "*.*")))

def botonAceptar ():
    valor3=messagebox.askokcancel("Finalizar Carga de Datos", "¿Todos los datos son correctos?")
    if valor3==True:
        raiz.destroy()

raiz.iconbitmap("LogoPrimerPrograma.ico")
raiz.title("Practica")

raiz.config(bg="Light Blue")

raiz.config(bd="10")

raiz.config(relief="groove")
raiz.geometry("650x350")

Label(raiz, text="Practica Texto y Cajon", bg="Blue", font=("Comic Sans MS",19)).pack(anchor=("center"))

miFrame=Frame()
miFrame.pack(side="top", anchor="n", fill="x", expand="True")
miFrame.config(bg="Blue")
miFrame.config(width="400", height="400")
miFrame.config(cursor="pirate")
miFrame.config(relief="groove")
miFrame.config(bd=10)

#Coloco Imagen Arriba



#Coloco los Labels

miLabel1=Label(miFrame, text="Nombre")
miLabel1.grid(row=0, column=0, padx=5, pady=5)

cajaNombre=Entry(miFrame)
cajaNombre.grid(row=0, column=1, padx=5, pady=5)

miLabel2=Label(miFrame, text="Apellido")
miLabel2.grid(row=1, column=0, padx=5, pady=5)

cajaApellido=Entry(miFrame)
cajaApellido.grid(row=1, column=1, padx=5, pady=5)

miLabel3=Label(miFrame, text="Telefono")
miLabel3.grid(row=0, column=2, padx=5, pady=5)

cajaTelefono=Entry(miFrame)
cajaTelefono.grid(row=0, column=3, padx=5, pady=5)

miLabel4=Label(miFrame, text="Correo")
miLabel4.grid(row=1, column=2, padx=5, pady=5)
cajaEmail=False
for i in [cajaEmail]:
    if (i=="@"):
        cajaEmail=True

    if (cajaEmail==False):
        def error():
            error=messagebox.askquestion("no es un formato valido", "no es un email")
        
    




cajaEmail=Entry(miFrame)
cajaEmail.grid(row=1, column=3, padx=5, pady=5)

miLabel5=Label(miFrame, text="Telefono2")
miLabel5.grid(row=0, column=4, padx=5, pady=5)

cajaTelefono2=Entry(miFrame)
cajaTelefono2.grid(row=0, column=5, padx=5, pady=5)

miLabel6=Label(miFrame, text="Correo2")
miLabel6.grid(row=1, column=4, padx=5, pady=5)

cajaCorreo2=Entry(miFrame)
cajaCorreo2.grid(row=1, column=5, padx=5, pady=5)

botonAceptar=Button(miFrame, text="Aceptar", cursor="hand2", command=botonAceptar)
botonAceptar.grid(row=2, column=2, padx=15, pady=15)


#Menu Archivo
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Abrir", command=abrirFicheros)
archivoMenu.add_command(label="Cargar")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=infoSalir)
archivoMenu.add_command(label="Cerrar", command=infoCerrar)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

#Menu Editar

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Deshacer")
archivoMenu.add_command(label="Rehacer")
archivoMenu.add_separator()
archivoMenu.add_command(label="Copiar")
archivoMenu.add_command(label="Cortar")
archivoMenu.add_command(label="Pegar")
archivoMenu.add_separator()

barraMenu.add_cascade(label="Editar", menu=archivoMenu)

#Menu Ayuda

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Ver Licencia", command=infoLicencia)
archivoMenu.add_command(label="Privacidad")
archivoMenu.add_separator()
archivoMenu.add_command(label="Actualizaciones", command=infoActualizaciones)
archivoMenu.add_separator()
archivoMenu.add_command(label="Acerca De", command=infoAcercaDe)
archivoMenu.add_command(label="Informacion de Actividad", command=infoActividad)
archivoMenu.add_separator()

barraMenu.add_cascade(label="Ayuda", menu=archivoMenu)

#Ventanas Emergentes

def infoActividad ():
    messagebox.showinfo("Información de Actividad", "Usted está utilizando este programa")





raiz.mainloop()

