#!/usr/bin/python3

 
#• Em python 3, Utilizando objetos da classe string e seus métodos, resolva as questões a seguir:


#1) Faça um programa que leia uma frase e determine quantas vezes um determinado caractere, também informado pelo usuário, ocorre na frase.


leitor = str(input(" Digite uma frase: \n"))
caractere = str(input("\n Digite somente um caractere que deseja verificar a repetição na sua frase: \n"))
print("\n O caractere '",caractere,"' se repete ou ocorre ",leitor.count(str(caractere)), " vezes!")





#2) Escreva um programa que informe a quantidade de vogais presentes em uma palavra informada pelo usuário.

leitor = str(input("\n Digite uma palavra: "))
verificador = leitor.isalpha()
if verificador == True:
    print("\n Existem '",leitor.count("a"),"' caracteres com a vogal 'a'\n Existem '",leitor.count("e"),"' caracteres com a vogal 'e'\n Existem '",leitor.count("i"),"' caracteres com a vogal 'i'\n Existem '",leitor.count("o"),"' caracteres com a vogal 'o'\n Existem '",leitor.count("u"),"' caracteres com a vogal 'a'\n")
else:
    print("\n Tente novamente! somente letras por favor!")
    




#3) Implemente um programa que leia uma palavra e verifique se a mesma é palíndromo. Um palíndromo é uma palavra que pode ser lida igualmente de trás pra frente e de frente pra trás. Exemplo: arara.


leitor = str(input("\n Digite uma palavra: "))
verificador = leitor.isalpha()
if verificador == True:
    verificador1 = leitor[::-1]
    if leitor == verificador1:
        print("\n A palavra '",leitor,"' é palíndroma!")
    else:
        print("\n A palavra '",leitor,"' não é palíndroma!")  
else:
    print("\n Tente novamente! somente letras por favor!")




#4) Faça um programa que leia uma frase e depois altere a sequência de suas palavras pondo-as em ordem alfabética.


leitor = str(input("\n Digite uma frase: "))
minusculo = leitor.lower()
virgula = minusculo.replace(' ',',')
lista = virgula.split(",")
lista.sort()
finalizar = ' '.join(lista)

print("\n",finalizar)



#5) Faça um programa que leia um nome completo e apresente-o da seguinte forma:
Nome: João Maria Silva Resultado: Silva, João

leitor = str(input("\n Digite seu nome completo: "))
virgula = leitor.replace(' ',',')
lista = virgula.split(',')

print("\n Nome:" ,leitor," Resultado: ",lista[-1],",",lista[0])

