def sum_multiplo13(x,y):
    soma = 0

    if x>y:
        x,y=y,x

    for a in range(x, y+1):
        if not (a%13==0):
            soma=soma+a

    return soma

