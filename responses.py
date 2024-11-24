import re

def process_message(message, response_array, response):
    # Dividir el mensaje y la puntuaciòn dentro del array
    list_message = re.findall(r"[\w']+|[.,¡¿!?;]", message.lower())
    
    # Puntua el conjuntoo de palabras en el mensaje
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1
    
    # Retorna las respuestas y el score de la respuesta
    print(score, response) # Esto es solamente para debbuging
    return [score, response]

#Menu
menu = """
🍽️ Menú de Comidas y Bebidas 🍹

Entradas:
- 🥗 Ensalada César: $1500
- 🥟 Empanadas Mixtas (3 unidades): $800

Platos Principales:
- 🥩 Asado Criollo: $3500
- 🍝 Spaghetti a la Boloñesa: $2800

Postres:
- 🍰 Cheesecake de Frutos Rojos: $1200
- 🍮 Flan Casero con Dulce de Leche: $1000

Bebidas:
- 🥤 Limonada con Menta y Jengibre: $800
- 🍷 Vino Tinto Malbec (Copa): $1000
- 🍸 Gin Tonic: $2300

¡Esperamos que disfrutes de nuestras opciones!
"""

# Variable para almacenar reservas

reservas = []

def get_response(message):
    #Agrega tu respuesta personalizada
    response_list = [
        process_message(message, ['hola', 'hey', 'buenas', 'holis'], 'Hola! ¿Cómo estás?'),
        process_message(message, ['bien', 'muy', 'ok', 'tranquilo', 'tranqui', 'normal'], 'Bien, ¿estás listo para pedir?'),
        process_message(message, ['bye', 'chau', 'adios', 'hasta luego'], 'Chau, que la pases bien!!'),
        process_message(message, ['como', 'cómo', 'estas', 'estás', 'vos'], 'Yo estoy muy bien, muchas gracias!'),
        process_message(message, ['cual', 'es', 'tu', 'nombre', 'como', 'te', 'llamas'], 'Me llamo Bot Brumsweich'),
        process_message(message, ['quiero', 'la', 'carta', 'menu', 'dame', 'comidas', 'bebidas'], menu),
        process_message(message, ['reserva', 'reservar', 'quiero', 'hacer', 'una', 'mesa'], 'Claro, dime para cuántas personas es la reserva.'),
        process_message(message, ['me', 'puedes', 'ayudar', 'help', 'me'], 'Sí, en qué puedo ayudarte'),
        process_message(message, ['quiero', 'la', 'carta', 'carta', 'dame', 'la'], 'Claro, aquí tienes la carta'),
        process_message(message, ['cual', 'es', 'la', 'direccion', 'dime', 'la', 'ubicacion', 'donde', 'el', 'lugar'], 'Nuestra ubicación es: [Ver en Google Maps](https://www.google.com/maps?q=-31.528186,-68.573394)'),
        process_message(message, ['que', 'tiene', 'el', 'gin', 'lleva'], 'El gin 🍸 es una bebida alcohólica destilada, generalmente hecha de cereales 🍚 y aromatizada con bayas de enebro 🌿, lo que le da un sabor fresco y herbal. Se disfruta principalmente en cócteles como el gin tonic 🍹, y puede tener notas de cítricos 🍊, especias 🌶️ y hierbas 🌱, según la variedad.'),
        process_message(message, ['cuanto', 'vale', 'el', 'gin', 'dime', 'valor'], 'El gin vale $2300'),
        process_message(message, ['que', 'tiene', 'el', 'vino', 'lleva'], 'Un vino Malbec 🍷: intenso, con notas de frutas rojas 🍒 y negras 🫐, toques de vainilla 🍦 y especias 🌿. Ideal para carnes asadas 🍖 y momentos especiales ✨.'),
        process_message(message, ['cuanto', 'sale', 'vale', 'el', 'vino', 'dime', 'valor'], 'El vino Malbec (Copa) vale $1000'),
        process_message(message, ['tengo', 'reservar', 'mesa'], 'Claro dime tu nombre'),
    ]
    
    #Revisa todas las respuestas score y retorna la mejor conexion posible
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])
        
    #Obtener el mayor valor posible para la mejor respuesta y almacenarlo dentro de una variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]
    
    #Retorna el matching response al usuario 
    if winning_response == 0:
        bot_response = 'Yo no logro entender lo que escribiste'
    else:
        bot_response = matching_response[1]
        
    print('La respuesta del Bot:', bot_response)
    return bot_response

#prueba

user_message = "Quiero reservar para 3 personas"
print(get_response(user_message))