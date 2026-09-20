import streamlit as st
import numpy as np
import libreria_funciones_proyecto1 as lf
import librería_clases_proyecto1 as lc

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================

st.set_page_config(
    page_title="Gestión y Análisis de Datos - Python Fundamentals",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ESTILOS CSS
# ==========================================

st.markdown("""
    <style>

    /* ==========================================
       FONDO GENERAL
       ========================================== */

    .stApp {
        background-color: #1E293B;
        color: #F8FAFC;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }


    /* ==========================================
       BARRA LATERAL
       ========================================== */

    [data-testid="stSidebar"] {
        background-color: #334155;
        border-right: 1px solid #475569;
    }

    [data-testid="stSidebar"] .stMarkdown h1,
    [data-testid="stSidebar"] .stMarkdown h2,
    [data-testid="stSidebar"] .stMarkdown h3 {
        color: #38BDF8;
    }


    /* ==========================================
       TÍTULO DEL PANEL DE NAVEGACIÓN
       MISMO GRADIENTE QUE LOS TÍTULOS PRINCIPALES
       ========================================== */

    .sidebar-custom-title {

        background: linear-gradient(
            135deg,
            #0F172A 0%,
            #1D4ED8 35%,
            #2563EB 55%,
            #38BDF8 75%,
            #0F172A 100%
        ) !important;

        background-size: 250% 250% !important;

        border: 1px solid #475569 !important;

        border-left: 6px solid #38BDF8 !important;

        padding: 16px 20px !important;

        border-radius: 10px !important;

        box-shadow:
            0 10px 30px rgba(0, 0, 0, 0.5),
            0 0 20px rgba(37, 99, 235, 0.15) !important;

        position: relative !important;

        overflow: hidden !important;

        margin-bottom: 20px !important;

        animation:
            tituloGradient 6s ease infinite !important;
    }


    .sidebar-custom-title h2 {

        color: #F8FAFC !important;

        font-size: 1.25rem !important;

        font-weight: 700 !important;

        margin: 0 !important;

        text-shadow:
            0 2px 8px rgba(0, 0, 0, 0.35) !important;
    }


    /* ==========================================
       TÍTULOS PRINCIPALES
       ========================================== */

    .custom-data-title {

        background: linear-gradient(
            135deg,
            #0F172A 0%,
            #1D4ED8 35%,
            #2563EB 55%,
            #38BDF8 75%,
            #0F172A 100%
        ) !important;

        background-size: 250% 250% !important;

        border: 1px solid #475569 !important;

        border-left: 6px solid #38BDF8 !important;

        padding: 24px 30px !important;

        border-radius: 14px !important;

        box-shadow:
            0 10px 30px rgba(0, 0, 0, 0.5),
            0 0 20px rgba(37, 99, 235, 0.15) !important;

        margin-bottom: 30px !important;

        position: relative !important;

        overflow: hidden !important;

        animation:
            tituloGradient 6s ease infinite !important;
    }


    /* ==========================================
       ANIMACIÓN DEL GRADIENTE
       ========================================== */

    @keyframes tituloGradient {

        0% {
            background-position: 0% 50%;
        }

        50% {
            background-position: 100% 50%;
        }

        100% {
            background-position: 0% 50%;
        }

    }


    /* ==========================================
       TEXTO DE LOS TÍTULOS
       ========================================== */

    .custom-data-title h1 {

        color: #F8FAFC !important;

        font-size: 2.1rem !important;

        font-weight: 700 !important;

        margin: 0 !important;

        position: relative !important;

        z-index: 2 !important;

        text-shadow:
            0 2px 8px rgba(0, 0, 0, 0.35) !important;
    }


    .custom-data-title p {

        color: #E2E8F0 !important;

        font-size: 0.95rem !important;

        margin: 6px 0 0 0 !important;
    }


    /* ==========================================
       BOTONES
       ========================================== */

    .stButton > button {

        background: linear-gradient(
            135deg,
            #2563EB 0%,
            #1D4ED8 100%
        );

        color: white;

        border: none;

        border-radius: 8px;

        padding: 0.6rem 1.2rem;

        font-weight: 600;

        box-shadow:
            0 4px 12px rgba(37, 99, 235, 0.3);

        transition: all 0.3s ease;
    }


    .stButton > button:hover {

        background: linear-gradient(
            135deg,
            #3B82F6 0%,
            #2563EB 100%
        );

        box-shadow:
            0 0 20px rgba(59, 130, 246, 0.6);

        transform: translateY(-2px);
    }


    /* ==========================================
       CAMPOS DE ENTRADA
       ========================================== */

    .stTextInput input,
    .stSelectbox select,
    .stNumberInput input {

        background-color: #0F172A !important;

        color: #F8FAFC !important;

        border: 1px solid #475569 !important;

        border-radius: 8px !important;
    }


    /* ==========================================
       MÉTRICAS
       ========================================== */

    [data-testid="stMetric"] {

        background-color: #0F172A;

        padding: 15px;

        border-radius: 12px;

        border: 1px solid #475569;

        box-shadow:
            0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }


    [data-testid="stMetricLabel"] {

        color: #94A3B8 !important;
    }


    [data-testid="stMetricValue"] {

        color: #38BDF8 !important;
    }


    /* ==========================================
       TABLAS
       ========================================== */

    [data-testid="stDataFrame"] {

        border-radius: 10px;

        overflow: hidden;

        border: 1px solid #475569;
    }

    </style>
""", unsafe_allow_html=True)


# ==========================================
# BARRA LATERAL
# ==========================================

st.sidebar.markdown("""
    <div class="sidebar-custom-title">
        <h2>🎛️ Panel de Navegación</h2>
    </div>
""", unsafe_allow_html=True)


modulos = st.sidebar.selectbox(
    "Seleccione la sección a consultar",
    [
        "Home",
        "Ejercicio 1",
        "Ejercicio 2",
        "Ejercicio 3",
        "Ejercicio 4"
    ]
)


# ==========================================
# HOME
# ==========================================

if modulos == "Home":

    st.sidebar.markdown("---")

    st.sidebar.image(
        "image_home.png",
        use_container_width=True
    )

    st.markdown("""
        <div class="custom-data-title">
            <h1>Aplicación de Python para la Gestión y Análisis de Datos</h1>
        </div>
    """, unsafe_allow_html=True)


    col_info1, col_info2, col_info3 = st.columns(3)

    with col_info1:
        st.write("**Módulo:** Python Fundamentals")

    with col_info2:
        st.write("**Estudiante:** Stefany Salazar Espinoza")

    with col_info3:
        st.write("**Año:** 2026")


    st.markdown("---")


    st.markdown("""
    ### 💡 Descripción del Proyecto

    El presente proyecto tiene como objetivo aplicar los conocimientos
    adquiridos en el módulo **Python Fundamentals**, mediante el desarrollo
    de diferentes ejercicios utilizando estructuras de datos, funciones,
    clases y una interfaz interactiva desarrollada con Streamlit.

    ### 🛠️ Tecnologías utilizadas

    - **Python**
    - **Streamlit**
    - **NumPy**
    - **GitHub**
    """)


    st.image(
        "Python_logo.png",
        width=250
    )


# ==========================================
# EJERCICIO 1 - FLUJO DE CAJA
# ==========================================

elif modulos == "Ejercicio 1":

    st.sidebar.markdown("---")

    st.sidebar.image(
        "image_ejercicio1.jpg",
        use_container_width=True
    )


    st.markdown("""
        <div class="custom-data-title">
            <h1>💰 Flujo de caja con listas</h1>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    ### Descripción del ejercicio

    En este ejercicio se desarrolla un módulo para registrar movimientos
    financieros utilizando **listas**.

    Cada movimiento contiene un concepto, un tipo de movimiento y un valor.
    La aplicación permite calcular los ingresos, gastos y el saldo final.
    """)


    st.markdown("---")

    st.subheader("Registrar movimiento")


    concepto = st.text_input(
        "Ingrese el concepto del movimiento"
    )


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
                "Concepto": concepto,
                "Tipo": tipo,
                "Valor": valor
            }

            st.session_state.movimientos.append(
                movimiento
            )

            st.success(
                "Movimiento registrado correctamente."
            )

        else:

            st.error(
                "Ingrese un concepto válido y un valor mayor que 0."
            )


    st.markdown("---")

    st.subheader("Movimientos registrados")


    if len(st.session_state.movimientos) > 0:

        col1, col2, col3, col4 = st.columns(
            [3, 2, 2, 1]
        )

        col1.markdown("**Concepto**")
        col2.markdown("**Tipo**")
        col3.markdown("**Valor**")
        col4.markdown("**Eliminar**")


        for i, movimiento in enumerate(
            st.session_state.movimientos
        ):

            col1, col2, col3, col4 = st.columns(
                [3, 2, 2, 1]
            )

            col1.write(
                movimiento["Concepto"]
            )

            col2.write(
                movimiento["Tipo"]
            )

            col3.write(
                f"S/ {movimiento['Valor']:,.2f}"
            )


            if col4.button(
                "🗑️",
                key=f"eliminar_movimiento_{i}"
            ):

                st.session_state.movimientos.pop(i)

                st.rerun()


        total_ingresos = sum(
            movimiento["Valor"]
            for movimiento in st.session_state.movimientos
            if movimiento["Tipo"] == "Ingreso"
        )


        total_gastos = sum(
            movimiento["Valor"]
            for movimiento in st.session_state.movimientos
            if movimiento["Tipo"] == "Gasto"
        )


        saldo_final = (
            total_ingresos - total_gastos
        )


        st.markdown("---")

        st.subheader(
            "Resumen del flujo de caja"
        )


        col_m1, col_m2, col_m3 = st.columns(3)


        col_m1.metric(
            "Total de ingresos",
            f"S/ {total_ingresos:,.2f}"
        )


        col_m2.metric(
            "Total de gastos",
            f"S/ {total_gastos:,.2f}"
        )


        col_m3.metric(
            "Saldo final",
            f"S/ {saldo_final:,.2f}"
        )


        if saldo_final > 0:

            st.success(
                "Flujo de caja: A FAVOR 📈"
            )

        elif saldo_final < 0:

            st.error(
                "Flujo de caja: EN CONTRA 📉"
            )

        else:

            st.info(
                "Flujo de caja: EN EQUILIBRIO ⚖️"
            )


        st.markdown("---")


        if st.button(
            "Borrar todos los movimientos"
        ):

            st.session_state.movimientos = []

            st.rerun()


    else:

        st.write(
            "No hay movimientos registrados."
        )


