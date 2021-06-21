from Validacion.validacion import *
lstDNI = []
intDV = 0
bolSW = True
while bolSW:
    print("==============")
    print("==============")
    print("    ","MENU","    ")
    print("==============")
    print("==============")
    print("1. Ingrese su número de DNI")
    print("2. Ingresar el dígito validador de su DNI")
    print("3. Revise sus datos registrados")
    print("5. Validar el dígito validador")
    print("0. Salir")
    intOpc = pedirNumInt("Opción: ")
    if intOpc == 1:
        lstDNI = DNI()
    elif intOpc == 2:
        intDV = digitoValid()
    elif intOpc == 3:
        verDatos(lstDNI,str(intDV))
    elif intOpc == 4:
        validarDig(lstDNI,str(intDV))
    elif intOpc == 0:
        bolSW = False
    else:
        print("Introduce un número entre 0-4")