
def notas_validas(nota1, nota2):
    #Se as duas notas recebidas estiverem entre 0 e 10
    if (nota1 >= 0 and nota1 <= 10) and (nota2 >= 0 and nota2 <= 10):
        #Retorne a média dessas duas notas
        return (nota1+nota2)/2
    else: 
        return "nota invalida"

