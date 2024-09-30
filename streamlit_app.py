import TareaFunciones as tf
import streamlit as st
import pandas as pd

global GitHubUsage, GitHubTech
GitHubUsage = "https://github.com/YerayAnguiano/menu-de-opciones"
GitHubTech = "https://github.com/YerayAnguiano/Funcionameinto-de-Menu-de-Opciones"

def pagina0():
    st.title("Menú de Aplicaciones")
    st.header("by Yeray Anguiano")
    st.write("En la Barra Lateral se Encuentra el Menú de Opciones")
    st.write("Para Ayuda y Preguntas Frecuentes selecciona <FAQs>")

def pagina1():
    st.title("Saluda A Un Colega")
    st.header("Ingrea el Nombre de tu Colega:")
    nombre =  st.text_input("Escriba el Nombre")
    saludo = st.button("Saludar")
    if saludo:
        st.write(tf.saludar(nombre))
def pagina2():
    st.title("Suma de dos números")
    st.header("Ingrese Los Números")
    num1 = st.number_input("Ingrese el valor del primer número:")
    num2 = st.number_input("Ingrese el valor del segundo número número:")
    calcular = st.button("Sumar")
    if calcular:
        st.write(f"La suma de {num1} y {num2}, es igual a: {tf.sumar(num1,num2):.2f}")
def pagina3():
    st.title("Calcular Área de Un Triangulo")
    base = st.number_input("Ingrese el Valor de la Base del Triangulo:")
    altura =  st.number_input("Ingrese el Valor de la Altura del Triangulo:",step=1)
    calcular = st.button("Calcular Área")
    if calcular:
        st.write(f"El Área del Triangulo es Igual a: {tf.calcular_area_triangulo(base, altura):.2f}")
def pagina4():
    st.title("Calculadora de Precio con Descuento")
    precio = st.number_input("Ingrese la Cantidad sin Descuento:")
    desc = st.number_input("Ingrese el Valor del Porcentaje de Descuento:",step=1)
    descuento = desc/100
    with st.expander("Seleccione país (Impuesto):",False):
        opcion = st.radio("País",(
            "Belice", 
            "Costa Rica", 
            "El Salvador", 
            "Guatemala", 
            "Honduras", 
            "México",
            "Nicaragua", 
            "Panamá",
            "Otro"
        ),None)
    match opcion:
        case "Belice":
            impuesto = .125
        case "Costa Rica":
            impuesto = .13
        case "El Salvador":
            impuesto = .13
        case "Guatemala":
            impuesto = .12
        case "Honduras":
            impuesto = .15
        case "México":
            impuesto = .16
        case "Nicaragua":
            impuesto = .15
        case "Panamá":
            impuesto =.07
        case "Otro":
            opcion = "País no especificado"
            tax = st.number_input("Ingrese el Valor de Impuesto Sobre Consumo En su País:",step=1)
            impuesto = tax / 100
    calcular = st.button("Calcular")
    if calcular:
        st.write(f"El Valor Final con Descuento de {desc}% e Impuesto a Consumo en {opcion} de {impuesto} es Igual a: {tf.calcular_precio_final(precio, impuesto, descuento):.2f}")
def pagina5():
    st.title("Suma de un Conjunto de Números")
    conjunto = st.text_input("Ingrese una Lista de Números Separados por Comas ',':")
    calcular = st.button("Sumar Conjunto")
    if conjunto:
        try:
            lista_nums = [float(num) for num in conjunto.split(",")]
            if calcular:
                st.write(f"La Suma de la Lista Ingresada es de: {tf.sumar_lista(lista_nums)}")
        except ValueError:
            st.error("Por Favor Ingrese los Números Separados por Comas.")
def pagina6():
    st.title("Precio de Productos")
    with st.expander("Lista de productos:",False):
        product = st.radio("Producto",(
            "🥤 CocaCola 300ml",
            "🍫Barra Chocolate Hershey 40g",
            "🍎 Manzana Roja",
            "🧃Jugo Jumex 300ml",
            "🍺 Cerveza Clara Corona Familiar 940ml",
            "🥡 Maruchan 64g"
        ),None)
    cantidad = st.number_input("Ingrese la Cantidad de Productos a Llevar:",min_value=0,max_value=99, step=1)
    match product:
        case "🥤 CocaCola 300ml":
            precio_unidad = 10
        case "🍫Barra Chocolate Hershey 40g":
            precio_unidad = 22
        case "🍎 Manzana Roja":
            precio_unidad = 12.50
        case "🧃Jugo Jumex 300ml":
            precio_unidad = 10.70
        case "🍺 Cerveza Clara Corona Familiar 940ml":
            precio_unidad = 47
        case "🥡 Maruchan 64g":
            precio_unidad = 15.50
    calcular = st.button("Calcular")
    if calcular:
        st.write(f"{tf.producto(product,cantidad, precio_unidad)}")
