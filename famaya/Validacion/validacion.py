def pedirNumInt(strMsg):
    check = False
    num = 0
    while(not check):
        try:
            num = int(input(strMsg))
            check = True
        except ValueError:
            print('Error, Ingrese número entero')
    return num

def DNI():
    check = False
    while(not check):
        num = pedirNumInt("Ingrese N°DNI: ")
        if len(str(num)) == 8:
            check = True
        else:
            print("Dni debe tener 8 dígitos, vuelva a ingresarlo")
    return list(str(num))

def digitoValid():
    check = False
    while(not check):
        num = pedirNumInt("Ingrese Dígito Validaror: ")
        if len(str(num)) == 1:
            check = True
        else:
            print("Dígito Validador debe ser de 1 dígito, vuelva a ingresarlo")
    return num 

def verDatos(lstVer,strDV):
    strCade = ""
    for strNom in lstVer:
        strCade = strCade + strNom
    print("DNI - DIGITO VALIDADOR: " + strCade +" - " +strDV)

def validarDig(lstVer,strDV):
    lstVar1 = [3,2,7,6,5,4,3,2]
    lstVar2 = [6,7,8,9,0,1,1,2,3,4,5]
    x = 0
    intRDV = 0
    for strDato in lstVer:
        intRDV = intRDV + (int(strDato) * lstVar1[x])
        x = x + 1
    intRDV = intRDV % 9
    intRDV = 11 - intRDV
    if intRDV == 11:
        intRDV = 0
    intRDV = intRDV + 1
    intRDV = lstVar2[intRDV - 1]
    if intRDV == int(strDV):
        print("El dígito Validador es correcto")
    else:
        print("El dígito Validador es incorrecto, registrar nuevamente")