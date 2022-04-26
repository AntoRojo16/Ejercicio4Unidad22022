class Ventana:
    __titulo=""
    __VerticeSupIzX=0
    __VerticeSupIzY=0
    __VerticeInDeX=0
    __VerticeInDeY=0

    def __init__(self,tit,VSIX=12,VSIY=14,VIDX=20,VIDY=18):
        self.__titulo=tit
        self.__VerticeSupIzX=VSIX
        self.__VerticeSupIzY=VSIY
        self.__VerticeInDeX=VIDX
        self.__VerticeInDeY=VIDY

    def mostrar(self):
        print ("Titulo: {} Vertice superior izquierdo X e Y ({},{}) Vertice inferior derecho X e Y ({},{})".format(self.__titulo,self.__VerticeSupIzX,self.__VerticeSupIzY,self.__VerticeInDeX,self.__VerticeInDeY))

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        if self.__VerticeSupIzY<self.__VerticeInDeY:
            alto=self.__VerticeInDeY-self.__VerticeSupIzY
            return alto
        else:
            print("Erorr en los vertices Y, no se puede calcular el alto")

    def ancho(self):
        if self.__VerticeSupIzX<self.__VerticeInDeX:
            ancho=self.__VerticeInDeX-self.__VerticeSupIzX
            return ancho
        else:
            print("Error en los vertices X, no se puede calcular el ancho")

    def moverDerecha(self,num=1):
        self.__VerticeSupIzX +=num
        self.__VerticeInDeX +=num

    def moverIzquierda(self,num=1):
        self.__VerticeSupIzX -=num
        self.__VerticeInDeX -=num

    def bajar (self,num=1):
        self.__VerticeSupIzY -= num
        self.__VerticeInDeY -=num

    def subir(self,num=1):
        self.__VerticeInDeY +=num
        self.__VerticeSupIzY +=num










