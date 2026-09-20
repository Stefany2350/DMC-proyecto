import streamlit as st
import numpy as np
import libreria_funciones_proyecto1 as lf
import librería_clases_proyecto1 as lc


# ============================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Gestión y Análisis de Datos - Python Fundamentals",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# ESTILOS PERSONALIZADOS
# ============================================================

st.markdown("""
<style>

/* ==========================================================
   FONDO GENERAL
   ========================================================== */

.stApp {
    background-color: #1E293B;
    color: #F8FAFC;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}


/* ==========================================================
   BARRA LATERAL
   ========================================================== */

[data-testid="stSidebar"] {
    background-color: #334155;
    border-right: 1px solid #475569;
}

[data-testid="stSidebar"] .stMarkdown h1,
[data-testid="stSidebar"] .stMarkdown h2,
[data-testid="stSidebar"] .stMarkdown h3 {
    color: #38BDF8;
}


/* ==========================================================
   PANEL DE NAVEGACIÓN
   MISMO GRADIENTE QUE LOS TÍTULOS PRINCIPALES
   ========================================================== */

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

    border-left: 5px solid #38BDF8 !important;

    padding: 16px 20px !important;

    border-radius: 10px !important;

    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.5),
        0 0 20px rgba(37, 99, 235, 0.15) !important;

    position: relative !important;

    overflow: hidden !important;

    margin-bottom: 20px !important;

    animation: tituloGradient 6s ease infinite !important;
}


.sidebar-custom-title h2 {

    color: #F8FAFC !important;

    font-size: 1.25rem !important;

    font-weight: 700 !important;

    margin: 0 !important;

    text-shadow:
        0 2px 8px rgba(0, 0, 0, 0.35) !important;
}


/* ==========================================================
   TÍTULOS PRINCIPALES
   ========================================================== */

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

    animation: tituloGradient 6s ease infinite !important;
}


/* ==========================================================
   ANIMACIÓN DEL GRADIENTE
   ========================================================== */

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


/* ==========================================================
   TEXTO DE LOS TÍTULOS
   ========================================================== */

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


/* ==========================================================
   BOTONES
   ========================================================== */

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


/* ==========================================================
   CAMPOS DE ENTRADA
   ========================================================== */

.stTextInput input,
.stNumberInput input {

    background-color: #0F172A !important;

    color: #F8FAFC !important;

    border: 1px solid #475569 !important;

    border-radius: 8px !important;
}


/* ==========================================================
   SELECTBOX
   ========================================================== */

.stSelectbox > div > div {

    background-color: #0F172A !important;

    color: #F8FAFC !important;

    border-radius: 8px !important;

    border-color: #475569 !important;
}


/* ==========================================================
   MÉTRICAS
   ========================================================== */

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


/* ==========================================================
   DATAFRAMES
   ========================================================== */

[data-testid="stDataFrame"] {

    border-radius: 10px;

    overflow: hidden;

    border: 1px solid #475569;
}


/* ==========================================================
   SUBTÍTULOS
   ========================================================== */

h2, h3 {
    color: #E2E8F0 !important;
}


/* ==========================================================
   TEXTO
   ========================================================== */

p, label {
    color: #E2E8F0;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# PANEL DE NAVEGACIÓN
# ============================================================

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


# ============================================================
# HOME
# ============================================================

if modulos == "Home":

    st.markdown("""
        <div class="custom-data-title">
            <h1>Aplicación de Python para la Gestión y Análisis de Datos</h1>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("Información del proyecto")

    st.write("**Nombre:** Stefany Salazar Espinoza")
    st.write("**Módulo:** Python Fundamentals")
    st.write("**Año:** 2026")

    st.markdown("""
    ### Tecnologías utilizadas

    - 🐍 Python
    - 🎨 Streamlit
    - 🔢 NumPy
    - 🐙 GitHub
    """)


# ============================================================
# EJERCICIO 1
# FLUJO DE CAJA CON LISTAS
# ============================================================

elif modulos == "Ejercicio 1":

    st.markdown("""
        <div class="custom-data-title">
            <h1>Ejercicio 1 - Flujo de Caja con Listas</h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    En este ejercicio se registra un flujo de caja utilizando
    **listas de Python**, permitiendo registrar ingresos y gastos
    y calcular el saldo final.
    """)

    st.subheader("Registrar movimiento")

    concepto = st.text_input(
        "Concepto",
        placeholder="Ejemplo: Venta de producto"
    )

    tipo = st.selectbox(
        "Tipo de movimiento",
        ["Ingreso", "Gasto"]
    )

    valor = st.number_input(
        "Valor (S/)",
        min_value=0.0,
        value=0.0,
        step=10.0
    )


    # Crear lista en session_state
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []


    col1, col2 = st.columns(2)

    with col1:

        if st.button("Registrar movimiento"):

            if concepto.strip() == "":
                st.error("Ingrese un concepto.")

            elif valor <= 0:
                st.error("El valor debe ser mayor que 0.")

            else:

                movimiento = {
                    "Concepto": concepto,
                    "Tipo de movimiento": tipo,
                    "Valor": valor
                }

                st.session_state.movimientos.append(movimiento)

                st.success("Movimiento registrado correctamente.")


    with col2:

        if st.button("Eliminar último registro"):

            if len(st.session_state.movimientos) > 0:

                st.session_state.movimientos.pop()

                st.success("Último registro eliminado.")

            else:

                st.info("No existen registros para eliminar.")


    if st.button("Restablecer todos los movimientos"):

        st.session_state.movimientos = []

        st.success("Todos los movimientos fueron eliminados.")


    # ========================================================
    # MOSTRAR INFORMACIÓN
    # ========================================================

    if len(st.session_state.movimientos) > 0:

        st.subheader("Movimientos registrados")

        st.dataframe(
            st.session_state.movimientos,
            use_container_width=True
        )


        # Calcular totales

        total_ingresos = sum(
            movimiento["Valor"]
            for movimiento in st.session_state.movimientos
            if movimiento["Tipo de movimiento"] == "Ingreso"
        )


        total_gastos = sum(
            movimiento["Valor"]
            for movimiento in st.session_state.movimientos
            if movimiento["Tipo de movimiento"] == "Gasto"
        )


        saldo_final = total_ingresos - total_gastos


        # ====================================================
        # MÉTRICAS
        # ====================================================

        col1, col2, col3 = st.columns(3)


        with col1:
            st.metric(
                "Total ingresos",
                f"S/ {total_ingresos:,.2f}"
            )


        with col2:
            st.metric(
                "Total gastos",
                f"S/ {total_gastos:,.2f}"
            )


        with col3:
            st.metric(
                "Saldo final",
                f"S/ {saldo_final:,.2f}"
            )


        # ====================================================
        # ESTADO
        # ====================================================

        if saldo_final > 0:

            st.success(
                f"Estado: A FAVOR | Saldo disponible: "
                f"S/ {saldo_final:,.2f}"
            )

        elif saldo_final < 0:

            st.error(
                f"Estado: EN CONTRA | Déficit: "
                f"S/ {abs(saldo_final):,.2f}"
            )

        else:

            st.info(
                "Estado: EN EQUILIBRIO | "
                "Los ingresos y gastos son iguales."
            )

    else:

        st.info(
            "No hay movimientos registrados. "
            "Ingrese datos del movimiento."
        )


# ============================================================
# EJERCICIO 2
# REGISTRO DE PRODUCTOS CON NUMPY
# ============================================================

elif modulos == "Ejercicio 2":

    st.markdown("""
        <div class="custom-data-title">
            <h1>Ejercicio 2 - Formulario de Registro de Productos</h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    En este ejercicio se utilizan **arreglos de NumPy** para
    registrar productos, calcular automáticamente el total de
    cada operación y visualizar los registros.
    """)


    st.subheader("Registrar producto")


    nombre_producto = st.text_input(
        "Nombre del producto",
        placeholder="Ejemplo: Laptop"
    )


    categoria = st.selectbox(
        "Categoría",
        [
            "Tecnología",
            "Hogar",
            "Oficina",
            "Alimentos",
            "Otros"
        ]
    )


    precio = st.number_input(
        "Precio unitario (S/)",
        min_value=0.0,
        value=0.0,
        step=10.0
    )


    cantidad = st.number_input(
        "Cantidad",
        min_value=1,
        value=1,
        step=1
    )


    total = precio * cantidad


    st.metric(
        "Total calculado",
        f"S/ {total:,.2f}"
    )


    # ========================================================
    # SESSION STATE
    # ========================================================

    if "productos" not in st.session_state:

        st.session_state.productos = np.empty(
            (0, 5),
            dtype=object
        )


    col1, col2 = st.columns(2)


    with col1:

        if st.button("Registrar producto"):

            if nombre_producto.strip() == "":

                st.error("Ingrese el nombre del producto.")

            elif precio <= 0:

                st.error("El precio debe ser mayor que 0.")

            else:

                nuevo_producto = np.array(
                    [[
                        nombre_producto,
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


    with col2:

        if st.button("Eliminar último producto"):

            if len(st.session_state.productos) > 0:

                st.session_state.productos = (
                    st.session_state.productos[:-1]
                )

                st.success(
                    "Último producto eliminado."
                )

            else:

                st.info(
                    "No existen productos para eliminar."
                )


    if st.button("Restablecer inventario"):

        st.session_state.productos = np.empty(
            (0, 5),
            dtype=object
        )

        st.success(
            "Todos los productos fueron eliminados."
        )


    # ========================================================
    # MOSTRAR PRODUCTOS
    # ========================================================

    if len(st.session_state.productos) > 0:

        st.subheader("Productos registrados")


        columnas = [
            "Producto",
            "Categoría",
            "Precio unitario",
            "Cantidad",
            "Total"
        ]


        st.dataframe(
            st.session_state.productos,
            column_config={
                "0": "Producto",
                "1": "Categoría",
                "2": "Precio unitario",
                "3": "Cantidad",
                "4": "Total"
            },
            use_container_width=True
        )


        total_ventas = sum(
            float(fila[4])
            for fila in st.session_state.productos
        )


        st.metric(
            "Total registrado",
            f"S/ {total_ventas:,.2f}"
        )

    else:

        st.info(
            "No hay productos registrados."
        )


# ============================================================
# EJERCICIO 3
# FUNCIÓN EXTERNA
# ============================================================

elif modulos == "Ejercicio 3":

    st.markdown("""
        <div class="custom-data-title">
            <h1>Ejercicio 3 - Cálculo de Tasa de Error</h1>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    En este ejercicio se utiliza una función externa desarrollada
    en el módulo **libreria_funciones_proyecto1** para calcular
    la tasa de error de las transacciones.
    """)


    st.subheader("Datos de las transacciones")


    periodo = st.text_input(
        "Periodo",
        placeholder="Ejemplo: Enero 2026"
    )


    total_transacciones = st.number_input(
        "Total de transacciones",
        min_value=0,
        value=0,
        step=1
    )


    transacciones_fallidas = st.number_input(
        "Transacciones fallidas",
        min_value=0,
        value=0,
        step=1
    )


    if "historial_tasas" not in st.session_state:

        st.session_state.historial_tasas = []


    col1, col2 = st.columns(2)


    with col1:

        if st.button("Calcular tasa"):

            if periodo.strip() == "":

                st.error(
                    "Ingrese el periodo."
                )

            elif total_transacciones <= 0:

                st.error(
                    "El total de transacciones debe ser mayor que 0."
                )

            elif transacciones_fallidas > total_transacciones:

                st.error(
                    "Las transacciones fallidas no pueden superar "
                    "el total de transacciones."
                )

            else:

                resultado = lf.calcular_tasa_error_transacciones(
                    transacciones_fallidas,
                    total_transacciones
                )

                tasa_error = resultado

                tasa_exito = 100 - tasa_error


                registro = {
                    "Periodo": periodo,
                    "Total transacciones": total_transacciones,
                    "Transacciones fallidas": transacciones_fallidas,
                    "Tasa de error (%)": tasa_error,
                    "Tasa de éxito (%)": tasa_exito
                }


                st.session_state.historial_tasas.append(
                    registro
                )


                st.success(
                    "Tasa calculada correctamente."
                )


    with col2:

        if st.button("Limpiar historial"):

            st.session_state.historial_tasas = []

            st.success(
                "Historial eliminado correctamente."
            )


    # ========================================================
    # RESULTADOS
    # ========================================================

    if len(st.session_state.historial_tasas) > 0:

        st.subheader("Historial de resultados")


        st.dataframe(
            st.session_state.historial_tasas,
            use_container_width=True
        )


        ultimo = st.session_state.historial_tasas[-1]


        col1, col2 = st.columns(2)


        with col1:

            st.metric(
                "Tasa de error",
                f"{ultimo['Tasa de error (%)']:.2f}%"
            )


        with col2:

            st.metric(
                "Tasa de éxito",
                f"{ultimo['Tasa de éxito (%)']:.2f}%"
            )


# ============================================================
# EJERCICIO 4
# PROGRAMACIÓN ORIENTADA A OBJETOS
# ============================================================

elif modulos == "Ejercicio 4":

    st.markdown("""
        <div class="custom-data-title">
            <h1>Ejercicio 4 - Gestión de Pacientes con POO</h1>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    En este ejercicio se utiliza **Programación Orientada a
    Objetos (POO)** mediante la clase `Paciente`.
    """)


    if "pacientes" not in st.session_state:

        st.session_state.pacientes = []


    st.subheader("Registrar paciente")


    nombre = st.text_input(
        "Nombre del paciente",
        key="nombre_paciente"
    )


    edad = st.number_input(
        "Edad",
        min_value=0,
        max_value=120,
        value=18,
        step=1,
        key="edad_paciente"
    )


    diagnostico = st.text_input(
        "Diagnóstico",
        key="diagnostico_paciente"
    )


    col1, col2 = st.columns(2)


    with col1:

        if st.button("Crear paciente"):

            if nombre.strip() == "":

                st.error(
                    "Ingrese el nombre del paciente."
                )

            elif diagnostico.strip() == "":

                st.error(
                    "Ingrese el diagnóstico."
                )

            else:

                paciente = lc.Paciente(
                    nombre,
                    edad,
                    diagnostico
                )

                st.session_state.pacientes.append(
                    paciente
                )

                st.success(
                    "Paciente registrado correctamente."
                )


    with col2:

        if st.button("Eliminar último paciente"):

            if len(st.session_state.pacientes) > 0:

                st.session_state.pacientes.pop()

                st.success(
                    "Último paciente eliminado."
                )

            else:

                st.info(
                    "No existen pacientes registrados."
                )


    # ========================================================
    # LISTADO DE PACIENTES
    # ========================================================

    if len(st.session_state.pacientes) > 0:

        st.subheader("Pacientes registrados")


        for i, paciente in enumerate(
            st.session_state.pacientes,
            start=1
        ):

            with st.expander(
                f"Paciente {i}: {paciente.nombre}"
            ):

                st.write(
                    f"**Nombre:** {paciente.nombre}"
                )

                st.write(
                    f"**Edad:** {paciente.edad}"
                )

                st.write(
                    f"**Diagnóstico:** {paciente.diagnostico}"
                )

                if hasattr(paciente, "resumen"):

                    st.write(
                        paciente.resumen()
                    )


    else:

        st.info(
            "No hay pacientes registrados."
        )



















