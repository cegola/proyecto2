import var,sys,clients



class Eventos():

        def Saludo():
            try:
                var.ui.lblHola.setText('Has pulsado el botón')
            except Exception as error:
                print('Error: %s ' % str(error))

        '''Eventos generales'''
        def Salir(self):
            try:
                sys.exit()
            except Exception as error:
                print("Error %s: " % str(error))

        def validoDNI():
            try:
                dni = var.ui.editDni.text()
                if clients.Clients.validarDNI(dni):
                    var.ui.lblValido.setStyleSheet('QLabel {color: green;}')
                    var.ui.lblValido.setText('V')
                    var.ui.editDni.setText(dni.upper())
                else:
                    var.ui.lblValido.setStyleSheet('QLabel {color:red;}')
                    var.ui.lblValido.setText('X')
                    var.ui.editDni.setText(dni.upper())

            except Exception as error:
                print('Error: %s ' % str(error))