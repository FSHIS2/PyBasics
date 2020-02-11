# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
list = [1,True,2.5,[0,1]]
list[0:3] = [False]
tuple = (1,2,4.7,[0,1],(2,3))
tuple = tuple[-5:-1:1] #slicing
string = "hola mundo"
string = string[:5]
dictionary = {"Binary" : (0,1), "Decimal" : "Ten"} #mapping
print(str(type(tuple)) + " :"+ str(tuple) + '\n' +
      str(type(list)) + " :" + str(list) + '\n' +
      str(type(dictionary)) + " :" + str(dictionary) + '\n' +
      str(type(dictionary)) + " :" + str(string))
random = 0
if random < 0 :
    print("Negativo")
elif random > 0 :
    print("Positivo")
else :
    print("Cero")
s = "par" if(random % 2 == 0) else "impar"
print(s)

'''while True :
    entrada = input("> ")
    if entrada != "adiós" :
        print(entrada)
    else:
        break'''
for tuple in 1 :
    print(tuple)

        
