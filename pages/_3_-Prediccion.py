import streamlit as st
import pandas as pd
import joblib

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://images.unsplash.com/photo-1542903660-eedba2cda473?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    h1, h2, h3, h4, h5, h6, span, p {{
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
        Autor: <a href="https://unsplash.com/es/@markusspiske" target="_blank">Markus Spiske</a> en <a href="https://unsplash.com/es" target="_blank">Unsplash</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Cargar modelo
modelo = joblib.load('Modelo/modelo_videojuegos.pkl')

# Título de la app
st.title('📈​ Predicción de ventas de videojuegos 📉.')
st.markdown('Introduce los detalles del videojuego para estimar su categoría de ventas.')
lista_publisher = ['Nintendo', 'Microsoft Game Studios', 'Take-Two Interactive', 'Sony Computer Entertainment', 'Activision', 'Ubisoft', 'Bethesda Softworks', 'Electronic Arts', 'Sega', 'SquareSoft', 'Atari', '505 Games', 'Capcom', 'GT Interactive', 'Konami Digital Entertainment', 'Sony Computer Entertainment Europe', 'Square Enix', 'LucasArts', 'Virgin Interactive', 'Warner Bros. Interactive Entertainment', 'Universal Interactive', 'Eidos Interactive', 'RedOctane', 'Vivendi Games', 'Enix Corporation', 'Namco Bandai Games', 'Palcom', 'Hasbro Interactive', 'THQ', 'Fox Interactive', 'Acclaim Entertainment', 'MTV Games', 'Disney Interactive Studios', 'Majesco Entertainment', 'Codemasters', 'Red Orb', 'Level 5', 'Arena Entertainment', 'Midway Games', 'JVC', 'Deep Silver', '989 Studios', 'NCSoft', 'UEP Systems', 'Parker Bros.', 'Maxis', 'Imagic', 'Tecmo Koei', 'Valve Software', 'ASCII Entertainment', 'Mindscape', 'Infogrames', 'Unknown', 'Square', 'Valve', 'Activision Value', 'Banpresto', 'D3Publisher', 'Oxygen Interactive', 'Red Storm Entertainment', 'Video System', 'Hello Games', 'Global Star', 'Gotham Games', 'Westwood Studios', 'GungHo', 'Crave Entertainment', 'Hudson Soft', 'Coleco', 'Rising Star Games', 'Atlus', 'TDK Mediactive', 'ASC Games', 'Zoo Games', 'Accolade', 'Sony Online Entertainment', '3DO', 'RTL', 'Natsume', 'Focus Home Interactive', 'Alchemist', 'Black Label Games', 'SouthPeak Games', 'Mastertronic', 'Ocean', 'Zoo Digital Publishing', 'Psygnosis', 'City Interactive', 'Empire Interactive', 'Success', 'Compile', 'Russel', 'Taito', 'Agetec', 'GSP', 'Microprose', 'Play It', 'Slightly Mad Studios', 'Tomy Corporation', 'Sammy Corporation', 'Koch Media', 'Game Factory', 'Titus', 'Marvelous Entertainment', 'Genki', 'Mojang', 'Pinnacle', 'CTO SpA', 'TalonSoft', 'Crystal Dynamics', 'SCi', 'Quelle', 'mixi, Inc', 'Rage Software', 'Ubisoft Annecy', 'Scholastic Inc.', 'Interplay', 'Mystique', 'ChunSoft', 'Square EA', '20th Century Fox Video Games', 'Avanquest Software', 'Hudson Entertainment', 'Nordic Games', 'Men-A-Vision', 'Nobilis', 'Big Ben Interactive', 'Touchstone', 'Spike', 'Jester Interactive', 'Nippon Ichi Software', 'LEGO Media', 'Quest', 'Illusion Softworks', 'Tigervision', 'Funbox Media', 'Rocket Company', 'Metro 3D', 'Mattel Interactive', 'IE Institute', 'Rondomedia', 'Sony Computer Entertainment America', 'Universal Gamex', 'Ghostlight', 'Wizard Video Games', 'BMG Interactive Entertainment', 'PQube', 'Trion Worlds', 'Laguna', 'Ignition Entertainment', 'Takara', 'Kadokawa Shoten', 'Destineer', 'Enterbrain', 'Xseed Games', 'Imagineer', 'System 3 Arcade Software', 'CPG Products', 'Aruze Corp', 'Gamebridge', 'Midas Interactive Entertainment', 'Jaleco', 'Answer Software', 'XS Games', 'Activision Blizzard', 'Pack In Soft', 'Rebellion', 'Xplosiv', 'GameMill Entertainment', 'Wanadoo', 'NovaLogic', 'Telltale Games', 'Epoch', 'BAM! Entertainment', 'Knowledge Adventure', 'Mastiff', 'Tetris Online', 'Harmonix Music Systems', 'ESP', 'TYO', 'Telegames', 'Mud Duck Productions', 'Screenlife', 'Pioneer LDC', 'Magical Company', 'Mentor Interactive', 'Kemco', 'Human Entertainment', 'Avanquest', 'Data Age', 'Electronic Arts Victor', 'Black Bean Games', 'Jack of All Games', '989 Sports', 'Takara Tomy', 'Media Rings', 'Elf', 'Starfish', 'Zushi Games', 'Jorudan', 'Destination Software, Inc', 'New', 'Brash Entertainment', 'ITT Family Games', 'PopCap Games', 'Home Entertainment Suppliers', 'Ackkstudios', 'Starpath Corp.', 'P2 Games', 'BPS', 'Gathering of Developers', 'NewKidCo', 'Storm City Games', 'CokeM Interactive', 'CBS Electronics', 'Magix', 'Marvelous Interactive', 'Kalypso Media', 'Nihon Falcom Corporation', 'Wargaming.net', 'Angel Studios', 'Arc System Works', 'Playmates', 'SNK Playmore', 'Hamster Corporation', 'From Software', 'Nippon Columbia', 'Nichibutsu', 'Little Orbit', 'Conspiracy Entertainment', 'DTP Entertainment', 'Hect', 'Mumbo Jumbo', 'Pacific Century Cyber Works', 'Indie Games', 'Liquid Games', 'NEC', 'Axela', 'ArtDink', 'Sunsoft', 'Gust', 'NEC Interchannel', 'FuRyu', 'Xing Entertainment', 'ValuSoft', 'Victor Interactive', 'Detn8 Games', 'American Softworks', 'Nordcurrent', 'Bomb', 'Falcom Corporation', 'AQ Interactive', 'CCP', 'Milestone S.r.l.', 'JoWood Productions', 'Seta Corporation', 'SNK', 'On Demand', 'NCS', 'Aspyr', 'Gremlin Interactive Ltd', 'Agatsuma Entertainment', 'Compile Heart', 'Culture Brain', 'Mad Catz', 'Shogakukan', 'Merscom LLC', 'Rebellion Developments', 'Nippon Telenet', 'TDK Core', 'bitComposer Games', 'Foreign Media Games', 'Astragon', 'SSI', 'Kadokawa Games', 'Idea Factory', 'Performance Designed Products', 'Asylum Entertainment', 'Core Design Ltd.', 'PlayV', 'UFO Interactive', 'Idea Factory International', 'Playlogic Game Factory', 'Essential Games', 'Adeline Software', 'Funcom', 'Panther Software', 'Blast! Entertainment Ltd', 'Game Life', 'DSI Games', 'Avalon Interactive', 'Popcorn Arcade', 'Neko Entertainment', 'Vir2L Studios', 'Aques', 'Syscom', 'White Park Bay Software', 'System 3', 'Vatical Entertainment', 'Daedalic', 'EA Games', 'Media Factory', 'Vic Tokai', 'The Adventure Company', 'Game Arts', 'Broccoli', 'Acquire', 'General Entertainment', 'Excalibur Publishing', 'Imadio', 'Swing! Entertainment', 'Sony Music Entertainment', 'Aqua Plus', 'Paradox Interactive', 'Hip Interactive', 'DreamCatcher Interactive', 'Tripwire Interactive', 'Sting', 'Yacht Club Games', 'SCS Software', 'Bigben Interactive', 'Havas Interactive', 'Slitherine Software', 'Graffiti', 'Funsta', 'Telstar', 'U.S. Gold', 'DreamWorks Interactive', 'Data Design Interactive', 'MTO', 'DHM Interactive', 'FunSoft', 'SPS', 'Bohemia Interactive', 'Reef Entertainment', 'Tru Blu Entertainment', 'Moss', 'T&E Soft', 'O-Games', 'Aksys Games', 'NDA Productions', 'Data East', 'Time Warner Interactive', 'Gainax Network Systems', 'Daito', 'O3 Entertainment', 'Gameloft', 'Xicat Interactive', 'Simon & Schuster Interactive', 'Valcon Games', 'PopTop Software', 'TOHO', 'HMH Interactive', '5pb', 'Cave', 'CDV Software Entertainment', 'Microids', 'PM Studios', 'Paon', 'Micro Cabin', 'GameTek', 'Benesse', 'Type-Moon', 'Enjoy Gaming ltd.', 'Asmik Corp', 'Interplay Productions', 'Asmik Ace Entertainment', 'inXile Entertainment', 'Image Epoch', 'Phantom EFX', 'Evolved Games', 'responDESIGN', 'Culture Publishers', 'Griffin International', 'Hackberry', 'Hearty Robin', 'Nippon Amuse', 'Origin Systems', 'Seventh Chord', 'Mitsui', 'Milestone', 'Abylight', 'Flight-Plan', 'Glams', 'Locus', 'Warp', 'Daedalic Entertainment', 'Alternative Software', 'Myelin Media', 'Mercury Games', 'Irem Software Engineering', 'Sunrise Interactive', 'Elite', 'Evolution Games', 'Tivola', 'Global A Entertainment', 'Edia', 'Athena', 'Aria', 'Gamecock', 'Tommo', 'Altron', 'Happinet', 'iWin', 'Media Works', 'Fortyfive', 'Revolution Software', 'Imax', 'Crimson Cow', '10TACLE Studios', 'Groove Games', 'Pack-In-Video', 'Insomniac Games', 'Ascaron Entertainment GmbH', 'Asgard', 'Ecole', 'Yumedia', 'Phenomedia', 'HAL Laboratory', 'Grand Prix Games', 'DigiCube', 'Creative Core', 'Kaga Create', 'WayForward Technologies', 'LSP Games', 'ASCII Media Works', 'Coconuts Japan', 'Arika', 'Ertain', 'Marvel Entertainment', 'Prototype', 'Phantagram', '1C Company', 'The Learning Company', 'TechnoSoft', 'Vap', 'Misawa', 'Tradewest', 'Team17 Software', 'Yeti', 'Pow', 'Navarre Corp', 'MediaQuest', 'Max Five', 'Comfort', 'Monte Christo Multimedia', 'Pony Canyon', 'Riverhillsoft', 'Summitsoft', 'Milestone S.r.l', 'Playmore', 'MLB.com', 'Kool Kizz', 'Flashpoint Games', '49Games', 'Legacy Interactive', 'Alawar Entertainment', 'CyberFront', 'Cloud Imperium Games Corporation', 'Societa', 'Virtual Play Games', 'Interchannel', 'Sonnet', 'Experience Inc.', 'Zenrin', 'Iceberg Interactive', 'Ivolgamus', '2D Boy', 'MC2 Entertainment', 'Kando Games', 'Just Flight', 'Office Create', 'Mamba Games', 'Fields', 'Princess Soft', 'Maximum Family Games', 'Berkeley', 'Fuji', 'Dusenberry Martin Racing', 'imageepoch Inc.', 'Big Fish Games', 'Her Interactive', 'Kamui', 'ASK', 'TopWare Interactive', 'Headup Games', 'KSS', 'Cygames', 'KID', 'Quinrose', 'Sunflowers', 'dramatic create', 'TGL', 'Encore', 'Extreme Entertainment Group', 'Intergrow', 'G.Rev', 'Sweets', 'Kokopeli Digital Studios', 'Number None', 'Nexon', 'id Software', 'BushiRoad', 'Tryfirst', 'Strategy First', '7G//AMES', 'GN Software', "Yuke's", 'Easy Interactive', 'Licensed 4U', 'FuRyu Corporation', 'Lexicon Entertainment', 'Paon Corporation', 'Kids Station', 'GOA', 'Graphsim Entertainment', 'King Records', 'Introversion Software', 'Minato Station', 'Devolver Digital', 'Blue Byte', 'Gaga', 'Yamasa Entertainment', 'Plenty', 'Views', 'fonfun', 'NetRevo', 'Codemasters Online', 'Quintet', 'Phoenix Games', 'Dorart', 'Marvelous Games', 'Focus Multimedia', 'Karin Entertainment', 'Aerosoft', 'Gakken', 'Mirai Shounen', 'Datam Polystar', 'Saurus', 'HuneX', 'Revolution (Japan)', 'Giza10', 'Visco', 'Alvion', 'Mycom', 'Giga', 'Warashi', 'System Soft', 'Sold Out', 'Lighthouse Interactive', 'Masque Publishing', 'RED Entertainment', 'Michaelsoft', 'Media Entertainment', 'New World Computing', 'Genterprise', 'Interworks Unlimited, Inc.', 'Boost On', 'Stainless Games', 'EON Digital Entertainment', 'Epic Games', 'Naxat Soft', 'Ascaron Entertainment', 'Piacci', 'Nitroplus', 'Paradox Development', 'Otomate', 'Ongakukan', 'Commseed', 'Inti Creates', 'Takuyo', 'Interchannel-Holon', 'Rain Games', 'UIG Entertainment']
# Inputs visibles para el usuario
plataformas_activas = [
    'PlayStation 4', 'Xbox One', 'PC'
]
plataforma_secundaria = ['Nintendo 3DS', 'PlayStation Vita']
plataforma_obsoleta = ['Nintendo Wii', 'Nintendo Entertainment System', 'Game Boy', 'Nintendo DS', 'Xbox 360', 'PlayStation 3', 'PlayStation 2', 'Super Nintendo Entertainment System', 'Game Boy Advance', 'Nintendo 64', 'PlayStation', 'Xbox', 'Atari 2600', 'PlayStation Portable', 'GameCube', 'Nintendo Wii U', 'Sega Genesis', 'Dream Cast', 'Sega Saturn']
estado_consola = st.selectbox('Antigüedad Consola', ['Consola Obsoleta', 'Consola Secundaria', 'Consola Activa'])
if estado_consola == 'Consola Activa':
    platform = st.selectbox('Plataforma', plataformas_activas)
