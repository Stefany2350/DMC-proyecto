import streamlit as st
import numpy as np
import libreria_funciones_proyecto1 as lf
import librería_clases_proyecto1 as lc

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA Y ESTILOS CSS
# ==========================================
st.set_page_config(
    page_title="Gestión y Análisis de Datos - Python Fundamentals",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inyección de Estilos CSS Avanzados
st.markdown("""
    <style>
    /* --------------------------------------------------------
       PALETA SLATE SOFT & CONTENEDORES PRINCIPALES
       -------------------------------------------------------- */
    .stApp {
        background-color: #1E293B; /* Slate 800: Fondo general más suave y moderno */
        color: #F8FAFC;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Estilo del Sidebar (Panel de Navegación) en Slate 700 */
    [data-testid="stSidebar"] {
        background-color: #334155;
        border-right: 1px solid #475569;
    }
    
    [data-testid="stSidebar"] .stMarkdown h1, 
    [data-testid="stSidebar"] .stMarkdown h2, 
    [data-testid="stSidebar"] .stMarkdown h3 {
        color: #38BDF8;
    }

    /* --------------------------------------------------------
       TÍTULO DEL SIDEBAR
       -------------------------------------------------------- */
    .sidebar-custom-title {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%) !important;
        border: 1px solid #475569 !important;
        border-left: 5px solid #38BDF8 !important;
        padding: 16px 20px !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
        position: relative !important;
        overflow: hidden !important;
        margin-bottom: 20px !important;
        transition: all 0.4s ease !important;
    }

    .sidebar-custom-title::before {
        content: "" !important;
        position: absolute !important;
        top: 0; right: 0; bottom: 0; left: 0;
        background-image: radial-gradient(circle, rgba(56, 189, 248, 0.15) 1.5px, transparent 1.5px) !important;
        background-size: 14px 14px !important;
        opacity: 0.6 !important;
        pointer-events: none !important;
    }

    .sidebar-custom-title::after {
        content: "" !important;
        position: absolute !important;
        top: 0; right: 0; bottom: 0; left: 0;
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.3) 0%, rgba(56, 189, 248, 0.3) 100%) !important;
        opacity: 0 !important;
        transition: opacity 0.4s ease-in-out !important;
        pointer-events: none !important;
        z-index: 1 !important;
    }

    .sidebar-custom-title > * {
        position: relative !important;
        z-index: 2 !important;
    }

    .sidebar-custom-title:hover {
        transform: translateY(-2px) !important;
        border-color: #38BDF8 !important;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.4) !important;
    }

    .sidebar-custom-title:hover::after {
        opacity: 1 !important;
    }

    .sidebar-custom-title h2 {
        color: #F8FAFC !important;
        font-size: 1.25rem !important;
        font-weight: 700 !important;
        margin: 0 !important;
    }

    /* --------------------------------------------------------
       TÍTULOS PRINCIPALES CON DISEÑO FIJO (SIN HOVER EFFECT)
       -------------------------------------------------------- */
    .contenedor-titulo-fijo {
        background-color: #111a2c !important; /* Fondo azul oscuro */
        background-image: radial-gradient(rgba(255, 255, 255, 0.1) 1px, transparent 1px) !important;
        background-size: 15px 15px !important; /* Efecto de cuadrícula de puntos */
        border: 1.5px solid #3b82f6 !important; /* Borde azul claro/celeste */
        border-radius: 12px !important;
        padding: 25px 30px !important;
        box-shadow: 0px 0px 20px 2px rgba(59, 130, 246, 0.4) !important; /* Resplandor (glow) externo */
        margin-bottom: 25px !important;
        
        /* Prevenir transiciones o cambios de cursor */
        transition: none !important; 
        cursor: default !important;
    }

    .contenedor-titulo-fijo:hover {
        background-color: #111a2c !important;
        border: 1.5px solid #3b82f6 !important;
        box-shadow: 0px 0px 20px 2px rgba(59, 130, 246, 0.4) !important;
        transform: none !important;
    }

    .titulo-principal {
        color: white !important;
        font-size: 32px !important;
        font-weight: 700 !important;
        margin: 0 !important;
        padding-bottom: 8px !important;
        display: flex !important;
        align-items: center !important;
        gap: 12px !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }

    .subtitulo {
        color: #cbd5e1 !important; /* Gris claro/pizarra */
        font-size: 16px !important;
        margin: 0 !important;
        font-weight: 400 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }

    /* --------------------------------------------------------
       ESTILOS PARA BOTONES, INPUTS Y MÉTRICAS
       -------------------------------------------------------- */
    .stButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%);
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.6);
        transform: translateY(-2px);
    }

    .stTextInput input, .stSelectbox select, .stNumberInput input {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
        border: 1px solid #475569 !important;
        border-radius: 8px !important;
    }
    
    .stTextInput input:focus, .stSelectbox select:focus, .stNumberInput input:focus {
        border-color: #38BDF8 !important;
        box-shadow: 0 0 10px rgba(56, 189, 248, 0.3) !important;
    }

    [data-testid="stMetric"] {
        background-color: #0F172A;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #475569;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    [data-testid="stMetricLabel"] {
        color: #94A3B8 !important;
    }
    [data-testid="stMetricValue"] {
        color: #38BDF8 !important;
    }

    [data-testid="stDataFrame"] {
        border-radius: 10px;
        overflow: hidden;
        border: 1px solid #475569;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# BARRA LATERAL (NAVEGACIÓN MEJORADA)
# ==========================================
st.sidebar.markdown("""
    <div class="sidebar-custom-title">
        <h2>🎛️ Panel de Navegación</h2>
    </div>
""", unsafe_allow_html=True)

modulos = st.sidebar.selectbox(
    "Seleccione la sección a consultar",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# ==========================================
# SECCIÓN: HOME
# ==========================================
if modulos == "Home":
    st.sidebar.markdown("---")
    st.sidebar.image("image_home.png", use_container_width=True)
    
    st.markdown("""
        <div class="contenedor-titulo-fijo">
            <h1 class="titulo-principal">🚀 Aplicación de Python para la Gestión y Análisis de Datos</h1>
            <p class="subtitulo">Módulo: Python Fundamentals | Panel de Control General</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_info1, col_info2 = st.columns(2)
    with col_info1:
        st.write("**Estudiante:** Stefany Salazar Espinoza")
    with col_info2:
        st.write("**Año:** 2026")
        
    st.markdown("---")
    
    st.markdown("""
    ### 💡 Descripción del Proyecto
    El presente proyecto tiene como objetivo aplicar los conocimientos adquiridos en el módulo **Python Fundamentals**, 
    permitiendo evidenciar el uso de estructuras de datos, widgets, funciones, clases y lógica de programación 
    mediante la creación de una interfaz interactiva y de alto rendimiento visual.

    ### 🛠️ Tecnologías Utilizadas
    - **Python** (Lógica y procesamiento)
    - **Streamlit** (Interfaz de usuario interactiva)
    - **NumPy** (Estructuras de datos optimizadas)
    - **GitHub** (Control de versiones)
    """)

    st.image("Python_logo.png", width=250)

# ==========================================
# SECCIÓN: EJERCICIO 1 (Flujo de caja)
# ==========================================
elif modulos == "Ejercicio 1":
    st.sidebar.markdown("---")
    st.sidebar.image("image_ejercicio1.jpg", use_container_width=True)
    
    st.markdown("""
        <div class="contenedor-titulo-fijo">
            <h1 class="titulo-principal">💰 Flujo de caja con listas</h1>
            <p class="subtitulo">Módulo Financiero - Análisis de Ingresos y Gastos</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### Descripción del ejercicio
    En este ejercicio se desarrolla un módulo para registrar movimientos financieros utilizando listas. 
    Permite registrar ingresos y gastos, calcular subtotales y determinar el **saldo final del flujo de caja**.
    """)

    st.markdown("---")
    st.subheader("Registrar movimiento")

    concepto = st.text_input("Ingrese el concepto del movimiento")
    tipo = st.selectbox("Seleccione el tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Ingrese el valor", min_value=0.0, value=0.0, step=10.0)

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    if st.button("Registrar movimiento"):
        if concepto != "" and valor > 0:
            movimiento = {"concepto": concepto, "tipo": tipo, "valor": valor}
            st.session_state.movimientos.append(movimiento)
            st.success("Movimiento registrado correctamente")
        else:
            st.error("Ingrese un concepto válido y un valor mayor que 0.")

    st.markdown("---")
    st.subheader("Movimientos registrados")

    if len(st.session_state.movimientos) > 0:
        col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
        col1.markdown("**Concepto**")
        col2.markdown("**Tipo**")
        col3.markdown("**Valor**")
        col4.markdown("**Eliminar**")

        for i, movimiento in enumerate(st.session_state.movimientos):
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
            col1.write(movimiento["concepto"])
            col2.write(movimiento["tipo"])
            col3.write(f"S/ {movimiento['valor']:,.2f}")

            if col4.button("🗑️", key=f"eliminar_{i}"):
                st.session_state.movimientos.pop(i)
                st.rerun()

        total_ingresos = sum(m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Ingreso")
        total_gastos = sum(m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Gasto")
        saldo_final = total_ingresos - total_gastos

        st.markdown("---")
        st.subheader("Resumen del flujo de caja")
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Total de ingresos", f"S/ {total_ingresos:,.2f}")
        col_m2.metric("Total de gastos", f"S/ {total_gastos:,.2f}")
        col_m3.metric("Saldo final", f"S/ {saldo_final:,.2f}")

        if saldo_final > 0:
            st.success("Flujo de caja: A FAVOR 📈")
        elif saldo_final < 0:
            st.error("Flujo de caja: EN CONTRA 📉")
        else:
            st.info("Flujo de caja: EN EQUILIBRIO ⚖️")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Borrar todos los movimientos"):
            st.session_state.movimientos = []
            st.rerun()
    else:
        st.info("No hay movimientos registrados actualmente.")

# ==========================================
# SECCIÓN: EJERCICIO 2 (Registro de productos)
# ==========================================
elif modulos == "Ejercicio 2":
    st.sidebar.markdown("---")
    st.sidebar.image("image_ejercicio2.jpg", use_container_width=True)
    
    st.markdown("""
        <div class="contenedor-titulo-fijo">
            <h1 class="titulo-principal">📦 Formulario de registro de productos</h1>
            <p class="subtitulo">Módulo de Inventario - Procesamiento con Arreglos NumPy</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### Descripción del ejercicio
    Formulario optimizado para registrar productos utilizando **arreglos de NumPy**, calculando totales automáticos.
    """)

    st.markdown("---")
    st.subheader("Registrar producto")

    nombre = st.text_input("Ingrese el nombre del producto")
    categoria = st.selectbox("Seleccione la categoría", ["Limpieza", "Tecnología", "Alimentos", "Bebidas", "Otros"])
    precio = st.number_input("Ingrese el precio", min_value=0.0, value=0.0, step=1.0)
    cantidad = st.number_input("Ingrese la cantidad", min_value=1, value=1, step=1)

    if "productos" not in st.session_state:
        st.session_state.productos = np.empty((0, 5), dtype=object)

    if st.button("Registrar producto"):
        if nombre != "" and precio > 0 and cantidad > 0:
            total = precio * cantidad
            nuevo_producto = np.array([[nombre, categoria, precio, cantidad, total]], dtype=object)
            st.session_state.productos = np.vstack([st.session_state.productos, nuevo_producto])
            st.success("Producto registrado correctamente")
        else:
            st.error("Ingrese un nombre válido y un valor mayor que 0.")

    st.markdown("---")
    st.subheader("Productos registrados")

    if len(st.session_state.productos) > 0:
        st.dataframe(
            st.session_state.productos,
            column_config={
                1: "Nombre",
                2: "Categoría",
                3: st.column_config.NumberColumn("Precio", format="S/ %.2f"),
                4: "Cantidad",
                5: st.column_config.NumberColumn("Total", format="S/ %.2f")
            },
            hide_index=True,
            use_container_width=True
        )

        st.markdown("---")
        st.subheader("Gestión de inventario")
        nombres_productos = [p[0] for p in st.session_state.productos]
        producto_seleccionado = st.selectbox("Seleccione el producto que desea eliminar", nombres_productos)

        col_elim1, col_elim2 = st.columns(2)
        with col_elim1:
            if st.button("Eliminar producto seleccionado"):
                indice = nombres_productos.index(producto_seleccionado)
                st.session_state.productos = np.delete(st.session_state.productos, indice, axis=0)
                st.success("Producto eliminado correctamente")
                st.rerun()
        with col_elim2:
            if st.button("Borrar todo el inventario"):
                st.session_state.productos = np.empty((0, 5), dtype=object)
                st.success("Todos los productos fueron eliminados.")
                st.rerun()
    else:
        st.info("No hay productos registrados en el sistema.")

# ==========================================
# SECCIÓN: EJERCICIO 3 (Tasa de error)
# ==========================================
elif modulos == "Ejercicio 3":
    st.sidebar.markdown("---")
    st.sidebar.image("image_ejercicio3.jpg", use_container_width=True)
    
    st.markdown("""
        <div class="contenedor-titulo-fijo">
            <h1 class="titulo-principal">📊 Cálculo de tasa de error de transacciones</h1>
            <p class="subtitulo">Módulo de Control de Calidad - Métricas y Análisis de Datos</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### Descripción del ejercicio
    Análisis de transacciones mediante funciones externas para calcular tasas de error y éxito de manera automatizada.
    """)

    st.markdown("---")
    st.subheader("Parámetros de Análisis")

    nombre_analisis = st.text_input("Ingrese periodo del análisis")
    transacciones_fallidas = st.number_input("Número de transacciones fallidas", min_value=0, value=0, step=1)
    transacciones_totales = st.number_input("Número de transacciones totales", min_value=1, value=1, step=1)

    if st.button("Ejecutar análisis"):
        if nombre_analisis == "":
            st.warning("Por favor ingrese el periodo del análisis.")
        else:
            try:
                resultado = lf.calcular_tasa_error_transacciones(transacciones_fallidas, transacciones_totales)
                st.success("Función ejecutada correctamente.")

                st.markdown("---")
                st.subheader(f"Resultado: {nombre_analisis}")
                
                col_r1, col_r2 = st.columns(2)
                col_r1.metric("Tasa de Error", f"{resultado['tasa_error_pct']:.4f}%")
                col_r2.metric("Tasa de Éxito", f"{resultado['tasa_exito_pct']:.4f}%")

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
                st.error(str(e))

    st.markdown("---")
    st.subheader("Histórico de resultados")
    if "historico_tasa_error" in st.session_state and len(st.session_state.historico_tasa_error) > 0:
        st.dataframe(st.session_state.historico_tasa_error, use_container_width=True)
        if st.button("Limpiar histórico"):
            st.session_state.historico_tasa_error = []
            st.rerun()
    else:
        st.info("No hay resultados históricos registrados.")

# ==========================================
# SECCIÓN: EJERCICIO 4 (Gestión de pacientes)
# ==========================================
elif modulos == "Ejercicio 4":
    st.sidebar.markdown("---")
    st.sidebar.image("image_ejercicio4.jpg", use_container_width=True)
    
    st.markdown("""
        <div class="contenedor-titulo-fijo">
            <h1 class="titulo-principal">🏥 Gestión de pacientes (CRUD)</h1>
            <p class="subtitulo">Módulo de Programación Orientada a Objetos - Control Clínico</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### Descripción del ejercicio
    Sistema orientado a objetos utilizando la clase **Paciente** para control clínico, cálculo de IMC y superficie corporal.
    """)

    if "pacientes" not in st.session_state:
        st.session_state.pacientes = []

    st.markdown("---")
    st.subheader("➕ Crear nuevo registro médico")

    nombre_p = st.text_input("Ingrese el nombre del paciente")
    peso_p = st.number_input("Ingrese el peso en kg", min_value=0.1, value=60.0, step=0.1)
    altura_p = st.number_input("Ingrese la altura en metros", min_value=0.1, value=1.60, step=0.01)

    if st.button("Registrar paciente"):
        try:
            paciente = lc.Paciente(nombre_p, peso_p, altura_p)
            st.session_state.pacientes.append(paciente)
            st.success("Paciente registrado correctamente.")
        except ValueError as e:
            st.error(str(e))

    st.markdown("---")
    st.subheader("📋 Registros de pacientes")
    if len(st.session_state.pacientes) > 0:
        registros = [p.resumen() for p in st.session_state.pacientes]
        st.dataframe(registros, use_container_width=True)

        st.markdown("---")
        col_act, col_elm = st.columns(2)

        with col_act:
            st.subheader("✏️ Actualizar datos")
            nombres = [p.nombre for p in st.session_state.pacientes]
            paciente_actualizar = st.selectbox("Seleccione paciente a actualizar", nombres, key="sel_act")
            nuevo_peso = st.number_input("Nuevo peso en kg", min_value=0.1, value=60.0, step=0.1, key="n_peso")
            nueva_altura = st.number_input("Nueva altura en metros", min_value=0.1, value=1.60, step=0.01, key="n_alt")

            if st.button("Actualizar paciente"):
                indice = nombres.index(paciente_actualizar)
                p_obj = st.session_state.pacientes[indice]
                p_obj.peso_kg = nuevo_peso
                p_obj.altura_m = nueva_altura
                st.success("Paciente actualizado correctamente.")
                st.rerun()

        with col_elm:
            st.subheader("🗑️ Eliminar registro")
            paciente_eliminar = st.selectbox("Seleccione paciente a eliminar", nombres, key="sel_elm")
            if st.button("Eliminar paciente"):
                indice = nombres.index(paciente_eliminar)
                st.session_state.pacientes.pop(indice)
                st.success("Paciente eliminado correctamente.")
                st.rerun()
    else:
        st.info("No hay pacientes registrados en la base de datos temporal.")


















