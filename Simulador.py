#Simulador de Inversion
from datetime import date
from datetime import datetime

from tkinter import *
from tkinter import messagebox

ventana= Tk()
ventana.title('Simulador de Inversión')
ventana.geometry('500x700')

def convertir_dia():
    valor_texto = dia.get()
    try:
        valor_entero = int(valor_texto)
        print("El valor entero es:", valor_entero)
    except ValueError:
        print("El valor no es un entero válido")
    print(type(dia))

def convertir_mes():
    try:
        valor_entero = int(mes.get())
        print("El valor entero es:", valor_entero)
    except ValueError:
        print("El valor no es un entero válido")
    print(type(mes))

def convertir_anual():
    valor_texto = anual.get()
    valor_entero = int(valor_texto)
    print("El valor entero es:", valor_entero)
    #except ValueError:
        #print("El valor no es un entero válido")
    print(type(anual))

def convertir_inversion():
    valor_texto = inversion.get()
    try:
        valor_entero = int(valor_texto)
        print("El valor entero es:", valor_entero)
    except ValueError:
        print("El valor no es un entero válido")  
    print(type(inversion))   

# botonDia = Button(ventana,text='Guardar',command=clickar)
# botonDia.place(x=50,y=500)

etiqueta1 = Label(ventana,text='Ingrese fecha en la que invirtió:')
etiqueta1.place(x=20,y=50)

dia = Entry(ventana, width=30)
dia.place(x=20,y=100)

etiqueta2 = Label(ventana,text='Ingrese el número del mes en el que invirtió: ')
etiqueta2.place(x=20,y=150)

mes= Entry(ventana, width=30)
mes.place(x=20,y=200)

etiqueta3 = Label(ventana,text='Ingrese año en el que invirtió: ')
etiqueta3.place(x=20,y=250)

anual= Entry(ventana, width=30)
anual.place(x=20,y=300)

etiqueta4 = Label(ventana,text='Ingrese el monto de lo que invirtió: ')
etiqueta4.place(x=20,y=350)

inversion= Entry(ventana, width=30)
inversion.place(x=20,y=400)

etiqueta44 = Label(ventana,text='Ingrese la tasa anual de interés: ')
etiqueta44.place(x=20,y=450)

tasa= Entry(ventana, width=10)
tasa.place(x=20,y=500)

#se llama a la funcion que convierte entry a int pero realmente debe estar esto dentro de la funcion fecha para que funcione
botonDia = Button(ventana,text='Guardar dia',command=convertir_dia)
botonDia.place(x=300,y=100)
botonMes = Button(ventana,text='Guardar mes',command=convertir_mes)
botonMes.place(x=300,y=200)
botonAnual = Button(ventana,text='Guardar año',command=convertir_anual)
botonAnual.place(x=300,y=300)
botonInver = Button(ventana,text='Guardar monto',command=convertir_inversion)
botonInver.place(x=300,y=400)


#tasa = 0.0002864 #es la tasa diaria de interes generado sobre el monto acumulado FONDO CRECIMIENTO: 5.25%
#tasa = 0.000147500 #es la tasa diaria de interes generado sobre el monto acumulado FONDO DISPONIBLE:9.5%

def fecha():
    dia_valor = int(dia.get())
    mes_valor = int(mes.get())
    anual_valor = int(anual.get())
    inversion_valor = int(inversion.get())
    tasa_valor= float(tasa.get())/(365*100)
    inicio = datetime(anual_valor, mes_valor, dia_valor)
    hoy= datetime.now()
    plazo_ahorro = hoy-inicio
    print(inicio)
    plazo_ahorro_sec = plazo_ahorro.total_seconds()
    plazo = int(plazo_ahorro_sec) // 86400
    #plazo = int(input('Ingrese el plazo de la inversión en días: '))
    contador=1
    ahorro = inversion_valor
    monto= 0

    while contador<plazo:
        contador+=1
        monto=ahorro+ahorro*tasa_valor
        ahorro = monto
        cadiem=(0.0025)*ahorro
        real=ahorro-cadiem
    messagebox.showinfo("Resultados de Inversión", f"El monto ahorrado hasta la fecha es: {ahorro}\nPagas a CADIEM: {cadiem}\nLuego de pagar a CADIEM el ahorro real sería: {real}")



    
botonAhorro = Button(ventana,text='Calcular la inversión si retiro hoy',command=fecha)
botonAhorro.place(x=50,y=550)


ventana.mainloop()