elif estado_consola == 'Consola Secundaria':
    platform = st.selectbox('Plataforma', plataforma_secundaria)
else:
    platform = st.selectbox('Plataforma', plataforma_obsoleta)
genre = st.selectbox('Género', ['Sports', 'Platform', 'Racing', 'Role-Playing', 'Puzzle', 'Misc', 'Shooter', 'Simulation', 'Action', 'Fighting', 'Adventure', 'Strategy'])      # Ajusta también
price = st.number_input('Precio del videojuego (€)', min_value=29.99, max_value=69.99, value=29.99)
price_platform = st.number_input('Precio de la consola (€)', min_value=113.5, max_value=599.0, value=113.5)
modo_juego = st.selectbox('Modo de juego', ['Multijugador', 'Individual'])
pegi = st.selectbox('Clasificación PEGI', ['Infantil', 'Adulto', 'Adolescente'])
duracion_cat = st.selectbox('Duración estimada', ['Corto', 'Medio', 'Largo'])
year = st.number_input('Año del videojuego', min_value=1980, max_value=2020, value=1980)
nota_usuario = st.number_input('Nota del usuario (0-10)', min_value=0, max_value=10, value=0)
n_votaciones = st.number_input('Nº votaciones', min_value=0, max_value=24855, value=5)
year_consola = st.number_input('Año de la consola', min_value=1977, max_value=2013, value=1977)
saga = st.selectbox('Saga', ['No saga', 'Saga'])
economia = st.selectbox('Situación economica', ['Crecimiento', 'Recesion'])
publisher = st.selectbox('Compañia', lista_publisher)

