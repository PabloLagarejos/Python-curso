# En este archivo hacemos un menu de como quieres hacer tu sandwich

# Estas son las listas de los elementos para hacer el sandwich.
panes = ["Pan de molde ","Pan integral","Pan de leche","Baguette","Pan brioche","Pan de pita"]
carnes = ["Pavo","Jamon york","Chorizo","Pollo","Jamon serrano"]
quesos = ["Havarti","Gouda","Queso de cabra","Queso de oveja"]
vegetales = ["lechuga","maiz","aceituna","tomate","pimiento","cebolla picada","cebolla caramelizada"]
salsas = ["Ketchup","Barbacoa","Mayonesa","Salsa de tomate","mostaza"]

# Estas son las variables donde se van a guardar la eleccion de cada elemento del sandwich que elija el usuario.
pan = ""
carne = ""
queso = ""
vegetal1 = ""
vegetal2 = ""
salsa = ""

# Usaremos estos bool, que se volveran True cuando el usuario escoja un tipo de pan, algo de comida y una salsa.
# Sino escoge las tres al final del archivo le dirá que no ha cogido suficientes elementos
pan1 = False
comida1 = False
salsa1 = False

# Aqui se ven las listas de los precios de cada lista de elemento, en orden por cada elemento.
preciopan = [0.5,0.75,1,1,1.5,1.5]
preciocarne = [0.75,0.75,1,1.5,1.25]
precioqueso = [0.75,1,1,1]
preciovegetal = [0.10,0.05,0.05,0.05,1,0.5,1]
preciosalsa = [0.5,0.75,0.75,0.5,0.5]

# Se guardaran en unas variables los precios del elemento que escoja el usuario
ppan = 0
pcarne = 0
pqueso = 0
pvegetal1 = 0
pvegetal2 = 0
psalsa = 0


