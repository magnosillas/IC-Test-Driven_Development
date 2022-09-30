def quadrado_cubo (teste):
    result=[]
    for num in range(1,teste+1):
        result.append(str(num) + " " + str(pow(num,2))+" " +str(pow(num,3)))
    return result

