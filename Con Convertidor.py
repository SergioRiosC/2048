from tkinter import *
import random
from time import sleep
lista=[]
salto='\n'
tab='\t'
matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
L=input("Ingrese su nombre de usuario: ")


def inicio(L):
    print(salto)
    if L=="":
       print("Ingrese un nombre válido"+salto)
    else:
        return verificar(L,0)
    
def verificar(l,i):
    if lista==[]:
        lista.append(l)
        escribirLogin(l)
        print("Se guardó "+l+" Bienvenido"+salto)
        print("       LEADERBOARD \t\t")
        leaderboard()
    elif i==len(lista)-1:
        if l==lista[i]:
            print("Bienvenido de nuevo "+ l+salto)
            print("       LEADERBOARD \t\t")
            leaderboard()
        else:
            lista.append(l)
            escribirLogin(l)
            print("Se guardó "+l+" Bienvenido"+salto)
            print("       LEADERBOARD \t\t")
            leaderboard()
    else:
        if l==lista[i]:
            print("Bienvenido de nuevo "+ l+salto)
            print("       LEADERBOARD \t\t")
            leaderboard()
        else:
            return verificar(l,i+1)
    
def leaderboard():
    print("Usuario \t Puntuacion"+'\n')
    archivo=open("jugadores.txt","r")
    meter(0)
    archivo.close()

def meter(i):
    if lista==[]:
        print("inicio")
    else:
        if i==len(lista)-1:
            print(lista[i]+salto)
        else:
            print(lista[i]+salto)
            return meter(i+1)

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
    archivo.write(l+salto)    
    archivo.close()

def bases(B):
    
    if B=="":
        print("Ingrese una base válida"+salto)
    elif B=="Binaria" or B=="binaria":
        armar(0)
        direccion()
    elif B=="Octal" or B== "octal":
        armar(0)
        direccion()
    elif B=="Decimal" or B=="decimal":
        armar(0)
        direccion()

    elif B=="Hexadecimal" or B=="hexadecimal":
        armar(0)
        direccion()    
    else:
        print("Ingrese una base válida"+salto)
       
def teclas(event):
    if event.keysym=='Up':
        print("arriba")
        trasArr(0,0)
        aux(0,0)        
    elif event.keysym=='Down':
        print("abajo")
        trasAb(3,0)
        aux(0,0)
        
    
    elif event.keysym=='Left':
        print("izq")
        trasIz(0,0)
        aux(0,0) 
    else:
        print("derecha")
        trasDer(0,3)
        aux(0,0)

def trasArr(i,o):
    if i==2 and o ==3:
        if matriz[2][3]==0:
            matriz[2][3]=matriz[3][3]
            matriz[3][3]=0
            if matriz[1][0]!=0 and matriz[0][0]==0:
                trasArr(0,0)
            elif matriz[1][1]!=0 and matriz[0][1]==0:
                trasArr(0,0)
            elif matriz[1][2]!=0 and matriz[0][2]==0:
                trasArr(0,0)
            elif matriz[1][3]!=0 and matriz[0][3]==0:
                trasArr(0,0)
            else:
                arriba(1,0)
        else:
            if matriz[1][0]!=0 and matriz[0][0]==0:
                trasArr(0,0)
            elif matriz[1][1]!=0 and matriz[0][1]==0:
                trasArr(0,0)
            elif matriz[1][2]!=0 and matriz[0][2]==0:
                trasArr(0,0)
            elif matriz[1][3]!=0 and matriz[0][3]==0:
                trasArr(0,0)
            else:
                arriba(1,0)       
    elif o==3:
        if matriz[i][3]==0:
            matriz[i][3]=matriz[i+1][3]
            matriz[i+1][3]=0
            trasArr(i+1,0)
        else:
            trasArr(i+1,0)
    else:
        if matriz[i][o]==0:
            matriz[i][o]=matriz[i+1][o]
            matriz[i+1][o]=0
            trasArr(i,o+1)
        else:
            trasArr(i,o+1)
            