# Empezamos en un bucle que tiene 4 opciones. Las 3 primeras son los elementos del sandwich y la cuarta es para salir.
while True:
    print("Quieres hacer un sadwich, elige los distintos tipos de alimentos y condimentos que quieres poner.")
    print("Tiene que llevar al menos un tipo de pan, algo de comida y una salsa. Cuando lo tengas todo dale a salir.")
    print("Menú:")
    print("1. Elegir tipo de pan ")
    print("2. Elegir la comida")
    print("3. Elegir la salsa")
    print("4. Salir")
    # Aqui recoge la opcion que escoja el usuario.
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1 :
        # Si pulsamos 1 entraremos en los tipos de panes.
        print("Has elegido tipo de pan. ¿Que tipo de pan quieres usar?")
        # Pongo un menu que tiene las distintas opciones de pan
        # Aqui y en las opciones de comida y salsas he hecho un for para poder recorrer los elementos y sus precios
        # En cant recogemos la cantidad que va ir subiendo en el for de abajo para poder recorrer todo.
        cant= 0
        for i in panes:
            print(cant + 1,i,preciopan[cant],"$")
            cant += 1
        # Abajo del menu del for, recoge la opcion del usuario.
        pansolucion = int(input("Seleccione una opción: "))

        # Recoge la opcion. Si no ha pulsado la opcion tendra que repetirlo.
        # Si la ha pulsado correctamente pondra la opcion elegida con su precio y la guardara.
        # Esto pasa en la de comida y en la de salsas.
        if (pansolucion < 7) & (pansolucion > 0):
            print("El tipo de pan es ",panes[pansolucion - 1], "y su precio es ",preciopan[pansolucion - 1])
            ppan = preciopan[pansolucion - 1]
            pan = panes[pansolucion - 1]
            # Aqui se vuelve True, con lo cual ya ha elegido pan.
            # En las otras pasa la mismo pero con comida y salsas.
            pan1 = True
        else:
            print("Esa opcion no existe vuelve al menu.")

    elif opcion == 2 :
        # Tiene 4 opciones de comida y dentro de esas opciones hay mas como los tipos de pan de arriba.
        # Las opciones de dentro y lo usado es igual que la de tipos de pan.
        print("Has elegido comida. Elige que quieres poner carne,queso, primer vegetal o segundo vegetal. No hace falta que lleve todo pero sí al menos uno de ellos.")
        print("1. carne")
        print("2. queso")
        print("3. Primer vegetal")
        print("4. Segundo vegetal ")
        comidasolucion = int(input("Seleccione una opción: "))

        if comidasolucion == 1:
            # Las opciones de dentro y lo usado es igual que la de tipos de pan.
            print("Has elegido carne. Ahora elige el tipo de carne:")
            cant = 0
            for i in carnes:
                print(cant + 1, i, preciocarne[cant], "$")
                cant += 1
            carnesolucion = int(input("Seleccione una opción: "))

            if (carnesolucion < 6) & (carnesolucion > 0):
                print("El tipo de carne es ", carnes[carnesolucion - 1],"y su precio es ",preciocarne[carnesolucion - 1])
                pcarne = preciocarne[carnesolucion - 1]
                carne = carnes[carnesolucion - 1]
                comida1 = True
            else:
                print("Esa opcion no existe vuelve al menu.")

        elif comidasolucion == 2:
            print("Has elegido queso. Ahora elige el tipo de queso:")
            cant = 0
            for i in quesos:
                print(cant + 1, i, precioqueso[cant], "$")
                cant += 1
            quesosolucion = int(input("Seleccione una opción: "))

            if (quesosolucion < 5) & (quesosolucion > 0):
                print("El tipo de queso es ", quesos[quesosolucion - 1] ,"y su precio es ",precioqueso[quesosolucion - 1])
                pqueso = precioqueso[quesosolucion - 1]
                queso = quesos[quesosolucion - 1]
                comida1 = True
            else:
                print("Esa opcion no existe vuelve al menu.")

        elif comidasolucion == 3:
            print("Has elegido primer vegetal. Ahora elige el tipo de vegetal quieres poner:")
            cant = 0
            for i in vegetales:
                print(cant + 1, i, preciovegetal[cant], "$")
                cant += 1
            vegetalsolucion = int(input("Seleccione una opción: "))

            if (vegetalsolucion < 8) & (vegetalsolucion > 0):
                print("El tipo de vegetal es ", vegetales[vegetalsolucion - 1] ,"y su precio es ",preciovegetal[vegetalsolucion - 1])
                pvegetal1 = preciovegetal[vegetalsolucion - 1]
                vegetal1 = vegetales[vegetalsolucion - 1]
                comida1 = True
            else:
                print("Esa opcion no existe vuelve al menu.")

        elif comidasolucion == 4:
            print("Has elegido segundo vegetal. Ahora elige el tipo de vegetal quieres poner:")
            cant = 0
            for i in vegetales:
                print(cant + 1, i, preciovegetal[cant], "$")
                cant += 1
            vegetalsolucion = int(input("Seleccione una opción: "))

            if (vegetalsolucion < 8) & (vegetalsolucion > 0):
                print("El tipo de vegetal es ", vegetales[vegetalsolucion - 1] ,"y su precio es ",preciovegetal[vegetalsolucion - 1])
                pvegetal2 = preciovegetal[vegetalsolucion - 1]
                vegetal2 = vegetales[vegetalsolucion - 1]
                comida1 = True
            else:
                print("Esa opcion no existe vuelve al menu.")

        else:
            print("Esa opcion no existe vuelve al menu.")

    elif opcion == 3:
        # Las opciones de dentro y lo usado es igual que la de tipos de pan.
        print("Has elegido salsa. Ahora elige el tipo de salsa:")
        cant = 0
        for i in salsas:
            print(cant + 1, i, preciosalsa[cant], "$")
            cant += 1
        salsasolucion = int(input("Seleccione una opción: "))

        if ( salsasolucion < 6) & (salsasolucion > 0):
            print("El tipo de salsa es ", salsas[salsasolucion- 1] ,"y su precio es ",preciosalsa[salsasolucion - 1])
            psalsa = preciosalsa[salsasolucion- 1]
            salsa = salsas[salsasolucion- 1]
            salsa1 = True
        else:
            print("Esa opcion no existe vuelve al menu.")
    elif opcion == 4:
        # Si le da al 4 se sale del menu.
        print("Has elegido salir")
        break
    else:
        # Si le da a otro boton volvera al bucle del menu.
        print("Esa opcion no existe vuelve a probar.")

# Al terminar recoge todos los precios y los suma.
suma = ppan + pcarne + pqueso + pvegetal1 + pvegetal2 + psalsa

