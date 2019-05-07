import random
from tkinter import *

salto= '/n'
matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def teclas(event):
    if event.keysym=='Up':
        print("arriba")
        aux(0,0)
        arriba(1,0)
    elif event.keysym=='Down':
        print("abajo")
        aux(0,0)
        abajo(0,0)
    
    elif event.keysym=='Left':
        print("izq")
        aux(0,0)
        izquierda(0,1)
    else:
        print("derecha")
        aux(0,0)
        derecha(0,0)

        
def arriba(i,o):
    if i==3 and o ==3:
        
        if matriz[3][3]==matriz[2][3]:
            matriz[2][3]=matriz[3][3]+matriz[2][3]
            matriz[3][3]=0
            armar(0)
            direccion()
        else:
            armar(0)
            direccion()
    elif o==3:
        if matriz[i][3]==matriz[i-1][3]:
            matriz[i-1][3]=matriz[i][3]+matriz[i-1][3]
            matriz[i][3]=0
            return arriba(i+1,0)
        else:
            return arriba(i+1,0)
    else:
        if matriz[i][o]==matriz[i-1][o]:
            matriz[i-1][o]=matriz[i][o]+matriz[i-1][o]
            matriz[i][o]=0
            return arriba(i,o+1)
        else:
            return arriba(i,o+1)
        
def abajo(i,o):
    if i==2 and o ==3:
        
        if matriz[2][3]==matriz[3][3]:
            matriz[3][3]=matriz[2][3]+matriz[3][3]
            matriz[2][3]=0
            armar(0)
            direccion()
        else:
            armar(0)
            direccion()
    elif o==3:
        if matriz[i][3]==matriz[i+1][3]:
            matriz[i+1][3]=matriz[i][3]+matriz[i+1][3]
            matriz[i][3]=0
            return abajo(i+1,0)
        else:
            return arriba(i+1,0)
    else:
        if matriz[i][o]==matriz[i+1][o]:
            matriz[i+1][o]=matriz[i][o]+matriz[i+1][o]
            matriz[i][o]=0
            return abajo(i,o+1)
        else:
            return abajo(i,o+1)
def izquierda(i,o):
    if i==3 and o==3:
        if matriz[3][3]==matriz[3][2]:
            matriz[3][2]=matriz[3][3]+matriz[3][2]
            matriz[3][3]=0
            armar(0)
            direccion()
        else:
            armar(0)
            direccion()
    elif o==3:
        if matriz[i][3]==matriz[i][2]:
            matriz[i][2]=matriz[i][2]+matriz[i][3]
            matriz[i][3]=0
            return izquierda(i+1,0)
        else:
            return izquierda(i+1,0)
    else:
        if matriz[i][o]==matriz[i][o-1]:
            matriz[i][o-1]=matriz[i][o]+matriz[i][o-1]
            matriz[i][o]=0
            return izquierda(i,o+1)
        else:
            return izquierda(i,o+1)
def derecha(i,o):
    if i==3 and o== 2:
        if matriz[3][2]==matriz[3][3]:
            matriz[3][3]=matriz[3][2]+matriz[3][3]
            matriz[3][2]=0
            armar(0)
            direccion()
        else:
            armar(0)
            direccion()
    elif  o==2:
        if matriz[i][2]==matriz[i][3]:
            matriz[i][3]= matriz[i][2]+matriz[i][3]
            matriz[i][2]=0
            return derecha(i+1,0)
        else:
            return derecha(i+1,0)
    else:
        if matriz[i][o]==matriz[i][o+1]:
            matriz[i][o+1]=matriz[i][o]+matriz[i][o+1]
            matriz[i][o]=0
            return derecha(i,o+1)
        else:
            return derecha(i,o+1)









    
def aleatorios():
    f=random.randint(0,3)
    c=random.randint(0,3)
    if matriz[f][c] == 0:
        matriz[f][c]=random.choice((2,4))
        #armar(0)
        
    else:
        return aleatorios()

def armar(i):
    if i==3:
        print(matriz[3])
        print(" ")
    else:
        print(matriz[i])
        return armar(i+1)
def aux(i,o):
    if i==3 and o==3:
        if matriz[i][o]!=0:
            print("Game Over!")
            puntuacion(0,0,0)
        else:
            return aleatorios()
        
    elif i==3:
        return aux(0,o+1)    
    elif matriz[i][o]==0:
        return aleatorios()
    
    else:
        return aux(i+1,o)
def puntuacion(i,o,mayor):
    
    if  i==3 and o==3:
        if matriz[3][3]>mayor:
            mayor=matriz[3][3]
            print(mayor)
            print("Su puntuación fue de: ", mayor)
        else:
            print("Su puntuación fue de: ", mayor)
    elif o==3:
        if matriz[i][3]>mayor:
            mayor=matriz[i][3]
            print(mayor)
            return puntuacion(i+1,0,mayor)
        else:
            return puntuacion(i+1,0,mayor)
    else:
        if matriz[i][o]>mayor:
            mayor=matriz[i][o]
            print(mayor)
            return puntuacion(i,o+1,mayor)
        else:
            return puntuacion(i,o+1,mayor)
            
            

    


def direccion():
    main=Tk()
    main.bind_all("<KeyPress-Up>", teclas)
    main.bind_all("<KeyPress-Down>", teclas)
    main.bind_all("<KeyPress-Left>", teclas)
    main.bind_all("<KeyPress-Right>", teclas)
    main.focus()
    main.geometry("0x0")
    main.mainloop()


direccion()

