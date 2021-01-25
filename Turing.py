def maquina_turing(cadena, remplazo, movimiento, nuevo_estado):
    global cabezal, estado
    if cinta[cabezal] == cadena:
        cinta[cabezal] = remplazo
        estado = nuevo_estado
        if movimiento == 'Izquierda':
            cabezal -= 1
        else:
            cabezal += 1
        return True
    return False
print("------------------------------REGLAS------------------------------")
print("Cadena en blanco")
print("La lista contiene solo a y su número total es par")
print("La lista contiene solo b y su número total es par")
print("La entrada es una combinación de a y b y su número total es par")
print("----------------------------ACLARACIONES--------------------------")
print("El primer conjunto de a se reemplaza por X y el segundo por Z")
print("El primer conjunto de b se reemplaza por U y el segundo por V")
print("------------------------------------------------------------------")
cadena = input("Ingrese una cadena: ")
#remplazar = input ("Ingrese el reemplazo: ")
tamaño = len(cadena) + 2
cinta = ['I']*tamaño
i = 1
cabezal = 1
for s in cadena: #lazo para colocar cuerda en cinta
    cinta[i] = s
    i += 1
estado = 0
#asignar caracteres a la variable para que no tenga que usar caracteres cada vez
a, b, X, Z, U, V, DERECHA, Izquierda, I = 'a', 'b', 'X', 'Z', 'U', 'V', 'DERECHA', 'Izquierda', 'I' 
cabezalviejo = -1
accept = False
while(cabezalviejo != cabezal): #si la cabeza de cinta no se mueve, eso significa terminar la máquina de Turing
    cabezalviejo = cabezal
    print(cinta , "con cabezal de cinta en el índice",cabezal, "en estado" , estado)
    
    if estado == 0:
        if maquina_turing(a, X, DERECHA, 1) or maquina_turing(I, I, DERECHA, 10) or maquina_turing(Z, Z, DERECHA, 7) or maquina_turing(b, U, DERECHA, 4):
            pass     
    elif estado == 1:
        if maquina_turing(a, a, DERECHA, 1) or maquina_turing(b, b, DERECHA, 2) or maquina_turing(I, I, Izquierda, 11):
            pass   
    elif estado == 2:
        if maquina_turing(b, b, DERECHA, 2) or maquina_turing(Z, Z, DERECHA, 2) or maquina_turing(a, Z, Izquierda, 3):
            pass       
    elif estado == 3:
        if maquina_turing(b, b, Izquierda, 3) or maquina_turing(Z, Z, Izquierda, 3) or maquina_turing(a, a, Izquierda, 3) or maquina_turing(X, X, DERECHA, 0):
            pass
    elif estado == 4:
        if maquina_turing(b, b, DERECHA, 4) or maquina_turing(Z, Z, DERECHA, 5) or maquina_turing(I, I, Izquierda, 15):
            pass   
    elif estado == 5:
        if maquina_turing(Z, Z, DERECHA, 5) or maquina_turing(V, V, DERECHA, 5) or maquina_turing(b, V, Izquierda, 6):
            pass   
    elif estado == 6:
        if maquina_turing(Z, Z, Izquierda, 6) or maquina_turing(V, V, Izquierda, 6) or maquina_turing(b, b, Izquierda, 6) or maquina_turing(U, U, DERECHA, 0):
            pass          
    elif estado == 7:
        if maquina_turing(Z, Z, DERECHA, 7) or maquina_turing(V, V, DERECHA, 8):
            pass          
    elif estado == 8:
        if maquina_turing(V, V, DERECHA, 8) or maquina_turing(I, I, DERECHA, 9):
            pass      
    elif estado == 11:
        if maquina_turing(a, a, Izquierda, 11) or maquina_turing(X, X, DERECHA, 12):
            pass
    elif estado == 12:
        if maquina_turing(a, Z, DERECHA, 13):
            pass       
    elif estado == 13:
        if maquina_turing(a, X, DERECHA, 12) or maquina_turing(I, I, DERECHA, 14):
            pass           
    elif estado == 15:
        if maquina_turing(b, b, Izquierda, 15) or maquina_turing(U, U, DERECHA, 16):
            pass          
    elif estado == 16:
        if maquina_turing(b, V, DERECHA, 17):
            pass            
    elif estado == 17:
        if maquina_turing(b, U, DERECHA, 16) or maquina_turing(I, I, DERECHA, 18):
            pass            
    else:
        accept = True    
if accept:
    print("Cadena aceptada en el estado = ", estado)
else:
    print("Cadena NO aceptada en el estado = ", estado)