def trasAb(i,o):
    if i==1 and o==3:
        if matriz[1][3]==0:
            matriz[1][3]=matriz[0][3]
            matriz[0][3]=0
            if matriz[2][3]!=0 and matriz[3][3]==0:
                trasAb(3,0)
            elif matriz[2][2]!=0 and matriz[3][2]==0:
                trasAb(3,0)
            elif matriz[2][1]!=0 and matriz[3][1]==0:
                trasAb(3,0)
            elif matriz[2][0]!=0 and matriz[3][0]==0:
                trasAb(3,0)
            else:
                abajo(0,0)
        else:
            if matriz[2][3]!=0 and matriz[3][3]==0:
                trasAb(3,0)
            elif matriz[2][2]!=0 and matriz[3][2]==0:
                trasAb(3,0)
            elif matriz[2][1]!=0 and matriz[3][1]==0:
                trasAb(3,0)
            elif matriz[2][0]!=0 and matriz[3][0]==0:
                trasAb(3,0)
            else:
                abajo(0,0)      
    elif o==3:
        if matriz[i][3]==0:
            matriz[i][3]=matriz[i-1][3]
            matriz[i-1][3]=0
            trasAb(i-1,0)
        else:
            trasAb(i-1,0)
    else:
        if matriz[i][o]==0:
            matriz[i][o]=matriz[i-1][o]
            matriz[i-1][o]=0
            trasAb(i,o+1)
        else:
            trasAb(i,o+1)

def trasIz(i,o):
    if i==3 and o==2:
        if matriz[3][2]==0:
            matriz[3][2]=matriz[3][3]
            matriz[3][3]=0
            if matriz[0][1]!=0 and matriz[0][0]==0:
                trasIz(0,0)
            elif matriz[1][1]!=0 and matriz[1][0]==0:
                trasIz(0,0)
            elif matriz[2][1]!=0 and matriz[2][0]==0:
                trasIz(0,0)
            elif matriz[3][1]!=0 and matriz[3][0]==0:
                trasIz(0,0)
            else:
                izquierda(0,1)
        else:
            if matriz[0][1]!=0 and matriz[0][0]==0:
                trasIz(0,0)
            elif matriz[1][1]!=0 and matriz[1][0]==0:
                trasIz(0,0)
            elif matriz[2][1]!=0 and matriz[2][0]==0:
                trasIz(0,0)
            elif matriz[3][1]!=0 and matriz[3][0]==0:
                trasIz(0,0)
            else:
                izquierda(0,1)
    elif o==2:
        if matriz[i][2]==0:
            matriz[i][2]=matriz[i][3]
            matriz[i][3]=0
            trasIz(i+1,0)
        else:
            trasIz(i+1,0)
    else:
        if matriz[i][o]==0:
            matriz[i][o]=matriz[i][o+1]
            matriz[i][o+1]=0
            trasIz(i,o+1)
        else:
            trasIz(i,o+1)        

def trasDer(i,o):
    if i==3 and o==1:
        if matriz[3][1]==0:
            matriz[3][1]=matriz[3][0]
            matriz[3][0]=0
            if matriz[0][2]!=0 and matriz[0][3]==0:
                return trasDer(0,3)
            elif matriz[1][2]!=0 and matriz[1][3]==0:
                return trasDer(0,3)
            elif matriz[2][2]!=0 and matriz[2][3]==0:
                return trasDer(0,3)
            elif matriz[3][2]!=0 and matriz[3][3]==0:
                return trasDer(0,3)
            else:
                derecha(0,0)
        else:
            if matriz[0][2]!=0 and matriz[0][3]==0:
                return trasDer(0,3)
            elif matriz[1][2]!=0 and matriz[1][3]==0:
                return trasDer(0,3)
            elif matriz[2][2]!=0 and matriz[2][3]==0:
                return trasDer(0,3)
            elif matriz[3][2]!=0 and matriz[3][3]==0:
                return trasDer(0,3)
            else:
                derecha(0,0)     
    elif o==1:
        if matriz[i][1]==0:
            matriz[i][1]=matriz[i][0]
            matriz[i][0]=0
            return trasDer(i+1,3)
        else:
            return trasDer(i+1,3)
    else:
        if matriz[i][o]==0:
            matriz[i][o]=matriz[i][o-1]
            matriz[i][o-1]=0
            return trasDer(i,o-1)
        else:
            return trasDer(i,o-1)
        
def arriba(i,o):
    if i==3 and o ==3:
        if matriz[3][3]==matriz[2][3]:
            matriz[2][3]=matriz[3][3]+matriz[2][3]
            matriz[3][3]=0
            armar(0)
        else:
            armar(0)
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
        else:
            armar(0)
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
        else:
            armar(0)
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
        else:
            armar(0)
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
    else:
        return aleatorios()
    
def armar(i):
    if B=="Decimal" or B=="decimal":
        if i==3:
            print(matriz[3])
            print(" ")
        else:
            print(matriz[i])
            return armar(i+1)
    elif B=="Binaria" or B=="binaria":
        armaraux(0,0,2)
    elif B=="Octal" or B== "octal":
        armaraux(0,0,8)
    else:
        armaraux(0,0,16)

