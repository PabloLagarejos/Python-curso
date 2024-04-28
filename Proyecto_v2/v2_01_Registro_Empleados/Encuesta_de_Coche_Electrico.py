import pandas as pd
import json
from datetime import date
from datetime import datetime
import numpy as np
import csv
import seaborn as sns
import matplotlib.pyplot as plt

#Exportar la encuesta en formato CSV
def guardar_en_csv(encuestados):
    with open('encuestados.csv', 'a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        if archivo_csv.tell() == 0:
            writer.writerow(['Fecha','Marca', 'Vivienda', 'garaje', 'Codigo_Postal', 'Anio','Media'])  # Encabezados de las columnas
        for encuestado in encuestados:
            writer.writerow(encuestado.values())

#Exportar la encuesta en formato JSON
def guardar_en_json(encuestados):
    with open('encuestados.json', 'w') as archivo_json:
        json.dump(encuestados, archivo_json, indent=4)


def cargar_preguntas():
    preguntas = []
    with open('preguntas.txt', 'r', encoding='utf8') as file:
        for line in file:
            preguntas.append(line.strip())
    return preguntas

def ingresar_encuesta(preguntas):
    fecha = datetime.now().strftime('%d/%m/%Y')
    marca = input("¿Cual es la marca de su coche?: ")
    vivienda = input("¿Vive usted en una vivienda unifamiliar?:  ")
    garaje = input("¿Tiene usted garaje?: ")
    codigo_postal = input("¿Cuál es su código postal?: ")
    anio = input("¿De que año es su coche?: ")
    print("------- Califique las siguiente preguntas del 1 al 5 -------")

    respuestas = []
    media = []
    for i, pregunta in enumerate(preguntas, 1):
        respuesta = int(input(f"{i}{pregunta} "))
        respuestas.append(respuesta)
    encuestado = {
        'Fecha': fecha,
        'Marca': marca,
        'Vivienda': vivienda,
        'garaje': garaje,
        'Codigo_Postal': codigo_postal,
        'Anio': anio,
        **{f"Pregunta {i}": respuestas[i-1] for i in range(1, len(preguntas) + 1)}

    }
    encuestado = {'Media': media}
    return encuestado

def graficar_strip_plot(encuestados):
    df = pd.DataFrame(encuestados)
    df['Anio'] = pd.to_numeric(df['Anio'])  # Convertir el año a numérico
    sns.stripplot(data=df, x='Marca', y='Anio', hue='Codigo_Postal', jitter=True)
    plt.title('Strip Plot: Año del Coche por Marca y Código Postal')
    plt.xlabel('Marca')
    plt.ylabel('Año del Coche')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend(title='Código Postal', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()


def main():
    preguntas = cargar_preguntas()
    encuestados = []
    while True:
        opcion = input("¿Desea ingresar hacer la encuesta? (s/n): ")
        if opcion.lower() == 's':
            encuestado = ingresar_encuesta(preguntas)
            encuestados.append(encuestado)
        else:
            break
    guardar_en_csv(encuestados)
    guardar_en_json(encuestados)
    graficar_strip_plot(encuestados)
    print("¡Gracias por participar en nuestra encuesta de satisfaccion de coches electricos!")
    print("Encuestados guardados exitosamente.")

now = datetime.now()
print(now)


datos='encuestados.csv'
medias = []
with open(datos, 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)
    for row in lector_csv:
        valores = [float(valor) for valor in row[6:]]
        media = sum(valores) / len(valores) if valores else 0
        encuestado = {'Media': media}
        medias.append(media)
for i, media in enumerate(medias, start=1):
    print("La media de la fila", i, "es:", media)
import csv
marcas = []
with open(datos, 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)
    for row in lector_csv:
        marca = row[1].split()  # Utilizamos el método split para dividir la cadena en palabras
        marcas.extend(marca)  # Utilizamos extend en lugar de append para agregar las palabras individualmente
print("marcas:", marcas)
print("medias:", medias)
grafica_medias = sns.scatterplot(x=medias, y=marcas)
plt.show()


if __name__ == '__main__':
    main()



