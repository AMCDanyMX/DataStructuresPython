def imprimir_matriz(mensaje1,matriz):
    mensaje=mensaje1 + "\n"+"\t"
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            mensaje+=str(matriz[i][j])+ "\t"
        mensaje+="\n"+"\t"
    print(mensaje)
    

#Inicializar las matrices
matriz1=[[1,2],[5,3]]
matriz2=[[4,5], [2,3]]

filas=len(matriz1)
columnas=len(matriz1[1])
print("filas",filas, "columnas", columnas)
suma,multi=[],[]
for i in range(filas):
    suma.append([0]*columnas)
    for j in range(columnas):
        suma[i][j]=matriz1[i][j]+matriz2[i][j]
for i in range(filas):
    multi.append([0]*columnas)
    for j in range(columnas):
        multi[i][j]=matriz1[i][j]*matriz2[i][j]
    
#Imprimir los resultados
print("Resultados")
imprimir_matriz("Matriz 1:",matriz1)
imprimir_matriz("Matriz 2:",matriz2)
imprimir_matriz("Suma:",suma)
imprimir_matriz("Multiplicación:",multi)