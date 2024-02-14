class persona: 
    __direccion ='cra 12A'
    def __init__(self, nombre, edad):
        # print('Se activo el ocntructor')
        self.__nombre = nombre
        self.edad=edad
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    def getDireccion(self):
        return self.__direccion
    # def metodo (self):
    #     print('soy un metodo en la clase gente')

objeto = persona ('pepe', 30)
print(objeto.getNombre())
objeto.setNombre('Jose Perez')
print(objeto.getNombre())

print(objeto.getDireccion())