# Botón para predecir
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #fbc02d;   /* Fondo amarillo oscuro */
        border: 2px solid #f44336;   /* Borde rojo */
        border-radius: 8px;
        padding: 0.6em 1.2em;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #b2ebf2;   /* Efecto al pasar el ratón */
        color: black;
        border-color: #4dd0e1;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)
if st.button('Predecir Ventas'):
        # Crear dataframe con los valores ingresados
        input_data = pd.DataFrame ({
            'Platform': [platform],
            'Genre': [genre],
            'Price': [price],
            'Modo Juego': [modo_juego],
            'PEGI_categoria': [pegi],
            'Duracion_juego_cat': [duracion_cat],
            'Year': [year],
            'Publisher': [publisher],  
            'User Score': [nota_usuario],
            'User Ratings Count': [n_votaciones],
            'Estado_Consola': [estado_consola],
            'Price_Platform': [price_platform],
            'Year_Consola': [year_consola],
            'Tipo_Saga': [saga],
            'Situacion_Economica': [economia],
            'Nombre_Base': ['JuegoGenérico'],
            'Precio_relativo': [price / price_platform],
            'Años_desde_lanzamiento_consola': [year - year_consola]})
        prediccion = modelo.predict(input_data)[0]

        st.markdown(
            f"""
            <div style="
                background-color: #e0f7fa;
                padding: 20px;
                border-radius: 10px;
                border: 1px solid #b2ebf2;
                color: black;
                font-weight: bold;
                margin-top: 20px;
            ">
                Predicción estimada: {prediccion}
            </div>
            """,
            unsafe_allow_html=True
        )
        if prediccion == 'Muy Alta':
            st.markdown("""
                <div style="
                    background-color: #e8f5e9;
                    padding: 15px;
                    border-radius: 8px;
                    border: 1px solid #c8e6c9;
                    color: #1b5e20;
                    margin-top: 10px;
                ">
                    🔹 Estimación: Entre 1.22 y 82.74 millones de unidades vendidas.
                </div>
                """, unsafe_allow_html=True)
        elif prediccion == 'Alta':
            st.markdown("""
                <div style="
                    background-color: #fffde7;
                    padding: 15px;
                    border-radius: 8px;
                    border: 1px solid #fff59d;
                    color: #f57f17;
                    margin-top: 10px;
                ">
                    🔹 Estimación: Entre 250 mil y 1.21 millones de unidades vendidas.
                </div>
                """, unsafe_allow_html=True)
        elif prediccion == 'Normal':
            st.markdown("""
                <div style="
                    background-color: #fbe9e7;
                    padding: 15px;
                    border-radius: 8px;
                    border: 1px solid #ffab91;
                    color: #bf360c;
                    margin-top: 10px;
                ">
                    🔹 Estimación: Entre mil y 240 mil de unidades vendidas.
                </div>
                """, unsafe_allow_html=True)
