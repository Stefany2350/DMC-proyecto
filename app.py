import streamlit as st
import numpy as np
import libreria_funciones_proyecto1 as lf
import librería_clases_proyecto1 as lc

st.title("Titulo del proyecto") 
st.sidebar.title("Parámetros")

st.sidebar.image("DMC.png")

modulos = st.sidebar.selectbox("Selecione la sección a consultar",["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

if modulos == "Home":

   st.subheader("Módulo: Python Fundamentals")

    st.write("Nombre: Stefany Salazar Espinoza")
    
    st.write("Año: 2026")

    st.markdown("""
    ### Descripción

    El presente proyecto tiene como objetivo aplicar los conocimientos
    adquiridos en el módulo **Python Fundamentals**, desarrollando
    diferentes ejercicios mediante el uso de Python y Streamlit.

    ### Tecnologías utilizadas

    - **Python**
    - **Streamlit**
    - **NumPy**
    - **GitHub**
    """)

    st.image("Python_logo.png", width=300)
  

"""if modulos == "Listas":
  st.write("Te encuentras en el módulo de listas")

  valor_inicial = int(st.number_input("Ingresa tu valor inicial del rango", value=0))
  valor_final = int(st.number_input("Ingresa tu valor final del rango",value=10))

  lista = list(range(valor_inicial, valor_final))

  st.write(lista) """

""" elif modulos == "Arreglos":
  st.write("Te encuentras en el módulo de arreglos")

  cantidad = st.slider("Seleccione un valor del rango", min_value = 1, max_value = 100, value=20 )
  arreglo = np.arange(cantidad)

  st.write(arreglo)


elif modulos == "Funciones":
  st.write("Te encuentras en el módulo de Funciones")
  capital_i = st.number_input("Ingrese el capital inicial", min_value = 0 , max_value = 100000, value=1000)
  aporte_m = st.number_input("Ingrese el aporte mensual", min_value = 0 , max_value = 10000, value=100)
  tasa_a = st.slider("Ingrese el aporte mensual", min_value = 0.01 , max_value = 1.00, value=0.05)
  anios = st.slider("Ingrese el aporte mensual", min_value = 1 , max_value = 20, value=2)

  resultado_valor_futuro = lf.valor_futuro_inversion(capital_i ,aporte_m,tasa_a,anios)
  st.write("El resultados de tu valor futuro de inversión es: ",round(resultado_valor_futuro,2))
  
else:
  st.write("Te encuentras en el módulo de POO")  """
  
