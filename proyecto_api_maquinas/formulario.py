import tkinter as ventana
def enviar_info():
    print("datos enviados a la base de datos")

formulario = ventana.Tk()
formulario.title("registro de maquinas") 

codigo_maquina = ventana.Label (formulario, text= "codigo maquina" ) 

codigo_maquina.pack()

texto_codigo = ventana.Entry(formulario)
texto_codigo.pack() 


nombre_maquina= ventana.Label(formulario,text="nombre de la maquina: ")

nombre_maquina.pack( )
texto_nombre = ventana.Entry(formulario)
texto_nombre.pack()

modelo_maquina = ventana.Label(formulario, text= "modelo maquina: ")
modelo_maquina.pack()

texto_modelo= ventana.Entry(formulario)
texto_modelo.pack()

estado_maquina = ventana.Label(formulario, text= "estado maquina: ")

estado_maquina.pack ()
texto_estado = ventana.Entry(formulario)
texto_estado.pack()

boton_maquina = ventana.Button( formulario, text= "estado maquinna: ", command= enviar_info)

boton_maquina.pack()


formulario.mainloop()