
class maquinaTuring:
    global ci
    global t
    global e
    global p

    def computa(self):
        while self.e in self.t.keys():
            ins = self.t[self.e]
            ins = ins[self.ci[self.p]]
            self.ejecuta(ins)
            if self.posicion >= len(self.ci) or self.posicion < 0:
                print("MLE")
                break

    def ejecuta(self, ins):
        self.e = ins[0]
        self.ci[self.p] = ins[1]
        self.movimiento(ins[2])

    def movimiento(self, ins):
        if ins == "R":
            self.posicion += 1
        if ins == "L":
            self.posicion -= 1


def configCinta(n, ci, c):
    for i in range(0, n):
        ci[i] = c


def lee():
    contador = 0
    diccionario = {}
    ci = []
    reglas = int(input("Ingrese el numero de reglas: "))
    reglas = int(reglas / 2)
    for i in range(0, reglas):
        lista = []
        print("Estado ", i)
        for j in range(0, 2):
            print("¨Procesando... ", j)
            lista2 = []
            lista2.append(int(input("Ingrese el nuevo estado: ")))
            lista2.append(int(input("Ingrese la cinta: ")))
            lista2.append(str(input("Ingrese el movimiento: ")))
            lista.append(lista2)
        diccionario[i] = lista
    print(diccionario)
    pruebas = int(input("Ingrese el numero de casos prueba: "))
    listPruebas = []
    for x in range(0, pruebas):
        print("Prueba ", x)
        x = int(input("Ingrese el numero de unos de entrada: "))
        y = int(input("Ingrese el numero de unos de salida: "))
        listPruebas.append((x, y))
        print(listPruebas)
    for x in range(1000):
        ci.append(0)
    for p in listPruebas:
        contador += 1
        configCinta(int(p[0]), ci, 1)
        maquina = maquinaTuring()
        maquina.ci = ci
        maquina.t = diccionario
        maquina.e = 0
        maquina.p = 0
        maquina.computa()
        if contador > 10000:
            print("TLE")
        print("en la prueba:")
        if maquina.ci.count(1) == p[1]:
            print("AC")
        else:
            print("WA")
        configCinta(int(1000), ci, 0)


lee()