from PIL import ImageGrab
import keyboard as teclado
import tkinter as tk
import os as sistema
from codetiming import Timer as cronometro
#import time as tiempo
from time import sleep as dormir

maestro = tk.Tk()
maestro.title("Cerrame :)")
maestro.geometry("400x200")

labelExample = tk.Label(maestro, text="Soy un bug :(\nCerrame porfa")
labelExample.pack()

anchoPantalla = int(maestro.winfo_screenwidth())
altoPantalla = int(maestro.winfo_screenheight())

preconfigMethodOne = 55
preconfigMethodTwo = 255
preconfigMethodThree = 300
preconfigMethodFour = preconfigMethodOne
preconfigMethodFive = preconfigMethodThree + preconfigMethodOne

# valores tomados a partir de 768
## VAULTSERV
primeraSIZE = altoPantalla - preconfigMethodOne
segundaSIZE = altoPantalla - preconfigMethodTwo
## VAULTIRSACORP
terceraSIZE = altoPantalla - preconfigMethodThree
## FILESHARING
cuartaSIZE = altoPantalla - preconfigMethodFour
## LEGALES
quintaSIZE = altoPantalla - preconfigMethodFive

teclaDefinida = 'z'

navegadorElegido = 'msedge'

destino_url = 'portal.office.com'
segundo_url = 'https://www.oracle.com/index.html'
tercer_url = 'https://visualstudio.microsoft.com/es/'
cuarto_url = 'https://aws.amazon.com/es/corretto/'
quinto_url = 'https://ptech.yourlearning.ibm.com/channels/recommended'

salida_azure_primera = 'azure_01.png'
salida_azure_segunda = 'azure_02.png'
salida_azure_tercera = 'azure_03.png'
salida_azure_cuarta = 'azure_04.png'
salida_azure_ultima = 'azure_05.png'


# SHORTCUTS
nuevaPestana = "Ctrl+T"
cerrarPestana = "Ctrl+W"
minimizarTodo = "Win+D"
maximizarVentana = "Win+Up"
restaurarVentana = "Win+Down"
pantallaCompleta = "F11"
Minus = "-"
zoomIn = "Ctrl + Plus"

def controlarZoom(controlkeyaccess):
    teclado.press(controlkeyaccess)
    
def KillMePlease(): # FUNCION PARA ELIMINAR TK (ver como implementar)
    maestro.destroy()

def ejecutaCmd(dest):
    sistema.system("cmd" + "/c start " + navegadorElegido + " " + dest)
    
def cerrarProceso(pim):
    sistema.system("cmd" + "/c start" + " taskkill /F /IM " + pim + ".exe" + " /T")

def PrimerScreenshot(a,b,destino):
    while True:
        try:
            if teclado.is_pressed(teclaDefinida):
                # izq (x), arriba (y), derecha (x), abajo (y)
                # para full screen eliminar el bbox
                image = ImageGrab.grab(bbox=(0,100,a,b))
                ## VAULTSERV
                # primera -55
                # segunda -255
                ## VAULTIRSACORP
                # tercera -300
                ## FILESHARING
                # cuarta -55
                ## LEGALES
                # quinta -355
                image.save(destino)
                break
            else:
                pass
        except:
            break

def screenshotDirecto(a,b,destino):
    #tiempo.sleep(10)
    dormir(10)
    image = ImageGrab.grab(bbox=(0,100,a,b-100))
    image.save(destino)
    
  

def EjecucionAutomatica():
    with cronometro(name="navegador"):
        ejecutaCmd(destino_url)
        #tiempo.sleep(2)
        dormir(2)
        teclado.press(pantallaCompleta)


    screenshotDirecto(anchoPantalla,primeraSIZE, salida_azure_primera)

    with cronometro(name="navegador"):
        ejecutaCmd(segundo_url)

    #tiempo.sleep(2)
        
    screenshotDirecto(anchoPantalla,segundaSIZE, salida_azure_segunda)

    with cronometro(name="navegador"):
        ejecutaCmd(tercer_url)
        
    screenshotDirecto(anchoPantalla,terceraSIZE, salida_azure_tercera)

    with cronometro(name="navegador"):
        ejecutaCmd(cuarto_url)
        
    screenshotDirecto(anchoPantalla,cuartaSIZE, salida_azure_cuarta)

    with cronometro(name="navegador"):
        ejecutaCmd(quinto_url)
        
    screenshotDirecto(anchoPantalla,quintaSIZE, salida_azure_ultima)

    teclado.press(pantallaCompleta)
    
def EjecucionSemiAutomatica():
    # EJECUCION MANUAL ORIGINAL
    
    with cronometro(name="navegador"):
        ejecutaCmd(destino_url)
        dormir(2)
        teclado.press(pantallaCompleta)

    PrimerScreenshot(anchoPantalla,primeraSIZE, salida_azure_primera)

    with cronometro(name="navegador"):
        ejecutaCmd(segundo_url)

    PrimerScreenshot(anchoPantalla,segundaSIZE, salida_azure_segunda)


    with cronometro(name="navegador"):
        ejecutaCmd(tercer_url)

    PrimerScreenshot(anchoPantalla,terceraSIZE, salida_azure_tercera)

    with cronometro(name="navegador"):
        ejecutaCmd(cuarto_url)

    PrimerScreenshot(anchoPantalla,cuartaSIZE, salida_azure_cuarta)

    with cronometro(name="navegador"):
        ejecutaCmd(quinto_url)

    PrimerScreenshot(anchoPantalla,quintaSIZE, salida_azure_ultima)
    
    teclado.press(pantallaCompleta)
    #cerrarProceso(navegadorElegido)
    
def EjecucionManual(primeraSIZE, salida_azure_primera):
    # en desarrollo
    # ERROR
    #dormir(15)
    # PrimerScreenshot(anchoPantalla,primeraSIZE, salida_azure_primera)
    
    # agregar chequeo de existencia o agregar al main la posibilidad de elegir que picture sacar
    
    with cronometro(name="navegador"):
        print("Captura Preparada\nEjecutar la tecla asignada " + teclaDefinida + " cuando esté listo")
        
    PrimerScreenshot(anchoPantalla,primeraSIZE, salida_azure_primera)
    teclado.unhook_all()
    
def IncrementarNumeroDeArchivo(n): # DEPRECATED FUNCTION
    # falta sacar resultado a otro lado
    # asi no queda siempre con el mismo valor estático
    ## METODO PROVISORIO, QUIZAS DEFINITIVO:
    ### USAR argv n
    global numeroFile
    global nombreID
    global formato
    global nombreArchivo
    numeroFile = int(n)
    nombreID = "azure_0"
    formato = ".png"
    numeroFile += 1
    nombreArchivo = nombreID + str(numeroFile) + formato
    print("numero actual: " + str(numeroFile))
    print("nombre archivo salida: " + nombreArchivo)
    
## implementar:
    ## if file exists:
        ## Incrementar