# ==========================================
# EJERCICIO 2 - REGISTRO DE PRODUCTOS
# ==========================================

elif modulos == "Ejercicio 2":

    st.sidebar.markdown("---")

    st.sidebar.image(
        "image_ejercicio2.jpg",
        use_container_width=True
    )


    st.markdown("""
        <div class="custom-data-title">
            <h1>📦 Formulario de registro de ventas</h1>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    ### Descripción del ejercicio

    En este ejercicio se desarrolla un formulario para registrar ventas
    utilizando **arreglos de NumPy**.

    El total se calcula automáticamente multiplicando el precio por
    la cantidad.
    """)


    st.markdown("---")

    st.subheader("Registrar producto")


    nombre = st.text_input(
        "Ingrese el nombre del producto"
    )


    categoria = st.selectbox(
        "Seleccione la categoría",
        [
            "Limpieza",
            "Tecnología",
            "Alimentos",
            "Bebidas",
            "Otros"
        ]
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


    if "productos" not in st.session_state:

        st.session_state.productos = np.empty(
            (0, 5),
            dtype=object
        )


    if st.button("Registrar producto"):

        if nombre != "" and precio > 0:

            total = precio * cantidad

            nuevo_producto = np.array(
                [[
                    nombre,
                    categoria,
                    precio,
                    cantidad,
                    total
                ]],
                dtype=object
            )


            st.session_state.productos = np.vstack(
                [
                    st.session_state.productos,
                    nuevo_producto
                ]
            )


            st.success(
                "Producto registrado correctamente."
            )

        else:

            st.error(
                "Ingrese un nombre válido y un precio mayor que 0."
            )


    st.markdown("---")

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
            hide_index=True,
            use_container_width=True
        )


        st.markdown("---")

        st.subheader("Eliminar producto")


        nombres_productos = [
            producto[0]
            for producto in st.session_state.productos
        ]


        producto_seleccionado = st.selectbox(
            "Seleccione el producto que desea eliminar",
            nombres_productos
        )


        col_elim1, col_elim2 = st.columns(2)


        with col_elim1:

            if st.button(
                "Eliminar producto seleccionado"
            ):

                indice = nombres_productos.index(
                    producto_seleccionado
                )


                st.session_state.productos = np.delete(
                    st.session_state.productos,
                    indice,
                    axis=0
                )


                st.rerun()


        with col_elim2:

            if st.button(
                "Borrar todo el inventario"
            ):

                st.session_state.productos = np.empty(
                    (0, 5),
                    dtype=object
                )

                st.rerun()


    else:

        st.write(
            "No hay productos registrados."
        )


