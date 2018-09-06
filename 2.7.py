def validaData(dia, mes, ano):
    validador = False
    if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
        if(dia <= 31):
            validador = True
    elif (mes==4 or mes==6 or mes==9 or mes==11):
        if(dia <= 30):
            validador = True
    elif mes == 2:
        if(ano%4==0 and ano%400!=0) or (ano%400==0):
            if(dia<=29):
                validador = True
            elif(dia<=28):
                validador = True
    if(validador):
        print('Data valida')
    else:
        print('Data invalida')

validaData(23,8,1995)
validaData(45,8,1995)