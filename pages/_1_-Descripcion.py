import streamlit as st

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://images.pexels.com/photos/1365795/pexels-photo-1365795.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    h1, h2, h3, h4, h5, h6, p, div, span {{
        color: white !important;
    }}
        section[data-testid="stSidebar"] > div {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    }}
        /* Créditos de la imagen */
    .credit {{
        position: fixed;
        bottom: 10px;
        right: 10px;
        font-size: 13px;
        background-color: rgba(0, 0, 0, 0.6);
        padding: 6px 10px;
        border-radius: 8px;
        color: white;
        border: 1px solid white;
        box-shadow: 0 0 6px rgba(255, 255, 255, 0.4);
        z-index: 100;
    }}
        .credit a {{
        color: white;
        text-decoration: underline;
    }}
    </style>

    <div class="credit">
        Autor: <a href="https://www.pexels.com/es-es/@mayday/" target="_blank">may day.ua</a> en <a href="https://www.pexels.com/es-es/" target="_blank">Pexels</a>
    </div>
    """,
    unsafe_allow_html=True
)
st.title("Descripción de los datos ✍️.​")
st.markdown("""
Este conjunto de datos, previo a una posterior limpieza, unión y transformación de los mismos, simula las características que influyen en las ventas globales de un videojuego en el año que sale al mercado.
            
- **Platform**: Videoconsola disponible para jugar.
- **Year**: Año de lanzamiento del videojuego.
- **Genre**: Genero del videojuego.
- **Publisher**: Empresa que desarrolla el juego.
- **User_Score**: Puntuacion del cliente (0-10) en la pagina web 'Metacritic.com'.
- **User Ratings Count**: Número de veces que han puntuado.
- **Estado_Consola**: Situación en el mercado actual de la videoconsola.
- **Price**: Precio del videojuego, en Euros (€), de salida al mercado.
- **Price_Platform**: Precio de salida, en Euros (€), de la videoconsola al mercado.
- **Year_Consola**: Año en el salio la videoconsola.
- **Modo Juego**: Opción del videojuego de jugar varios jugadores o es individual.
- **Años_desde_lanzamiento_consola**: Período de tiempo desde que salio al mercado la videoconsola, hasta que salio el videojuego para esa consola concreta.
- **Precio_relativo**: precio del videojuego en relación con el precio de la consola en la que se lanza. Es decir, cuán caro es un juego comparado con el coste de la plataforma que lo soporta.
- **PEGI_Categoria**: Clasificación oficial que establece la edad permitida que puede jugar a un videojuego en función del contenido del mismo.
- **Duración_juego_cat**: Duración de tiempo que tiene la historia principal de un videjuego en funcion de su genero.
- **Tipo_Saga**: Categoría que se establece para considerar si el videojuego pertenece a una Saga de videojuegos o no.
- **Situacion_Economica**: Situación Economica Global que se vivia en los años a el lanzamiento del videojuego.
            """)