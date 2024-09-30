import pandas as pd

def saludar(name:str)->str:
    return f"Hola {name}, Cómo Has Estado?"

def sumar(num1:int|float, num2:int|float)->int|float:
    return num1 + num2

def calcular_area_triangulo(base:int|float, altura:int|float)->int|float:
    return (base*altura)/2

def calcular_precio_final(precio:int|float, impuesto:float|int=.16, descuento:float|int=.10)->int|float:
    tax = precio * impuesto
    desc = precio * descuento
    return (precio - desc)+tax

def sumar_lista(lista:list)->int|float|list:
    suma = 0
    for i in lista:
        suma+= i
    return suma

def producto(name_product:str="CocaCola 300ml", cantidad:int=1, precio_unidad:int|float=10)->str:
    return f"El precio de {cantidad} {name_product} es igual a {cantidad*precio_unidad}$"

def numeros_pares_e_impares(lista:list|tuple)->tuple[list,list]:
    lista_pares = []
    lista_impares = []
    for i in lista:
        if isinstance(i, (int,float)):
            if i % 2 == 0:
                lista_pares.append(i)
            else:
                lista_impares.append(i)
        else: 
            raise ValueError()
    return lista_pares, lista_impares

def multiplicar_todos(*num:int|float|list|tuple)->int|float:
    datos = []
    for n in num:
        if isinstance(n, (list, tuple)):
            datos.extend(n)
        else:
            datos.append(n)
    m = 1
    for dato in datos:
        m = m*dato
        
    if len(datos)>= 1:
        return m
    else:
        return 1

def informacion_personal(**kwargs):
    data = kwargs
    df = pd.DataFrame([data])
    return df

def calculadora_flexible(num1:int|float, num2:int|float, operacion:str="Suma"):
    match operacion:
        case "Suma":
            return num1+num2
        case "Resta":
            return num1-num2
        case "Multiplicación":
            return num1*num2
        case "División":
            return num1/float(num2)
        
