"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import fileinput
import os
import csv

datos = []
with open("data.csv", "r") as archivo_datos:
    lector = csv.reader(archivo_datos, delimiter="\t")
    for fila in lector:
        datos.append(fila)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    suma = 0
    for i in datos:
        suma += int(i[1])

    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    letras={}
    for i in datos:
        if i[0] in letras:
            letras[i[0]] += 1
        else:
            letras[i[0]] = 1
    letras = sorted(letras.items())
    
    return letras


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    letras={}
    for i in datos:
        if i[0] in letras:
            letras[i[0]] +=int(i[1])
        else:
            letras[i[0]] = int(i[1])
    letras = sorted(letras.items())
    
    return letras



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    meses={}
    for i in datos:
        mes = i[2].split("-")[1]
        if mes in meses:
            meses[mes] += 1
        else:
            meses[mes] = 1
    return sorted(meses.items())

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    letras={}
    for i in datos:
        if i[0] in letras:
            if int(i[1]) > letras[i[0]][0]:
                letras[i[0]][0] = int(i[1])
            if int(i[1]) < letras[i[0]][1]:
                letras[i[0]][1] = int(i[1])
        else:
            letras[i[0]] = [int(i[1]),int(i[1])]
    letras = [(k,v[0],v[1]) for k,v in letras.items()]
    return sorted(letras, key=lambda x: x[0])


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    diccionario={}
    for i in datos:
        cadena= i[4].split(",")
        for j in cadena:
            clave= str(j.split(":")[0])
            valor= int(j.split(":")[1])
            
            if clave in diccionario:
                if valor > diccionario[clave][1]:
                    diccionario[clave][1] =  valor
                if valor < diccionario[clave][0]:
                    diccionario[clave][0] =  valor
            else:
                diccionario[clave] = [valor,valor]

    letras = [(k,v[0],v[1]) for k,v in diccionario.items()]
    return sorted(letras, key=lambda x: x[0])



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    [
        ('0', ['C']), 
        ('1', ['E', 'B', 'E']), 
        ('2', ['A', 'E']), 
        ('3', ['A', 'B', 'D', 'E', 'E', 'D']), 
        ('4', ['E', 'B']), 
        ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E']), 
        ('6', ['C', 'E', 'A', 'B']), 
        ('7', ['A', 'C', 'E', 'D']), 
        ('8', ['E', 'D', 'E', 'A', 'B']), 
        ('9', ['A', 'B', 'E', 'A', 'A', 'C'])
        ]

    """
    numeros={}
    for i in datos:
        valor=int(i[1])
        if valor in numeros:
            numeros[valor].append(i[0])
        else:
            numeros[valor] = [i[0]]
    numeros=  sorted(numeros.items())
    return numeros



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    numeros={}
    for i in datos:
        valor=int(i[1])
        if valor in numeros:
            if i[0] not in numeros[valor]:
                numeros[valor].append(i[0])
                numeros[valor].sort()
        else:
            numeros[valor] = [i[0]]
    numeros=  sorted(numeros.items())
    return numeros


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    diccionario={}
    for i in datos:
        cadena= i[4].split(",")
        for j in cadena:
            clave= str(j.split(":")[0])
            valor= int(j.split(":")[1])
            
            if clave in diccionario:
                diccionario[clave] += 1
            else:
                diccionario[clave] = 1
    diccionario = dict(sorted(diccionario.items()))
    return diccionario


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    lista=[]
    for i in datos:
        lista.append((i[0],len(i[3].split(",")),len(i[4].split(","))))
    return lista


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    diccionario={}
    for i in datos:
        cadena= i[3].split(",")
        for j in cadena:
            if j in diccionario:
                diccionario[j] += int(i[1])
            else:
                diccionario[j] = int(i[1])
    diccionario = dict(sorted(diccionario.items()))
    return diccionario


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    diccionario={}
    for i in datos:
        cadena= i[4].split(",")
        for j in cadena:
            valor= int(j.split(":")[1])
            if i[0] in diccionario:
                diccionario[i[0]] += valor
            else:
                diccionario[i[0]] = valor
    diccionario = dict(sorted(diccionario.items()))
    return diccionario
