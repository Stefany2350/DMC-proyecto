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
    adquiridos en el módulo **Python Fundamentals** permitiendo evidenciar el uso de estructuras
    de datos, widgets, funciones, clases y lógica de programación mediante la creaciòn de una interfaz interactiva.

    ### Tecnologías utilizadas

    - **Python**
    - **Streamlit**
    - **NumPy**
    - **GitHub**
    """)

   st.image("Python_logo.png", width=300)
  
elif modulos == "Ejercicio 1":

    st.title("Flujo de caja con listas")

    st.markdown("""
    ### Descripción del ejercicio

    En este ejercicio se desarrollará un pequeño módulo para registrar
    movimientos financieros utilizando una lista. Cada movimiento tendrá
    un **concepto**, un **tipo de movimiento** y un **valor**.

    La aplicación permitirá registrar ingresos y gastos, calcular el total
    de cada uno y determinar el **saldo final del flujo de caja**.
    """)

    st.subheader("Registrar movimiento")

    concepto = st.text_input("Ingrese el concepto del movimiento")

    tipo = st.selectbox(
        "Seleccione el tipo de movimiento",
        ["Ingreso", "Gasto"]
    )

    valor = st.number_input(
        "Ingrese el valor",
        min_value=0.0,
        value=0.0,
        step=10.0
    )

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    if st.button("Registrar movimiento"):

        if concepto != "" and valor > 0:

            movimiento = {
                "concepto": concepto,
                "tipo": tipo,
                "valor": valor
            }

            st.session_state.movimientos.append(movimiento)

            st.success("Movimiento registrado correctamente")

        else:
            st.error("Ingrese un concepto y un valor mayor que 0.")

    st.subheader("Movimientos registrados")

    if len(st.session_state.movimientos) > 0:

        st.dataframe(st.session_state.movimientos)

        total_ingresos = sum(
            movimiento["valor"]
            for movimiento in st.session_state.movimientos
            if movimiento["tipo"] == "Ingreso"
        )

        total_gastos = sum(
            movimiento["valor"]
            for movimiento in st.session_state.movimientos
            if movimiento["tipo"] == "Gasto"
        )

        saldo_final = total_ingresos - total_gastos

        st.subheader("Resumen del flujo de caja")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total de ingresos", f"S/ {total_ingresos:,.2f}")
        col2.metric("Total de gastos", f"S/ {total_gastos:,.2f}")
        col3.metric("Saldo final", f"S/ {saldo_final:,.2f}")

        if saldo_final > 0:
            st.success("Flujo de caja: A FAVOR")

        elif saldo_final < 0:
            st.error("Flujo de caja: EN CONTRA")

        else:
            st.info("Flujo de caja: EN EQUILIBRIO")

        st.subheader("Eliminar movimientos")

        if st.button("Borrar todos los movimientos"):
            st.session_state.movimientos = []
            st.success("Todos los movimientos fueron eliminados.")
            st.rerun()

    else:
        st.write("No hay movimientos registrados. Ingrese datos del movimiento.")


###############################################################################################################

elif modulos == "Ejercicio 2":

    st.title("Formulario de registro de productos")

    st.markdown("""
    ### Descripción del ejercicio

    En este ejercicio se desarrollará un formulario para registrar productos
    utilizando **arreglos de NumPy**.

    Cada registro tendrá un nombre, una categoría, un precio, una cantidad
    y un total calculado automáticamente.
    """)

    st.subheader("Registrar producto")

    nombre = st.text_input("Ingrese el nombre del producto")

    categoria = st.selectbox(
        "Seleccione la categoría",
        ["Limpieza", "Tecnología", "Alimentos", "Bebidas","Otros"]
    )

    precio = st.number_input(
        "Ingrese el precio",
        min_value=0.0,
        value=0.0,
        step=1.0
    )

    cantidad = st.number_input(
        "Ingrese la cantidad",
        min_value=1,
        value=1,
        step=1
    )

    # Crear arreglo NumPy vacío
    if "productos" not in st.session_state:
        st.session_state.productos = np.empty((0, 5), dtype=object)

    # Registrar producto
    if st.button("Registrar producto"):

        if nombre != "" and precio > 0 and cantidad > 0:

            total = precio * cantidad

            nuevo_producto = np.array(
                [[nombre, categoria, precio, cantidad, total]],
                dtype=object
            )

            st.session_state.productos = np.vstack(
                [st.session_state.productos, nuevo_producto]
            )

            st.success("Producto registrado correctamente")

        else:
            st.error("Ingrese un nombre y un precio mayor que 0.")

    # Mostrar productos
    st.subheader("Productos registrados")

    if len(st.session_state.productos) > 0:

        st.dataframe(
            st.session_state.productos,
            column_config={
                0: "Nombre",
                1: "Categoría",
                2: st.column_config.NumberColumn(
                    "Precio",
                    format="S/ %.2f"
                ),
                3: "Cantidad",
                4: st.column_config.NumberColumn(
                    "Total",
                    format="S/ %.2f"
                )
            },
            hide_index=True
        )

        # Eliminar producto
        st.subheader("Eliminar producto")

        opciones = []

        for i, producto in enumerate(st.session_state.productos):

            opciones.append(
                f"{i} - {producto[0]} - {producto[1]} - S/ {producto[4]:.2f}"
            )

        producto_seleccionado = st.selectbox(
            "Seleccione el producto que desea eliminar",
            opciones
        )

        if st.button("Eliminar producto"):

            indice = int(producto_seleccionado.split(" - ")[0])

            st.session_state.productos = np.delete(
                st.session_state.productos,
                indice,
                axis=0
            )

            st.success("Producto eliminado correctamente")

            st.rerun()

    else:
        st.write("No hay productos registrados.")





















 """elif modulos == "Funciones":
  st.write("Te encuentras en el módulo de Funciones")
  capital_i = st.number_input("Ingrese el capital inicial", min_value = 0 , max_value = 100000, value=1000)
  aporte_m = st.number_input("Ingrese el aporte mensual", min_value = 0 , max_value = 10000, value=100)
  tasa_a = st.slider("Ingrese el aporte mensual", min_value = 0.01 , max_value = 1.00, value=0.05)
  anios = st.slider("Ingrese el aporte mensual", min_value = 1 , max_value = 20, value=2)

  resultado_valor_futuro = lf.valor_futuro_inversion(capital_i ,aporte_m,tasa_a,anios)
  st.write("El resultados de tu valor futuro de inversión es: ",round(resultado_valor_futuro,2))
  
else:
  st.write("Te encuentras en el módulo de POO")  """
  
