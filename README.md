# Menú de Aplicaciones en Streamlit

Una manera interacrtiva de realizar calculos u otras operaciones con las distintas aplicaciones que ofrece la página.

[👑 Abrir en Streamlit](https://menu-aplicaciones-yeray-anguiano.streamlit.app/)

### Cómo correrlo desde tu maquina

1. Instala los requisitos

   ```
   $ pip install -r requirements.txt
   ```

2. Corre la app con streamlit

   ```
   $ streamlit run streamlit_app.py
   ```

# Para una explicación detallada técnica del codigo visite:
[🐈‍⬛Abrir en GitHub](https://github.com/YerayAnguiano/Funcionameinto-de-Menu-de-Opciones)

## Cómo Usarlo

Al ingresar a la página lo primero que se nos muestra es la pagina pricipal, y la sidebar de streamlit con el menú de aplicaciones.
Selecciona una aplicación haciendo click sobre del nombre de la app.

<img src= "images/menu_sin_seleccionar.png">
<img src= "images/menu_seleccionado.png">

## Saluda a un colega
En esta opción simplemente se debe agregar el nombre tuyo o de un colega en el apartado y seleccionar el botón saludar. que mostrará un saludo a tu colega.

<img src="images/saluda_colega.png">

## Suma de Dos Números
Esta opción suma dos numeros que debe ingresar solo escribiendolos en sus respectivos recuadros.

Al hacer click en el botón `Sumar`, se mostrará un mensaje con el resultado de la suma.

<img src="images/suma_dos_numeros.png">

## Calcular Área de un Triangulo
Esta aplicación consta de ingresar el valor de la base y altura de un triangulo. posteriormente al seleccionar el botón `Calcular Área` muestra un mensaje con el resultado de la operación.

<img src="images/area_triangulo.png">

## Calculadora de Descuentos
Ingrese el valor inicial en el apartado *Ingrese la Cantidad sin Descuento* y el valor del descuento en porcentaje en el apartado *Ingrese el Valor del Porcentaje del Descuento*.

<img src="images/precio_con_descuento.png">

Despues al seleccionar la opcion *Seleccione país (impuesto)*, se despliega una lista con paises y al seleccionar uno se establece el impuesto del país. En caso de que no se encuentre su país, seleccione la opcion `Otro` e ingrese el valor del porcentaje de impuesto en su país.

<img src="images/precio_con_descuento_tabla_paises.png">

## Suma de un Conjunto de Numeros
Esta aplicación solicita ingresar una lista de numeros separados por coma. Por ejemplo: *1,2,3,5,7*. 

<img src="images/suma_conjunto_de_numeros.png">

Despues de Ingresar los valores y hacer click al botón `Sumar Conjunto`, mostrará un mensaje con la suma de todos los numeros dentro de la lista.

