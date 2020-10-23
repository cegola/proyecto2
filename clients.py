class Clients():
    def validarDNI(dni):
        '''código tomado de la pag web perezmartin.es'''

        try:
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE" #letra dni, lista std
            dig_ext = "XYZ"
            reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'} #tabla letras extrangero
            numeros = "1234567890"
            dni = dni.upper() #a mayusc
            if len(dni) == 9: #debe tener 9 chars
                dig_control = dni[8] #tomo la letra
                dni = dni[:8] #tomo los 8 primeros chars
                if dni[0] in dig_ext:  #comprueba si es extr y si es lo cambia por un nº
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control
                    #comprueba que los primeros 8 chars son numeros y que la letra sea valida
                    #devuelve true si se dan las dos cond y sale del modulo o sino false y sale del modulo
            return False #sino devuelve falso
        except:
            print('error en la app')
            return None
