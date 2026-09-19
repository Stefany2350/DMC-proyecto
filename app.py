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

        # Encabezados de la tabla
        col1, col2, col3, col4 = st.columns([3, 2, 2, 1])

        col1.markdown("**Concepto**")
        col2.markdown("**Tipo**")
        col3.markdown("**Valor**")
        col4.markdown("**Eliminar**")

        # Mostrar cada movimiento
        for i, movimiento in enumerate(st.session_state.movimientos):

            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])

            col1.write(movimiento["concepto"])
            col2.write(movimiento["tipo"])
            col3.write(f"S/ {movimiento['valor']:,.2f}")

            if col4.button("🗑️", key=f"eliminar_{i}"):
                st.session_state.movimientos.pop(i)
                st.rerun()

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

        st.subheader("Eliminar todos los movimientos")

        if st.button("Borrar todos los movimientos"):
            st.session_state.movimientos = []
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
                1: "Nombre",
                2: "Categoría",
                3: st.column_config.NumberColumn(
                    "Precio",
                    format="S/ %.2f"
                ),
                4: "Cantidad",
                5: st.column_config.NumberColumn(
                    "Total",
                    format="S/ %.2f"
                )
            },
            hide_index=True
        )

        # Eliminar producto
        st.subheader("Eliminar producto")

        nombres_productos = []

        for producto in st.session_state.productos:
            nombres_productos.append(producto[0])

        producto_seleccionado = st.selectbox(
            "Seleccione el producto que desea eliminar",
            nombres_productos
        )

        if st.button("Eliminar producto"):

            indice = nombres_productos.index(producto_seleccionado)

            st.session_state.productos = np.delete(
                st.session_state.productos,
                indice,
                axis=0
            )

            st.success("Producto eliminado correctamente")

            st.rerun()

        st.subheader("Eliminar todos los registros")

        if st.button("Borrar todos los productos"):

            st.session_state.productos = np.empty((0, 5), dtype=object)

            st.success("Todos los productos fueron eliminados.")

            st.rerun()

    else:
        st.write("No hay productos registrados.")

##################################################################################################################################

elif modulos == "Ejercicio 3":

    st.title("Cálculo de tasa de error de transacciones")

    st.markdown("""
    ### Descripción del ejercicio

    En este ejercicio se utilizará una función desde una librería externa.
    Se utilizará una función relacionada con el análisis de transacciones
    para calcular la tasa de error y la tasa de éxito.

    La función recibe como parámetros el número de transacciones fallidas
    y el número de transacciones totales.
    """)

    st.subheader("Seleccionar función")

    funcion = st.selectbox(
        "Seleccione la función que desea ejecutar",
        ["Calcular tasa de error de transacciones"]
    )

    if funcion == "Calcular tasa de error de transacciones":

        st.subheader("Ingresar parámetros")

        nombre_analisis = st.text_input(
            "Ingrese periodo del análisis"
        )

        transacciones_fallidas = st.number_input(
            "Número de transacciones fallidas",
            min_value=0,
            value=0,
            step=1
        )

        transacciones_totales = st.number_input(
            "Número de transacciones totales",
            min_value=1,
            value=1,
            step=1
        )

        if st.button("Ejecutar función"):

            if nombre_analisis == "":
                st.write("Ingrese periodo del análisis")

            else:

                try:

                    resultado = lf.calcular_tasa_error_transacciones(
                        transacciones_fallidas,
                        transacciones_totales
                    )

                    st.write("Función ejecutada correctamente.")

                    st.subheader("Resultado")

                    st.write(
                        f"Periodo del análisis: {nombre_analisis}"
                    )

                    st.write(
                        f"Tasa de error: "
                        f"{resultado['tasa_error_pct']:.4f}%"
                    )

                    st.write(
                        f"Tasa de éxito: "
                        f"{resultado['tasa_exito_pct']:.4f}%"
                    )

                    if "historico_tasa_error" not in st.session_state:
                        st.session_state.historico_tasa_error = []

                    registro = {
                        "Análisis": nombre_analisis,
                        "Transacciones fallidas": transacciones_fallidas,
                        "Transacciones totales": transacciones_totales,
                        "Tasa de error (%)": resultado["tasa_error_pct"],
                        "Tasa de éxito (%)": resultado["tasa_exito_pct"]
                    }

                    st.session_state.historico_tasa_error.append(registro)

                except ValueError as e:

                    st.write(str(e))

    st.subheader("Histórico de resultados")

    if (
        "historico_tasa_error" in st.session_state
        and len(st.session_state.historico_tasa_error) > 0
    ):

        st.dataframe(
            st.session_state.historico_tasa_error,
            use_container_width=True
        )

        if st.button("Eliminar todos los registros"):
            st.session_state.historico_tasa_error = []
            st.rerun()

    else:

        st.write("No hay resultados registrados.")