def pagina7():
    st.title("Calculadora de Pariedad")
    conjunto = st.text_input("Ingrese una Lista de Números Separados por Comas ',' :")
    calcular = st.button("Separar Pares e Impares")
    if conjunto:
        try:
            lista_nums = [float(num) for num in conjunto.split(",")]
            if calcular:
                pares = []
                impares = []
                pares, impares = tf.numeros_pares_e_impares(lista_nums)
                st.write(f"Los numeros pares son: {pares}.")
                st.write(f"Los números impares son: {impares}.")
        except ValueError:
                st.error("Por Favor Ingrese los Números Separados por Comas.")
def pagina8():
    st.title("Multiplicación")
    conjunto = st.text_input("Ingrese una Lista de Números Separados por Comas ',' :")
    calcular = st.button("Multiplicar")
    if conjunto:
        try:
            lista_nums = [float(num) for num in conjunto.split(",")]
            if calcular:
                st.write(f"La Multiplicación de Todos los Números es Igual a: {tf.multiplicar_todos(lista_nums)}")
        except ValueError:
                st.error("Por Favor Ingrese los Números Separados por Comas.")
def pagina9():
    st.title("Información Personal")
    diccionario_clave = st.text_input("Ingrese Los Elemetos a Tabular Separados por Comas ',' (Por ejemplo: Nombre, Edad, Etc...):")
    try:
        lista_clave = [str(i)for i in diccionario_clave.split(",")]
    except ValueError:
        st.error("Por Favor Ingrese los Parametros Separados por Comas.")
    if lista_clave:
        lista_valor = []
        for i in lista_clave:
            valor = st.text_input(f"Ingrese el Valor del Parametro {i}:")
            if valor:
                lista_valor.append(valor)
            else:
                st.warning(f"Por Favor Ingrese un Valor para '{i}'.")
            
            
        diccionario_info = dict(zip(lista_clave,lista_valor))
        
        tabular = st.button("Hacer Tabla")
        if tabular:
            df=tf.informacion_personal(**diccionario_info) 
            st.dataframe(df)
def pagina10():
    st.title("Calculadora Felxible")
    st.header("Operqaciones con dos números")
    num1 = st.number_input("Ingrese el valor del primer número:")
    num2 = st.number_input("Ingrese el valor del segundo número:")
    with st.expander("Seleccione Operación:",False):
        operacion = st.radio("Operación",(
            "Suma",
            "Resta",
            "Multiplicación",
            "División"
        ), None)
    calcular = st.button("Calcular")
    if calcular:
        st.write(f"La {operacion} de {num1} y {num2} es Igual a: {tf.calculadora_flexible(num1,num2,operacion):.2f}")


def main():         
    with st.sidebar:
        st.title("Menú de opciones")
        opcion = st.sidebar.radio(
            "Aplicaciones:",(
                "Saluda A Un Colega!",
                "Suma de Dos Números",
                "Calcular Área de un Triangulo",
                "Calculadora de Descuentos",
                "Suma de un Conjunto de Numeros",
                "Precio de Productos",
                "Calculadora de Pariedad",
                "Multiplicación",
                "Información Personal",
                "Calculadora Flexible"
                ),None
            )               
        with st.expander("FAQs",False):
            st.page_link(GitHubUsage,label="¿Como Usar Las Apliciones?")
            st.page_link(GitHubTech, label="¿Como Funciona La Página?")
    
    match opcion:
        case "Saluda A Un Colega!":
            pagina1()
        case "Suma de Dos Números":
            pagina2()
        case "Calcular Área de un Triangulo":
            pagina3()
        case "Calculadora de Descuentos":
            pagina4()
        case "Suma de un Conjunto de Numeros":
            pagina5()
        case "Precio de Productos":
            pagina6()
        case "Calculadora de Pariedad":
            pagina7()
        case "Multiplicación":
            pagina8()
        case "Información Personal":
            pagina9()
        case "Calculadora Flexible":
            pagina10()
        case _:
            pagina0()
            

if __name__ == "__main__":
    main()
