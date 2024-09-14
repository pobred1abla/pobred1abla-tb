import tweepy

client_secret='LoMCE9ZxK7KANTyLTmsYbltjo3k_CDhdThGFWra06JrbE6rPix'
API_key= 'mjL4v0aausHz8a5EylsfGTTvU'
API_secret= 'knLPHN4nNnPN9Dm6lPs9FztVBiOgpyAT4WEzoAA326q144Z28h'
baerer_token= 'AAAAAAAAAAAAAAAAAAAAAIlfvwEAAAAAezVA3LeGAlPG0Plfvn32XPeUNs0%3DWAsQfulD1jC5UTlTiu2FFXd7LXnpRA61UeXtUuymeB2It6vZQn'
access_token_secret= 'lYHAK3dJIq06oYgBOj8xIULA7aRvu6Y3tYXgDP84Q4bEv'
access_token='1833985843666497536-sZmgTx1p8HtBYfeWoYqSrh5vRF5pZu'

client=tweepy.Client(baerer_token,API_key,API_secret,access_token,access_token_secret)

auth = tweepy.OAuthHandler(API_key, API_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

import random
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
import time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont  # Importar PIL para manipular imágenes
import os 

nombres_famosos = [
    "Lionel Messi", "Paulo Dybala", "Angel Di María", "Rodrigo de Paul", "Alberto Samid",
    "Dibu Martínez", "Julián Álvarez", "Enzo Fernández", "Cuti Romero", "Nicolás Otamendi",
    "Lisandro Martínez", "Huevo Acuña", "Leandro Paredes", "Lucas Dalto", "Exequiel Palacios",
    "Nico González", "Albere", "Papu Gómez", "Gonzalo Montiel", "Franco Armani",
    "Gaston Edul", "Joaquín Correa", "Sofi Martinez", "Equi Fernández", "Colo Barco",
    "Franco Colapinto", "Facundo Colidio", "Karina la Princesita", "Gustavo Alfaro", "Marcelo Gallardo",
    "Carlos Tevez", "Sergio Agüero", "Marcos Rojo", "Julio Falcioni", "Diego Martínez",
    "Ruso Zielinski", "Darío Benedetto", "Chelo Weigandt", "Chiquito Romero", "Ricardo Darín",
    "Guillermo Francella", "Peter Lanzani", "Bri Marcos", "Luis Brandoni", "Lali Espósito",
    "China Suárez", "Andrea Rincon", "Furia", "Coty de GH", "Agustina Albertario",
    "Sofi Maure", "Claudia Villafañe", "Diego Peretti", "Marcos Ginocchio", "Manzana",
    "Mariano Martínez", "Nicolás Cabré", "Abel Pintos", "Tini Stoessel", "María Becerra",
    "Nicki Nicole", "Duki", "Bizarrap", "L-Gante", "Trueno", "Wos", "Tiago PZK", "Emilia Mernes",
    "Rusherking", "Florencia Peña", "Khea", "Lit Killah", "Nathy Peluso", "La Sole", "Andrés Calamaro",
    "Fito Páez", "Charly García", "Oky", "Ale Sergi", "Juliana Gattas", "Gustavo Cordera",
    "Ciro", "Juan Roman Riquelme", "Marcelo Tinelli", "Mirtha Legrand", "Susana Giménez", "Marley",
    "Santiago del Moro", "Guido Kaczka", "Yanina Latorre", "Angel de Brito", "Jorge Rial",
    "Mika Lafuente", "Viviana Canosa", "Beto Casella", "Andy Kusnetzoff", "Alejandro Fantino",
    "Sofi Jujuy", "Silvina Escudero", "Pampita", "Valeria Mazza", "Zaira Nara", "Chano",
    "Dalma Maradona", "Martin Demichelis", "Gabriela Michetti", "Fátima Florez", "Martín Bossi",
    "Migue Granados", "Coscu", "Caro Pardiaco", "Lizy Tagliani", "Spreen", "Carrera",
    "Juan Martín del Potro", "Peque Pareto", "Manu Ginóbili", "Papa Francisco",
    "Maxima de Holanda", "Luciana Aymar", "Momo", "Markito Navaja", "Goncho Banzas", "Unicornio",
    "Robleis", "Joaco López", "Pimpeano", "Luquitas Rodríguez", "Boffe GP", "Rober Galati", "Santutu",
    "C0ker", "Alberto Fernandez", "Fabiola Yañez", "Alex Caniggia", "Amalia Granata",
    "Luciana Salazar", "Angie Velasco", "Piñon Fijo", "Cristina Kirchner", "Javier Milei",
    "‍Horacio Rodríguez Larreta", "Sergio Massa", "Patricia Bullrich", "Mauricio Macri",
    "Axel Kicillof", "María Eugenia Vidal", "Máximo Kirchner", "Daniel Scioli", "Juan Schiaretti",
    "Enzo Perez", "Julieta Poggio", "C.R.O", "Bhavi", "Charlotte Caniggia", "Rodolfo D'Onofrio",
    "Daniel Angelici", "Sol Perez", "Romina Malaspina", "Jimena Baron", "Dtoke", "Papo MC",
    "El Demente", "Marito Baracus", "Flavio Azzaro", "Presi Duka", "Morena Beltran",
    "Martín Liberman", "Pollo Vignolo", "Mariano Closs", "Diego Latorre", "Lionel Scaloni",
    "Gustavo López", "Juan Pablo Varsky", "Oscar Ruggeri", "Milica", "Quique Wolff", "Alina Moine",   
    "Angela Lerena", "Jorge Lanata", "Eduardo Feinmann", "Alejandro Dolina", "Diego Brancatelli",
    "Adolfo Cambiasso", "Luis Majul", "Baby Etchecopar", "Diego Leuco", "Nico Occhiatto",
    "Flor Jazmin Peña", "Yoyi Francella", "Trinche", "Alex Pelao", "Yayo", "Fran Gomez",
    "Nati Jota", "Santi Maratea", "Grego Rossello", "Sofi Morandi", "Paulina Cocina", "Brunenger",
    "Tomas Mazza", "TeLoResumo", "Mariano De La Canal", "Ofelia Fernandez", "El Polaco",
    "Wanda Nara", "Mauro Icardi", "Pablito Lescano", "YSY A", "Zulma Lobato", "Mateo Messi",
    "Antonella Rocuzzo", "Lilita Carrio", "Margarita Stolbizer", "Maru Botana", "Mauro Zarate",
    "Neo Pistea", "Moria Casan", "Indio Solari", "Luis Ventura", "Fran MG", "Flor de la V",
    "La Mona Jimenez", "Cami Nair", "Mica Suarez"
]

usuarios_twitter = [
    '', "@PauDybala_JR", '', "@rodridepaul", "@soyalbertosamid",
    "@emimartinezz1", "@julianalvarezzz", "@IEnzofernandez8", "@CutiRomero2", "@Notamendi30",
    "@LisandrMartinez", "@AcunaMarcos17", "@LParedss",'@SoyDalto', "@exepalacios_",
    "@nicoivang19", "@Alberee_", '', "@gonzamontiel29", '',
    "@gastonedul", "@tucu_correa", "@SofiMMartinez", '', '',
    "@FranColapinto", '', "@kari_prince", '', "@MGallardoficial",
    "@__CarlitosTevez", "@aguerosergiokun", '', "@JulioFalcioniDT", '',
    '', '', '', '', "@BombitaDarin",
    '', "@p_lanzani", "@brimarcos_", '', "@lalioficial",
    "@chinasuarez", "@andrearincontop", "@FuriaScaglione", '', "@agusalbertario",
    "@sofimaure07", '', "@dieperetti", "@marcosginocchio", "@fedefarias5",
    "@mariannmartinez", '', "@AbelPintos", "@TiniStoessel", "@MariaBecerra22",
    "@Nicki_Nicole19", "@DukiSSJ", "@bizarrap", '', "@TruenoOficiaI", '', "@tiagopzk", "@emimernes_",
    "@rusherkingg", "@Flor_de_P", "@kheayf", "@LITkillah", "@NathyPeluso", "@sole_pastorutti", "@calamarooficial",
    "@FitoPaezMusica", '', "@octavioappogh", "@AlejandroSergi", "@julianagattas", "@Gustavocordera",
    "@ciroylospersas", '', "@cuervotinelli", "@mirthalegrand", "@Su_Gimenez", "@marley_ok",
    "@SANTIAGODELMORO", "@guidokaczkaofc", "@yanilatorre", "@AngeldebritoOk", "@rialjorge",
    "@mikaalafuente_", "@vivicanosaok", "@elbetocasella", "@andykusnetzoff", "@fantinofantino",
    "@sofijujuyok", "@silvinaescudero", "@pampitaoficial", "@valeriamazza", "@zairana", "@CHANOTB",
    "@dalmaradona", "", "@gabimichetti", "@fatimaflorez", "@martinbossi",
    "@miguegranados", "@Martinpdisalvo", "@CaroPardiaco0k", '', "@SpreenDMC", "@rodricarreraaa",
    "@delpotrojuan", "@paupareto", "@manuginobili", "@Pontifex_es",
    '', "@aymarlucha", "@momorelojero", '', "@gonchobanzas", "@GermanUsinger",
    "@Robleis01", "@Juakoooo", "@Pimpeano", "@LuquitaRodrigue", "@BoffeGP", "@robergalati", "@Santetitas",
    "@c0ker_", "@alferdez", '', "@alexcaniggia", "@AmelieGranata",
    "@lulipop07", "@AngieVelasco08", "@pinonfijo1", "@CFKArgentina", "@JMilei",
    "@horaciorlarreta", "@SergioMassa", "@PatoBullrich", "@mauriciomacri",
    "@Kicillofok", "@mariuvidal", '', "@danielscioli", "@JSchiaretti",
    "@enzoperezofi", '', "@crocraxker33", "@bhaviboi", '', "@RodolfoDonofrio",
    '', "@SolPerez", "@romimalaspina7", "@baronjimena", "@DtokeFree", "@PapoMcArg",
    "@Dementardox", "@maritobaracus", "@FlavioAzzaro", "@andresduka", "@morenabeltran10",
    "@libermanmartin", "@PolloVignolo", '', "@dflatorre", '',
    "@gustavohlopez", "@JPVarsky", '', "@milica_yb", "@wolffquique", "@AlinaMoine",
    "@Angelalerena", '', "@edufeiok", "@negrodolina", "@diegobranca",
    "@ACambiasoOK", "@majulluis", "@angeletchecopar", "@diegoleuco", "@NicolasOcchiato",
    "@florjazminpe16", '', "@martindardik", '', "@yayobelgrano", "@FFranGomez",
    "@natijota", "@santumaratea1", "@gregorossello", "@sofimorandiOk", "@paulina_cocina", "@brunenger",
    "@MazzaTomas", "@teloresumo", "@marianocanalok", "@OfeFernandez_", "@elpolacoOficial",
    "@wanditanara", "@MauroIcardi", "@pablitolescano", "@ysy__a", '', '',
    '', "@elisacarrio", "@Stolbizer", "@Marubotana_ok", '',
    "@NeoPistea_", "@Moria_Casan", "@Indio_Solari_ok", "@LuisVenturaSoy", "@Fraaanchuuu", "@Flordelav",
    "@cmjoficial", "@soycamnair_", "@MicaSuarez12"
]


eliminados = []  # Lista para almacenar los personajes eliminados

dia = 1

# Función para generar la imagen solo con los nombres
def generar_imagen_en_columnas(columnas=6):
    personajes_por_columna = len(nombres_famosos + eliminados) // columnas + 1
    
    # Tamaño de la imagen
    ancho_imagen = 1000  # Ajuste el ancho total de la imagen
    alto_imagen = 30 * personajes_por_columna + 50  # Ajustar la altura según la cantidad de personajes

    # Crear una nueva imagen blanca
    imagen = Image.new('RGB', (ancho_imagen, alto_imagen), color='white')
    draw = ImageDraw.Draw(imagen)
    
    # Cargar la fuente
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()

    # Posiciones para empezar a dibujar las columnas
    margen_x = 20
    margen_y = 20
    espacio_horizontal = (ancho_imagen - 2 * margen_x) // columnas
    
    # Listar todos los personajes y eliminados en orden alfabético
    todos_personajes = sorted(nombres_famosos + eliminados)
    
    # Dibujar cada personaje en la imagen distribuidos por columnas (solo los nombres)
    for index, personaje in enumerate(todos_personajes):
        columna = index // personajes_por_columna
        fila = index % personajes_por_columna
        x = margen_x + columna * espacio_horizontal
        y = margen_y + fila * 30

        if personaje in eliminados:
            # Fondo rojo para eliminados
            draw.rectangle([x, y, x + espacio_horizontal - 10, y + 25], fill='red')
            draw.text((x + 5, y), personaje, font=font, fill='white')
        else:
            # Texto normal para personajes restantes
            draw.text((x + 5, y), personaje, font=font, fill='black')

    # Crear la carpeta si no existe
    carpeta_destino = "C:/Users/felip/Dekstop/imagenes_generadas"
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Guardar la imagen en la carpeta especificada
    nombre_archivo = os.path.join(carpeta_destino, f'participantes_dia_{dia}.png')
    imagen.save(nombre_archivo)
    
    print(f"Imagen guardada correctamente en {nombre_archivo}")
    return nombre_archivo

    # Mostrar la imagen usando el visor de imágenes predeterminado
    #imagen.show()

# Función para eliminar un personaje y crear el tweet (con el nombre de usuario)
def eliminar_personaje():
    if len(nombres_famosos) > 1:
        global dia
        # Elegir eliminador y eliminado
        indice_eliminador = random.choice(range(len(nombres_famosos)))
        eliminador = nombres_famosos[indice_eliminador]
        usuario_eliminador = usuarios_twitter[indice_eliminador]

        posibles_eliminados = [i for i in range(len(nombres_famosos)) if i != indice_eliminador]
        indice_eliminado = random.choice(posibles_eliminados)
        eliminado = nombres_famosos[indice_eliminado]
        usuario_eliminado = usuarios_twitter[indice_eliminado]

        # Eliminar al personaje
        nombres_famosos.pop(indice_eliminado)
        usuarios_twitter.pop(indice_eliminado)
        eliminados.append(eliminado)

        # Crear mensaje del tweet
        if len(nombres_famosos)==1:
                mensaje = f"Día {dia} \n{eliminador} ({usuario_eliminador}) eliminó a {eliminado} ({usuario_eliminado}). La guerra ha terminado. \n \n''#ArgentinaWarBot''"
                print(mensaje)
        elif len(nombres_famosos)>1:
            mensaje = f'Día {dia} \n{eliminador} ({usuario_eliminador}) eliminó a {eliminado} ({usuario_eliminado}). Quedan {len(nombres_famosos)} famosos en pie.\n \n''#ArgentinaWarBot''\n''#VolvioWarBot'''
            print(mensaje)  # Solo para depuración

        # Generar la imagen actualizada
        ruta_imagen = generar_imagen_en_columnas()

        # Subir la imagen a Twitter y publicar el tweet
        if os.path.exists(ruta_imagen):
            print(f"La imagen {ruta_imagen} existe. Preparando para subirla.")
            try:
        # Subir la imagen usando la API v1.1
                media = api.media_upload(ruta_imagen)
                media_id = media.media_id_string

        # Publicar el tweet con el texto y la imagen usando la API v2
                response = client.create_tweet(text=mensaje, media_ids=[media_id])
                print(f"Tweet publicado con éxito: Día {dia}, ID del tweet: {response.data['id']}")
        
            except tweepy.TweepyException as e:
                print(f"Error al intentar enviar el tweet: {e}")
        else:
            print(f"Error: La imagen {ruta_imagen} no existe.")
        
        dia += 1

        # Aquí puedes agregar el código para publicar el tweet
        # api.update_status(status=mensaje, media_ids=[media.media_id_string])
    else:
        # Cuando queda un solo personaje, anunciar el ganador
        ganador = nombres_famosos[0]
        usuario_ganador = usuarios_twitter[0]
        mensaje = f"¡La guerra ha terminado! El ganador es {ganador} ({usuario_ganador})"
        print(mensaje)

        # Generar la imagen final
        generar_imagen_en_columnas()

        # Aquí puedes agregar el código para publicar el tweet final
        # api.update_status(status=mensaje, media_ids=[media.media_id_string])

# Ejemplo de eliminación de un personaje
# while len(nombres_famosos and usuarios_twitter)>1:
#     eliminar_personaje()
if __name__ == "__main__":
    # Crear el programador
    scheduler = BackgroundScheduler()

    # Zona horaria de Argentina
    argentina_tz = pytz.timezone('America/Argentina/Buenos_Aires')

    # Programar la función eliminar_personaje() para que se ejecute cada hora desde las 10 am hasta las 10 pm
    trigger = CronTrigger(hour='10-22', minute=0, timezone=argentina_tz)
    job = scheduler.add_job(eliminar_personaje, trigger)
    print("Programada eliminación cada hora entre las 10:00 y las 22:00 hora argentina.")

    # Iniciar el programador
    scheduler.start()
    print("El programador ha iniciado. Esperando próximas ejecuciones...")

    try:
        # Mantener el script en ejecución
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        # Apagar el programador
        scheduler.shutdown()
        print("El programador se ha detenido.")
print(f"¡La guerra ha terminado! {nombres_famosos[0]} {usuarios_twitter[0]} ha sobrevivido y es el ganador de #ArgentinaWarBot" )