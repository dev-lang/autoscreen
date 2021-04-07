# !/usr/bin/python3
from tkinter import *

#from tkinter import messagebox
from funciones import *

gui = Tk()
gui.geometry("500x300")
gui.title('Azure Monitoring Automate v0.36.2.7- github.com/dev-lang')
gui.resizable(0,0)




cFlag = int(1)
#destFOlder
#directoryName = "images"
runDestino = True               # a implementar con checkbox
destinoMain = 'portal.azure.com'

manualNot = "Ejecutar Manual"
semiautomaticNot = "Ejecutar Semi-Automatico"
automaticNot = "Ejecutar Automático"
hardcodedNot = "En el modo manual y semi automatico debe\nusar la tecla z cada vez que aparezca un sitio web o cargue uno para capturar\nCerrar para finalizar proceso en memoria"
DEPRECATEDhardcodedNot = "[DEPRECATED MESSAGE]\nModo hardcordeado a Semi automatico\nEjecutar y presionar la tecla Z cada vez que aparezca un sitio web\nCerrar para finalizar proceso de fondo"
developerNot = "Programado por Franco Perez (github: dev-lang)"

def ProvManual():
    #global salida_azure_primera
    #global primeraSIZE
    #global salida_azure_segunda
    #global segundaSIZE
    #global salida_azure_tercera
    #global terceraSIZE
    #global salida_azure_cuarta
    #global cuartaSIZE
    #global salida_azure_ultima
    #global quintaSIZE
    global cFlag
    # probar incorporar un try except para evitar bug de archivo 5
    if cFlag == 1:
            # ingresar(link:azure)
        ejecutaCmd(destinoMain)
        # modificar apartura en manual para que sea bajo condicion con checkbox
        EjecucionManual(primeraSIZE, salida_azure_primera)
        print("Captura " + str(cFlag) + " realizada")
        cFlag += 1
    elif cFlag == 2:
        EjecucionManual(segundaSIZE, salida_azure_segunda)
        print("Captura " + str(cFlag) + " realizada")
        cFlag += 1
    elif cFlag == 3:
        EjecucionManual(terceraSIZE, salida_azure_tercera)
        print("Captura " + str(cFlag) + " realizada")
        cFlag += 1
    elif cFlag == 4:
        EjecucionManual(cuartaSIZE, salida_azure_cuarta)
        print("Captura " + str(cFlag) + " realizada")
        cFlag += 1
    elif cFlag == 5:
        EjecucionManual(quintaSIZE, salida_azure_ultima)
        print("Captura " + str(cFlag) + " realizada")
    else:
        pass
            

ExeManual = Button(gui, text = manualNot, command = ProvManual, width = 20)
ExeManual.place(x = 150,y = 60)

ExeSemiAuto = Button(gui, text = semiautomaticNot, command = EjecucionSemiAutomatica, width = 20)
ExeSemiAuto.place(x = 150,y = 90)

ExeAuto = Button(gui, text = automaticNot, command = EjecucionAutomatica, width = 20)
ExeAuto.place(x = 150,y = 120)

# crear un checkbox condicional
# guardar el estado
# segun estado checked o unchecked usar o no la posibilidad de ejecutar sitio AZURE de forma automatica

# agregar boton manual junto al semi automatico

labelExample = tk.Label(gui, text=hardcodedNot)
labelExample.pack()

statusbar = tk.Label(gui, text=developerNot, bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

gui.mainloop()

# CERRAR PROCESO DE FONDO
teclado.unhook_all()