def armaraux(i,o,b):
    if i==3 and o==3:
        matriz[3][3]=conv(int(matriz[3][3]),b) 
        imp(0)
    elif o==3:
        matriz[i][3]= conv(int(matriz[i][3]),b)
        armaraux(i+1,0,b)
    else:
        matriz[i][o]=conv(int(matriz[i][o]),b)
        armaraux(i,o+1,b)
def imp(i):    
    if i==3:
        print(matriz[3])
        print(" ")
    else:
        print(matriz[i])
        return imp(i+1)

def conv(num,base):
    cadenaConv="0123456789ABCDEF"
    if num<base:
        return cadenaConv[num]
    else:
        return conv(num//base,base)+cadenaConv[num%base]
    
def aux(i,o):
    if B=="Binaria" or B=="binaria":
        auxBin(0,0)
    elif B=="Octal" or B== "octal":
        auxOct(0,0)
    elif B=="Hexadecimal" or B=="hexadecimal":
        auxHex(0,0)        
    else:
        if i==3 and o==3:
            if matriz[i][o]!=0:
                print("Game Over!")
                return puntuacion(0,0,0)
            else:
                return aleatorios()            
        elif o==3:
            if matriz[i][o]==0:
                return aleatorios()
            else:
                return aux(i+1,0)    
        elif matriz[i][o]==0:
            return aleatorios()
        
        else:
            return aux(i,o+1)
       
def puntuacion(i,o,mayor):
    if  i==3 and o==3:
        if int(matriz[3][3])>mayor:
            mayor=matriz[3][3]
            print(L,", su puntuación fue de: ", mayor)
            leadFinal(0,mayor)            
        else:
            print(L,", su puntuación fue de: ", mayor)
            leadFinal(0,mayor)
    elif o==3:
        if int(matriz[i][3])>mayor:
            mayor=matriz[i][3]            
            return puntuacion(i+1,0,mayor)
        else:
            return puntuacion(i+1,0,mayor)
    else:
        if int(matriz[i][o])>mayor:
            mayor=matriz[i][o]
            
            return puntuacion(i,o+1,mayor)
        else:
            return puntuacion(i,o+1,mayor)

def auxBin(i,o):
    if i==3 and o==3:
            if conv(int(matriz[i][o]),2)!=conv(0,2):
                print("Game Over!")
                return puntBin(0,0,0)
            else:
                return aleatoriosBin()            
    elif o==3:
        if conv(int(matriz[i][o]),2)==conv(0,2):
            return aleatoriosBin()
        else:
            return aux(i+1,0)    
    elif conv(int(matriz[i][o]),2)==0:
        return aleatoriosBin()
        
    else:
        return auxBin(i,o+1)
def auxOct(i,o):
    if i==3 and o==3:
            if conv(int(matriz[i][o]),8)!=conv(0,8):
                print("Game Over!")
                return puntOct(0,0,0)
            else:
                return aleatoriosOct()           
    elif o==3:
        if conv(int(matriz[i][o]),8)==conv(0,8):
            return aleatoriosOct()
        else:
            return aux(i+1,0)    
    elif conv(int(matriz[i][o]),8)==0:
        return aleatoriosOct()
        
    else:
        return auxOct(i,o+1)
def auxHex(i,o):
    if i==3 and o==3:
            if conv(int(matriz[i][o]),16)!=conv(0,16):
                print("Game Over!")
                return puntOct(0,0,0)
            else:
                return aleatoriosHex()        
    elif o==3:
        if conv(int(matriz[i][o]),16)==conv(0,16):
            return aleatoriosHex()
        else:
            return aux(i+1,0)    
    elif conv(int(matriz[i][o]),16)==0:
        return aleatoriosHex()        
    else:
        return auxHex(i,o+1)

def aleatoriosBin():
    f=random.randint(0,3)
    c=random.randint(0,3)
    if conv(int(matriz[f][c]),2) =='0':
        matriz[f][c]=random.choice((10,100))
    else:
        return aleatoriosBin()

def aleatoriosOct():
    f=random.randint(0,3)
    c=random.randint(0,3)
    if conv(int(matriz[f][c]),8) =='0':
        matriz[f][c]=random.choice((2,4))
    else:
        return aleatoriosOct()

def aleatoriosHex():
    f=random.randint(0,3)
    c=random.randint(0,3)
    if conv(int(matriz[f][c]),16) =='0':
        matriz[f][c]=random.choice((2,4))
    else:
        return aleatoriosHex()

def puntBin(i,o,mayor):
    if  i==3 and o==3:
        if conv(int(matriz[3][3]),2)>conv(mayor,2):
            mayor=conv(int(matriz[3][3]),2)
            print(L,", su puntuación fue de: ", mayor)
            leadFinal(0,mayor)            
        else:
            print(L,", su puntuación fue de: ", mayor)
            leadFinal(0,mayor)
    elif o==3:
        if conv(int(matriz[i][3]),2)>conv(mayor,2):            
            mayor=conv(int(matriz[i][3]),2)           
            return puntuacion(i+1,0,mayor)
        else:
            return puntuacion(i+1,0,mayor)
    else:
        if conv(int(matriz[i][o]),2)>conv(mayor,2):
            mayor=conv(int(matriz[i][o]),2)
            
            return puntBin(i,o+1,mayor)
        else:
            return puntBin(i,o+1,mayor)

def puntOct(i,o,mayor):
    if  i==3 and o==3:
        if conv(int(matriz[3][3]),8)>conv(mayor,8):
            mayor=conv(int(matriz[3][3]),8)
            print(L,", su puntuación fue de: ", mayor)
            leadFinal(0,mayor)            
        else:
            print(L,", su puntuación fue de: ", mayor)
            leadFinal(0,mayor)
    elif o==3:
        if conv(int(matriz[i][3]),8)>conv(mayor,8):            
            mayor=conv(int(matriz[i][3]),8)            
            return puntuacion(i+1,0,mayor)
        else:
            return puntuacion(i+1,0,mayor)
    else:
        if conv(int(matriz[i][o]),8)>conv(mayor,8):
            mayor=conv(int(matriz[i][o]),8)            
            return puntOct(i,o+1,mayor)
        else:
            return puntOct(i,o+1,mayor)

def puntHex(i,o,mayor):
    if  i==3 and o==3:
        if conv(int(matriz[3][3]),16)>conv(mayor,16):
            mayor=conv(int(matriz[3][3]),16)
            print(L,", su puntuación fue de: ", mayor)
            leadFinal(0,mayor)
        else:
            print(L,", su puntuación fue de: ", mayor)
            leadFinal(0,mayor)
    elif o==3:
        if conv(int(matriz[i][3]),16)>conv(mayor,16):            
            mayor=conv(int(matriz[i][3]),16)
            return puntuacion(i+1,0,mayor)
        else:
            return puntuacion(i+1,0,mayor)
    else:
        if conv(int(matriz[i][o]),16)>conv(mayor,16):
            mayor=conv(int(matriz[i][o]),16)
            return puntHex(i,o+1,mayor)
        else:
            return puntHex(i,o+1,mayor)

def leadFinal(i,m):
    print("Usuario \t Puntuacion"+'\n')
    meter2(0,m)
def meter2(i,m):
    if lista==[]:
        print("Inicio")
    else:
        if i==len(lista)-1:
            if lista[i]==L:
                print(lista[i],tab,tab,m,salto)
                #return escribirPunt(m) 
            else:
                print(lista[i]+salto)
                #return escribirPunt(m)
        else:
            if lista[i]==L:
                print(lista[i],tab,tab,m,salto)
                return meter2(i+1,m)
            else:
                print(lista[i]+salto)
                return meter2(i+1,m)
   
def escribirPunt(m):
    archivo=open("jugadores.txt","r")
    linea=archivo.readline()
    return puntAux(linea,archivo,0,m)
def puntAux(l,archivo,i,m):
    if l:
        if l[-1]==salto:
            l=l[:-1]
            if L==l:
                todo=l,tab,tab,m,salto
                lista.append(todo)
                l=archivo.readline()
                return puntAux(l,archivo,i+1,m)
            else:
                lista.append(l)
                l=archivo.readline()
                return puntAux(l,archivo,i+1,m)  
        else:
            if L==l:
                todo=l,tab,tab,m
                lista.append(todo)
                l=archivo.readline()
                return puntAux(l,archivo,i+1,m)
            else:
                lista.append(l)
                l=archivo.readline()
                return puntAux(l,archivo,i+1,m)
    archivo.close()    
        
def direccion():
    main=Tk()
    main.bind_all("<KeyPress-Up>", teclas)
    main.bind_all("<KeyPress-Down>", teclas)
    main.bind_all("<KeyPress-Left>", teclas)
    main.bind_all("<KeyPress-Right>", teclas)
    main.focus()
    main.geometry("0x0")
    main.mainloop()
iniciarArchivo()
cargar()
inicio(L)
print("Bases: Binaria. Octal. Decimal. Hexadecimal"+salto)    
B=input("Escriba la base a jugar: ")
bases(B)
direccion()

