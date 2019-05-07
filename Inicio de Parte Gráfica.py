from tkinter import *
from tkinter import messagebox
from tkinter import ttk

lista=[]
salto='\n'
def guardar():
    L=Login.get()
    if L==" ":
        messagebox.showinfo("Inválido","Ingrese un nombre válido")
    elif L[0]== " ":
        L=L[1:]
        return verificar(L,0)
    else:
        return verificar(L,0)
    
def verificar(l,i):
    if lista==[]:
        lista.append(l)
        escribirLogin(l)
        messagebox.showinfo("Guardado","Se guardó"+" "+Login.get()+" "+"Bienvenido")
        Login.set(" ")
        leaderboard()
        #print("0")
        #print(lista)
        
        #ventana2()
        
  
    elif i==len(lista)-1:
        if l==lista[i]:
            messagebox.showinfo("Bienvenido","Bienvenido de nuevo"+" "+ Login.get())
            Login.set(" ")
            leaderboard()
         #   ventana2()
            #print("1")
            #print(lista)
        else:
            lista.append(l)
            escribirLogin(l)
            messagebox.showinfo("Guardado","Se guardó"+" "+Login.get()+" "+"Bienvenido")
            Login.set(" ")
            leaderboard()
            #print("2")
            #print(lista)
          #  ventana2()
            
    else:
        if l==lista[i]:
            messagebox.showinfo("Bienvenido","Bienvenido de nuevo"+" "+ Login.get())
            Login.set(" ")
            leaderboard()
            #print("3")
            #print(lista)
           # ventana2()
        else:
            #print(i)
            return verificar(l,i+1)
            
        
        
    
def leaderboard():
    r= Text(ventana1,width=50,height=30)
    r.insert(INSERT,"Usuario \t\t Puntuacion"+'\n')
    archivo=open("jugadores.txt","r")
    meter(0,r)
    r.insert(INSERT,salto)
    r.insert(INSERT,Login.get()+salto)
    
    
    r.place(x=50,y=95)
    r.config(state=DISABLED)
def meter(i,r):
    if lista==[]:
        print("inicio")
    else:
        if i==len(lista)-1:
            r.insert(INSERT,lista[i]+salto)
        else:
            r.insert(INSERT,lista[i]+salto)
            return meter(i+1,r)

   

def iniciarArchivo():
    archivo=open("jugadores.txt","a")
    archivo.close()


def cargar():
    archivo=open("jugadores.txt","r")
    linea=archivo.readline()
    return cargaux(linea,0,archivo)
def cargaux(l,i,archivo):
    if l:
        if l[-1]==salto:
            l=l[:-1]
            lista.append(l)
            l=archivo.readline()
            return cargaux(l,i+1,archivo)
        else:
            lista.append(l)
            l=archivo.readline()

            return cargaux(l,i+1,archivo)
    archivo.close()
def escribirLogin(l):
    archivo=open("jugadores.txt","a")
    
    if l[0]== " ":
        archivo.write(l[1:]+salto)
        
    else:
        archivo.write(l+salto)
        
    archivo.close()


    
    
ventana1=Tk()
ventana1.title('2048')
ventana1.geometry("800x650") 
Login=StringVar()
iniciarArchivo()
cargar()
leaderboard()

etiquetaNombre=Label(ventana1,text='2048 por Sergio Ríos').place(x=320,y=0)
etiquetaLeaderboard=Label(ventana1,text='Leaderboard').place(x=50,y=65)
etiquetaLogin=Label(ventana1,text='Ingrese su nombre de usuario').place(x=550,y=270)
login=Entry(ventana1,textvariable=Login).place(x=550,y=300)
botonInicio=Button(ventana1,text="Ingresar",command=guardar).place(x=550,y=350)

Bases=StringVar()
Operaciones=StringVar()
 
def inicio(b):
    print(Bases.get())
    
'''
def opera(x):
    return ventana3()
def ventana3():
    ventana3=Tk()
    ventana3.title('2048')
    ventana3.geometry("800x6500")'''
def ventana2():
    def inicio():
        print(Bases.get()+ '\n'+ Operaciones.get())
    #ventana1.withdraw()
    ventana2=Tk()
    ventana2.title('2048')
    ventana2.geometry("800x650")

    bases=ttk.Combobox(ventana2,textvariable=Bases)
    bases.place(x=310,y=30)
    bases['values']=("Binario","Octal","Decimal","Hexadecimal")
    bases.current(0)
    bases.config(state="readonly")
        
    operaciones=ttk.Combobox(ventana2)
    operaciones.place(x=310,y=90)
    operaciones['values']=("Suma","Multiplicación")
    operaciones.current(0)
    operaciones.config(state="readonly")
    botonIniciar=Button(ventana2,text="Iniciar Juego",command=inicio).place(x=330,y=120)
  
    etiquetaBases=Label(ventana2,text="Elija base numérica").place(x=330,y=0)
    etiquetaOpera=Label(ventana2,text="Elija la operación").place(x=330,y=60)
        



        
    




ventana2()