# Si ha escogido pan comida y salsa te dirá de que es tu sandwich y cuanto vale.
if(pan1 == True) & (comida1 == True) & (salsa1 == True):
    # Ponemos las variables de los elementos elegidos y ponemos el precio final.
    print(f"Tu sandwich lleva: {pan} {carne} {queso} {vegetal1} {vegetal2} {salsa} y cuesta {suma} $")
# Sino Te dirá que no has escogido el sandwich completo o simplemente le diste a salir.
else:
    print("Has salido o no has elegido el sandwich completo.")

with open("sandwich.html", "w") as file:
    # Escribir el contenido HTML en el archivo
    file.write("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sandwich</title>
        <style>
            /* Estilos para el contenedor del sándwich */
            .sandwich {
                width: 300px; /* Ancho del contenedor */
                height: 200px; /* Altura del contenedor */
                background-color: #f8d7da; /* Color de fondo del sándwich */
                border: 2px solid #dc3545; /* Borde del contenedor */
                margin: 50px auto; /* Margen para centrar el contenedor */
                padding: 20px; /* Espaciado interno del contenedor */
            }

            /* Estilos para los ingredientes del sándwich */
            .ingredientes {
                font-size: 16px; /* Tamaño de fuente */
                margin-bottom: 10px; /* Margen inferior */
            }
        </style>
    </head>
    <body>
        
        <div class="sandwich">
            <!-- Aquí se mostrarán los ingredientes del sándwich -->
            <p class="ingredientes">Pan: <span id="pan"></span></p>
            <p class="ingredientes">Carne: <span id="carne"></span></p>
            <p class="ingredientes">Queso: <span id="queso"></span></p>
            <p class="ingredientes">Vegetal 1: <span id="vegetal1"></span></p>
            <p class="ingredientes">Vegetal 2: <span id="vegetal2"></span></p>
            <p class="ingredientes">Salsa: <span id="salsa"></span></p>
            <p class="ingredientes">Precio: <span id="precio"></span></p>
        </div>
    </body>
    </html>
    """)

# Abre el archivo HTML en el navegador web
import webbrowser

webbrowser.open("sandwich.html")
# Aquí está tu código Python existente...

# Obtén los ingredientes seleccionados por el usuario
ingredientes_seleccionados = {
    "Pan": pan,
    "Carne": carne,
    "Queso": queso,
    "Vegetal 1": vegetal1,
    "Vegetal 2": vegetal2,
    "Salsa": salsa,
    "Precio": suma
}
# Aquí está tu código Python existente...

# Crear un archivo HTML
with open("sandwich.html", "w") as file:
    # Escribir el contenido HTML en el archivo
    file.write(f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sandwich</title>
        <style>
            /* Estilos para el contenedor del sándwich */
            .sandwich {{
                width: 50%;
                margin: 0 auto;
                padding: 20px;
                background-color: #f7f7f7;
                border: 2px solid #ddd;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}

            /* Estilos para los ingredientes del sándwich */
            .ingredientes {{
                font-size: 18px;
                margin-bottom: 10px;
            }}

            /* Estilos para el título */
            h1 {{
                text-align: center;
                font-size: 24px;
                color: #333;
            }}

            /* Estilos para el precio */
            .precio {{
                font-size: 20px;
                font-weight: bold;
                color: #dc3545;
            }}
        </style>
    </head>
    <body>
        <h1>Tu Sandwich Personalizado</h1>
        <img src="sandwich.jpg" alt="Sandwich" style="display: block; margin: 0 auto; width: 50%;" />
        <div class="sandwich">
            <!-- Aquí se mostrarán los ingredientes del sándwich -->
            {"".join([f'<p class="ingredientes">{key}: <span id="{key.lower()}">{value}</span></p>' for key, value in ingredientes_seleccionados.items()])}
            <p class="ingredientes">Precio Total: <span class="precio" id="precio">{suma} $</span></p>
        </div>
        <script>
            // Actualizar el contenido de las etiquetas span con los ingredientes seleccionados
            const ingredientes = {ingredientes_seleccionados};
            Object.entries(ingredientes).forEach(([key, value]) => {{
                document.getElementById(key.toLowerCase()).textContent = value;
            }});
        </script>
    </body>
    </html>
    """)

# Abre el archivo HTML en el navegador web
import webbrowser
webbrowser.open("sandwich.html")