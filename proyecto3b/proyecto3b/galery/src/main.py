import flet as ft


def main(page: ft.Page):
    page.title="Galeria"
    page.bgcolor=ft.Colors.BLACK38

    personajes = [
        {
            "nombre": "Antony carmine",
            "edad": "18",
            "historia":"El Soldado Anthony Carmine fue el hermano de Benjamin Carmine y Clayton Carmine. Fue el miembro más joven de Delta-Uno, Anthony compensa su falta de experiencia con un entusiasmo desenfrenado y verdadero respeto por los veteranos de guerra como Marcus y Dom",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyecto/refs/heads/main/antony.jpeg"     
        },  
        { 
            "nombre": "",
            "edad": "no especificada",
            "historia": "La Primera Ministra Anya Stroud fue la primera ministra de la restablecida Coalición de Gobiernos Ordenados y una oficial retirada del Ejército de la CGO durante las Guerras del Péndulo y la Guerra Locust. Hija de la mayor Helena Stroud, Anya se unió al ejército de la CGO para seguir los pasos de su madre. ",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyecto/refs/heads/main/anya.jpeg", 
        },
        {
            "nombre": "marcus fenix",
            "edad": "63",
            "historia": "Marcus Michael Fenix, Sargento del Ejército de la Coalición de Gobiernos Ordenados (CGO), protagonista y personaje principal de la primera saga del universo de Gears of War. Un muy reconocido militar durante las Guerras del Péndulo, ganó la Estrella Embry, la más grande condecoración de todas, por sus grandes hazañas en la Batalla de los Campos de Aspho",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyecto/refs/heads/main/marcus.jpeg",
        },  
        {
            "nombre": "benjamin",
            "edad": "18",
            "historia": "Benjamin Ben Carmine (Placa: CGO CSID 83B186-22AO3-SF), Soldado de las Fuerzas Armadas de la Coalición de Gobiernos Ordenados, fue un Gear que sirvió a la Coalición durante la Guerra Locust. Llamado Carmine por su equipo y Mequetrefe por sus hermanos,",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyecto/refs/heads/main/benjamin.webp",            
            
        },
        {
            "nombre": "damon baird",
            "edad": "35",
            "historia": "El Cabo Damon S. Baird, anteriormente Teniente, fue un soldado Gear, genio en varios campos técnicos, mecánicos y científicos. Es experto en recolectar, analizar y descifrar tanto armas Locust, como otros tipos de equipos, artefactos y documentos, también se destaca por ser un gran ingeniero,",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyecto/refs/heads/main/damon.jpeg",         
        },
        {
            "nombre": "dominic santiago",
            "edad": "no establecida",
            "historia": "Dominic Dom Santiago era un cabo de las fuerzas armadas de la Coalición de Gobiernos Ordenados (CGO). Es un duro guerrero que posee una actitud positiva incluso en los peores momentos.",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyecto/refs/heads/main/dominic.jpeg",            
        },
        {
            "nombre": "garron pudak",
            "edad": "80",
            "historia": "El Jefe Garron Paduk era soldado raso  del Ejército de la Coalición de Gobiernos Ordenados  y miembro del Escuadrón Kilo . Durante las Guerras del Péndulo , sirvió como Mayor [ 4 ] en la Infantería de la Unión de Repúblicas Independientes en su tierra natal,",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyecto/refs/heads/main/garron.jpeg",
        },   
        {
            "nombre": "jd fenix",
            "edad": "22",
            "historia": "El Capitán James Dominic Fenix, [3], a menudo llamado JD por sus amigos y compañeros de escuadrón, era un soldado Gear e hijo del legendario Marcus Fenix y Anya Stroud.",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyecto/refs/heads/main/garron.jpeg",           
        },   
        {
            "nombre": "kait diaz",
            "edad": "22",
            "historia": "Kait Díaz es una joven Forastera que nació y se crió fuera de las ciudades amuralladas que protegen a gran parte de la humanidad. Kait es co-protagonista de Gears of War 4 y protagonista de Gears 5.",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyecto/refs/heads/main/kait.jpeg",            
        },
        {
            "nombre": "sid redburd",
            "edad": "79",
            "historia": "El Mayor Sid Redburn era un Gear del Ejército de la CGO y denunciante de los experimentos poco éticos en el Centro de Investigación de Nueva Esperanza . Al principio de su carrera, el soldado Redburn estuvo destinado en Nueva Esperanza,",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/proyecto/refs/heads/main/sid.jpeg",            
        },
    ]

    indice_actual=[0]

    contenedor=ft.Container(
        content=ft.Column([]),
        width=500,
        height=580,
        bgcolor=ft.Colors.BLUE_300,
        alignment=ft.alignment.center,
        padding=30
    )

    boton_siguiente = ft.ElevatedButton(text="Siguiente sobreviviente")

    def mostrar_personaje():
        personaje=personajes[indice_actual[0]]
        contenedor.content=ft.Column([
            ft.Image(src=personaje["imagen"],width=300,height=300,fit=ft.ImageFit.CONTAIN),
            ft.Text(personaje["nombre"],size=20,weight=ft.FontWeight.BOLD),
            ft.Text(f"Edad: {personaje ['edad']}",size=16),
            ft.Text(f"Historia: {personaje ["historia"]}",size=14,italic=True)
        ],alignment=ft.MainAxisAlignment.CENTER)
        
        if indice_actual[0]==len(personajes)-1:
            boton_siguiente.text="Volver al inicio"
        else:
            boton_siguiente.text="Siguiente personaje"
        page.update()

    def siguiente_click(e):
        indice_actual[0]=(indice_actual[0]+1)%len(personajes)
        mostrar_personaje()
    boton_siguiente.on_click=siguiente_click



    page.add(
        ft.Container(
            content=ft.Column([
                contenedor,
                boton_siguiente
            ],alignment=ft.MainAxisAlignment.CENTER,
              horizontal_alignment=ft.CrossAxisAlignment.CENTER,
              spacing=20
        ),

            alignment=ft.alignment.center,
            expand=True
        )
    ) 
    mostrar_personaje()


ft.app(main)
