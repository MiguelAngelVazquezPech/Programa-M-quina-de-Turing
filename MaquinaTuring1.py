#----------------------------------------------------------------------------------------------------------------
def Turing (estado = None, #estados de la maquina de turing
                   blanco = None, # simbolo blanco de el alfabeto de la cinta
                   reglas = [], #reglas de transicion
                   array = [], #entrada
                   final = None, #estado valido y/o final 
                   posicion = 0): #posicion siguiente de la maquina
#Creamos una funcion llamada Maquina_turing para darle los valores del contenido de la cinta despues
#----------------------------------------------------------------------------------------------------------------
    st = estado #Igualamos la variable st al estado de la maquina
#----------------------------------------------------------------------------------------------------------------
    #seguridad prevenir errores
    if not array: array = [blanco] #Movimiento de la posicion en las entradas
    if posicion < 0 : posicion += len(array)
    #Error cuando la posicion inicia mal
    if posicion >= len(array) or posicion < 0 : raise Error ("Se inicializo mal la posicion")
#Aqui se asegura que el cabezal este este la posicion correcta 
#----------------------------------------------------------------------------------------------------------------
    reglas = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in reglas)#Se evalua cada regla del automata
    """
    Estado	 Símbolo leído	  Símbolo escrito	    Mov. 	  Estado sig.
    p(s0)	      1(v0)	          x(v1)            R(dr)	     p(s1)
    """
#----------------------------------------------------------------------------------------------------------------
    while True:
        print (st, '\t', end = " ")#Impresion con tabulacion
        for i, v in enumerate(array):#Lectura de cada caracter de la lista
            if i == posicion: print ("[%s]"%(v,),end=" ")#imprime los valores
            else: print (v,end=" ")
        print()
#El método Enumerate () agrega un contador a un iterable y lo devuelve en forma de objeto enumerado. 
#Este objeto enumerado se puede usar directamente en bucles for o convertirse en una lista de tuplas usando el método list ().
#----------------------------------------------------------------------------------------------------------------
        if st == final : break #Cuando la posicion llega al estado final termina
        if (st, array[posicion]) not in reglas : break #Termina de revisar las reglas del automata
#----------------------------------------------------------------------------------------------------------------
        (v1,cabezal,s1) = reglas [(st, array[posicion])]#Valida las reglas dependiendo la posicion del puntero
        array[posicion] = v1 # rescribe el simbolo de la cinta    
#----------------------------------------------------------------------------------------------------------------
#movimeinto del cabezal
#Se define como se debe posicionar el puntero
#Ya sea un movimiento por la izquierda o la derecha
        if cabezal == 'left': 
            if posicion > 0 : posicion -= 1
            else: array.insert(0, blanco)
#si la instruccion para el cabezal es irse a la izquierda, el cabezal pasa a la posicion -1 e inserta un 0 invisible
#----------------------------------------------------------------------------------------------------------------
        if cabezal == 'right': 
            posicion += 1
            if posicion >= len(array): array.append(blanco)
        st = s1
#si la instruccion para el cabezal es irse a la derecha, el cabezal pasa a la posicion +1 e inserta el valor de st
#----------------------------------------------------------------------------------------------------------------         
print("Maquina de turing")
print("Duplicación")
dato = input("Ingrese los caracteres aaa: ")
print("Resultado:")
#----------------------------------------------------------------------------------------------------------------
Turing (estado = 's1', #Estado incial
                blanco = 'b', #Caracter del vacio
                array = list(dato), #Valores de entrada
                final = 's4', #Estado final
                reglas = map(tuple,
                            [
                            "s1 a 1 right s1".split(),
                            "s1 b b left  s2".split(),
                            "s2 a a left  s2".split(),
                            "s2 1 a right s3".split(),
                            "s3 a a right s3".split(),
                            "s3 b a left  s2".split(),
                            "s2 b b right s4".split(),
                            ]   
                            )#Reglas del automata
                )
#----------------------------------------------------------------------------------------------------------------