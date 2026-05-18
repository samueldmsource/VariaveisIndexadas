
'''while True:
    numeros=list(map(int,input("digite valores: ").split()))#[-5,-2,5,7,8,9]
    negativo=[i for i in numeros if i < 0]
    print(negativo)
    if 0 in numeros:
        break'''
from operator import index

#print("pare")
        #break
'''dados=[]
while True:
    numeros=list(map(int,input("digite o valor: ").split()))#[4,7,8,9,25]
    dados.append(numeros)

    if dados:
        maximo=max(dados)
        position=dados.index(maximo)
        if 0 in numeros:
            break
        print(f"valor maximo, {maximo}, na posição , {position}")'''

'''dados=[]
while True:
    numeros=list(map(int,input("digite valores: ").split()))
    dados.append(numeros)
    if numeros==0:
        break
    if dados:
        minimo=min(dados)
        posicao=dados.index(minimo)
        print("menor valor é:", minimo, "na posição", posicao)'''

'''ordenacao=[]
while True:
    numerosOrdenados=list(map(int,input("digite valores: ").split()))
    if numerosOrdenados==0:
        break
    ordenacao.append(numerosOrdenados)
    if ordenacao:
        ordenadas=sorted(ordenacao)
        print(ordenadas)'''

'''somar=[]
while True:
    somaNumeros=int(input("digite um numero: "))
    somar.append(somaNumeros)
    soma = sum(somar)
    print(soma)
    if somaNumeros==0:
        break'''
#letras=[]
'''while True:
    #numeros=int(input("digite um numero: "))
    palavra=input("digite uma palavra: ")
    numero=int(input('Digite um numero: '))
    #letras.append(palavra)

    if palavra:
        print(palavra[:numero+1])
    if palavra=='sair':
        break'''

'''while True:
    letras=input("qual palavra? ")
    numero=int(input('Digite um numero: '))
    
    if letras:
        print(letras[:numero])'''

#acumuladorVetor=[]
'''while True:
    try:
        vetor=list(map(int,input("digite valores inteiros ou negativos: ").split()))
        print(vetor, True)
#inteiros = all(isinstance(y, int) for y in vetor)
    except ValueError:
        print(vetor, False)'''



'''acimaMedia=[]
while True:
    vetor1=list(map(float,input("quais valores para cálculo da média? ").split()))
    if vetor1:
        media = sum(vetor1) / len(vetor1)
        acimaMedia = [w for w in vetor1 if w > media]
        print(media)
        print('valores no vetor acima da media,', acimaMedia)
        vetor1=list(map(float,input("quais valores para cálculo da média? ").split()))
    else:
        print("digite valores inteiros")
        break'''

'''acimaMedia=[]
media=0
while True:
    vetor1 = list(map(float, input("Quais valores para cálculo da média? ").split()))

    if vetor1:
        media = sum(vetor1) / len(vetor1)
        acimaMedia = [w for w in vetor1 if w > media]

        print("Média =", media)
        print("Valores no vetor acima da média:", acimaMedia)
    else:
        print("Digite valores inteiros ou decimais.")'''



'''acimaMedia=[]
valores=[]
while True:
    vetor1 = int(input("qual valor? "))
    valores.append(vetor1)
    
    if valores:
        media = sum(valores) / len(valores)
        acimaMedia = [w for w in valores if w > media]
        print(media)
        print('valores no vetor acima da media,', acimaMedia)

    else:
        print("digite valores inteiros")'''

'''vetorDobrado=[7,11,16]
dobro=[m*2 for m in vetorDobrado]
print(dobro)'''






