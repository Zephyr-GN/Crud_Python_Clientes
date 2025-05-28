import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Clientes import *
from Conexion import *



class FormularioClientes:
 global base
 base=None
 global textBoxId
 textBoxId=None
 global texBoxNombres
 texBoxNombres=None
 global texBoxApellidos
 texBoxApellidos=None
 global combo
 combo=None
 global groupBox
 groupBox=None
 global tree
 tree=None


def Formulario():
    global textBoxId
    global texBoxNombres
    global texBoxApellidos
    global combo
    global base
    global groupBox
    global tree

    try:
            base = Tk()
            base.geometry("1200x300")
            base.title("Formulario Python")
            groupBox = LabelFrame(base,text="Datos del Personal", padx=5, pady=5)
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelId=Label(groupBox,text="Id:",width=13,font=("arial",12)).grid(row=0,column=0)
            texBoxId=Entry(groupBox)
            texBoxId.grid(row=0,column=1)

            labelNombres=Label(groupBox,text="Nombres:",width=13,font=("arial",12)).grid(row=1,column=0)
            texBoxNombres=Entry(groupBox)
            texBoxNombres.grid(row=1,column=1)

            labelApellidos=Label(groupBox,text="Apellidos:",width=13,font=("arial",12)).grid(row=2,column=0)
            texBoxApellidos=Entry(groupBox)
            texBoxApellidos.grid(row=2,column=1)

            labelSexo=Label(groupBox,text="Sexo:",width=13,font=("arial",12)).grid(row=3,column=0)
            seleccionSexo= tk.StringVar()
            combo= ttk.Combobox(groupBox,values=["Masculino","Femenino"],textvariable=seleccionSexo)
            combo.grid(row=3,column=1)
            seleccionSexo.set("Masculino")

            Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=4,column=0)
            Button(groupBox,text="Modificar",width=10).grid(row=4,column=1)
            Button(groupBox,text="Eliminar",width=10).grid(row=4,column=2)

            groupBox=LabelFrame(base,text="Datos del Personal", padx=5, pady=5)
            groupBox.grid(row=0,column=1,padx=5,pady=5)

            # Creando un treeview y configurando columnas
            
            tree=ttk.Treeview(groupBox,columns=("Id","Nombres","Apellidos","Sexo"),show='headings',height=5,)
            tree.column("# 1",anchor=CENTER)
            tree.heading("# 1",text="Id")
            tree.column("# 2",anchor=CENTER)
            tree.heading("# 2",text="Nombres")
            tree.column("# 3",anchor=CENTER)
            tree.heading("# 3",text="Apellidos")
            tree.column("# 4",anchor=CENTER)
            tree.heading("# 4",text="Sexo")
            tree.pack()
            

            base.mainloop()
    except ValueError as error:
            print("Error al mostrar la interfaz, error {}".format(error))
    
def guardarRegistros():
        global texBoxNombres, texBoxApellidos, combo, groupBox

        #.
        try:
            #Verificar si los botones estan funcionando
            if texBoxNombres is None or texBoxApellidos is None or combo is None:
                print("Los botones estan funcionando")
                return
            nombres=texBoxNombres.get()
            apellidos=texBoxApellidos.get()
            sexo=combo.get()

            CClientes.ingresarClientes(nombres,apellidos,sexo)
            messagebox.showinfo("Informacion","Los datos fueron guardados")

            #Limpiamos los campos
            texBoxNombres.delete(0,END)
            texBoxApellidos.delete(0,END)

        except ValueError as error:
            print("Error al ingresar datos {}".format(error))

Formulario()