# ==========================================
# EJERCICIO 3 - TASA DE ERROR
# ==========================================

elif modulos == "Ejercicio 3":

    st.sidebar.markdown("---")

    st.sidebar.image(
        "image_ejercicio3.jpg",
        use_container_width=True
    )


    st.markdown("""
        <div class="custom-data-title">
            <h1>📊 Cálculo de tasa de error de transacciones</h1>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    ### Descripción del ejercicio

    En este ejercicio se utilizará una función desde una librería externa
    para calcular la **tasa de error** y la **tasa de éxito** de un conjunto
    de transacciones.

    La función recibe como parámetros el número de transacciones fallidas
    y el número de transacciones totales.
    """)


    st.markdown("---")

    st.subheader("Seleccionar función")


    funcion = st.selectbox(
        "Seleccione la función que desea ejecutar",
        [
            "Calcular tasa de error de transacciones"
        ]
    )


    if funcion == "Calcular tasa de error de transacciones":

        st.subheader("Ingresar parámetros")


        periodo = st.text_input(
            "Ingrese el periodo del análisis"
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

            if periodo == "":

                st.write(
                    "Debe ingresar el periodo del análisis."
                )

            else:

                try:

                    resultado = (
                        lf.calcular_tasa_error_transacciones(
                            transacciones_fallidas,
                            transacciones_totales
                        )
                    )


                    st.write(
                        "Función ejecutada correctamente."
                    )


                    st.subheader(
                        f"Resultado - {periodo}"
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
                        "Periodo": periodo,
                        "Transacciones fallidas": transacciones_fallidas,
                        "Transacciones totales": transacciones_totales,
                        "Tasa de error (%)": resultado[
                            "tasa_error_pct"
                        ],
                        "Tasa de éxito (%)": resultado[
                            "tasa_exito_pct"
                        ]
                    }


                    st.session_state.historico_tasa_error.append(
                        registro
                    )


                except ValueError as e:

                    st.write(str(e))


    st.markdown("---")

    st.subheader("Histórico de resultados")


    if (
        "historico_tasa_error" in st.session_state
        and len(
            st.session_state.historico_tasa_error
        ) > 0
    ):

        st.dataframe(
            st.session_state.historico_tasa_error,
            use_container_width=True
        )


        if st.button(
            "Eliminar todos los registros"
        ):

            st.session_state.historico_tasa_error = []

            st.rerun()


    else:

        st.write(
            "No hay resultados registrados."
        )


# ==========================================
# EJERCICIO 4 - GESTIÓN DE PACIENTES
# ==========================================

elif modulos == "Ejercicio 4":

    st.sidebar.markdown("---")

    st.sidebar.image(
        "image_ejercicio4.jpg",
        use_container_width=True
    )


    st.markdown("""
        <div class="custom-data-title">
            <h1>🏥 Gestión de pacientes</h1>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    ### Descripción del ejercicio

    En este ejercicio se utilizará la clase **Paciente**, almacenada
    en la librería externa `libreria_clases_proyecto1.py`.

    La aplicación implementa las operaciones básicas de un CRUD:

    - **Crear** registros.
    - **Leer** y visualizar registros.
    - **Actualizar** información.
    - **Eliminar** registros.

    La clase permite calcular el IMC, su clasificación y la superficie
    corporal.
    """)


    if "pacientes" not in st.session_state:

        st.session_state.pacientes = []


    st.markdown("---")

    st.subheader("Seleccionar clase")


    clase = st.selectbox(
        "Seleccione la clase que desea utilizar",
        ["Paciente"]
    )


    if clase == "Paciente":

        # ======================================
        # CREAR
        # ======================================

        st.subheader("Crear registro")


        nombre_p = st.text_input(
            "Ingrese el nombre del paciente"
        )


        peso_p = st.number_input(
            "Ingrese el peso en kg",
            min_value=0.1,
            value=60.0,
            step=0.1
        )


        altura_p = st.number_input(
            "Ingrese la altura en metros",
            min_value=0.1,
            value=1.60,
            step=0.01
        )


        if st.button("Crear paciente"):

            if nombre_p == "":

                st.write(
                    "Debe ingresar el nombre del paciente."
                )

            else:

                try:

                    paciente = lc.Paciente(
                        nombre_p,
                        peso_p,
                        altura_p
                    )


                    st.session_state.pacientes.append(
                        paciente
                    )


                    st.write(
                        "Paciente registrado correctamente."
                    )


                except ValueError as e:

                    st.write(str(e))


        # ======================================
        # LEER
        # ======================================

        st.markdown("---")

        st.subheader("Registros de pacientes")


        if len(st.session_state.pacientes) > 0:

            registros = []


            for paciente in st.session_state.pacientes:

                registros.append(
                    paciente.resumen()
                )


            st.dataframe(
                registros,
                use_container_width=True,
                hide_index=True
            )


        else:

            st.write(
                "No hay pacientes registrados."
            )


        # ======================================
        # ACTUALIZAR
        # ======================================

        if len(st.session_state.pacientes) > 0:

            st.markdown("---")

            st.subheader("Actualizar paciente")


            nombres = [
                paciente.nombre
                for paciente in st.session_state.pacientes
            ]


            paciente_actualizar = st.selectbox(
                "Seleccione el paciente que desea actualizar",
                nombres,
                key="paciente_actualizar"
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


            if st.button(
                "Actualizar paciente"
            ):

                indice = nombres.index(
                    paciente_actualizar
                )


                paciente = (
                    st.session_state.pacientes[indice]
                )


                paciente.peso_kg = nuevo_peso
                paciente.altura_m = nueva_altura


                st.rerun()


            # ======================================
            # ELIMINAR
            # ======================================

            st.markdown("---")

            st.subheader("Eliminar paciente")


            paciente_eliminar = st.selectbox(
                "Seleccione el paciente que desea eliminar",
                nombres,
                key="paciente_eliminar"
            )


            if st.button(
                "Eliminar paciente"
            ):

                indice = nombres.index(
                    paciente_eliminar
                )


                st.session_state.pacientes.pop(
                    indice
                )


                st.rerun()



