###############################################################################################################################################
elif modulos == "Ejercicio 4":

    st.title("Gestión de pacientes")

    st.markdown("""
    ### Descripción del ejercicio

    En este ejercicio se utilizará la clase **Paciente**,
    almacenada en la librería externa `libreria_clases_proyecto1.py`, la cual
    permite registrar pacientes y realizar cálculos
    básicos como el **IMC**, su clasificación y la
    **superficie corporal**.

    Se implementarán las operaciones básicas de un CRUD:

    - Crear
    - Leer
    - Actualizar
    - Eliminar
    """)

    st.subheader("Seleccionar clase")

    clase = st.selectbox(
        "Seleccione la clase que desea utilizar",
        ["Paciente"]
    )

    if clase == "Paciente":

        if "pacientes" not in st.session_state:
            st.session_state.pacientes = []

        # CREAR
        st.subheader("Crear registro")

        nombre = st.text_input(
            "Ingrese el nombre del paciente"
        )

        peso = st.number_input(
            "Ingrese el peso en kg",
            min_value=0.1,
            value=60.0,
            step=0.1
        )

        altura = st.number_input(
            "Ingrese la altura en metros",
            min_value=0.1,
            value=1.60,
            step=0.01
        )

        if st.button("Crear paciente"):

            try:

                paciente = lc.Paciente(
                    nombre,
                    peso,
                    altura
                )

                st.session_state.pacientes.append(paciente)

                st.write("Paciente registrado correctamente.")

            except ValueError as e:

                st.write(str(e))

        # LEER
        st.subheader("Registros de pacientes")

        if len(st.session_state.pacientes) > 0:

            registros = []

            for paciente in st.session_state.pacientes:

                registros.append(
                    paciente.resumen()
                )

            st.dataframe(
                registros,
                use_container_width=True
            )

        else:

            st.write("No hay pacientes registrados.")

        # ACTUALIZAR
        st.subheader("Actualizar paciente")

        if len(st.session_state.pacientes) > 0:

            nombres = []

            for paciente in st.session_state.pacientes:
                nombres.append(paciente.nombre)

            paciente_actualizar = st.selectbox(
                "Seleccione el paciente que desea actualizar",
                nombres,
                key="actualizar_paciente"
            )

            nuevo_peso = st.number_input(
                "Nuevo peso en kg",
                min_value=0.1,
                value=60.0,
                step=0.1,
                key="nuevo_peso"
            )

            nueva_altura = st.number_input(
                "Nueva altura en metros",
                min_value=0.1,
                value=1.60,
                step=0.01,
                key="nueva_altura"
            )

            if st.button("Actualizar paciente"):

                indice = nombres.index(
                    paciente_actualizar
                )

                paciente = st.session_state.pacientes[indice]

                paciente.peso_kg = nuevo_peso
                paciente.altura_m = nueva_altura

                st.write(
                    "Paciente actualizado correctamente."
                )

                st.rerun()

        # ELIMINAR
        st.subheader("Eliminar paciente")

        if len(st.session_state.pacientes) > 0:

            nombres = []

            for paciente in st.session_state.pacientes:
                nombres.append(paciente.nombre)

            paciente_eliminar = st.selectbox(
                "Seleccione el paciente que desea eliminar",
                nombres,
                key="eliminar_paciente"
            )

            if st.button("Eliminar paciente"):

                indice = nombres.index(
                    paciente_eliminar
                )

                st.session_state.pacientes.pop(
                    indice
                )

                st.write(
                    "Paciente eliminado correctamente."
                )

                st.rerun()





















