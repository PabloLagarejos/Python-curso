import folium
import pandas as pd
import webbrowser
from folium.plugins import HeatMap
import webbrowser
import tkinter as tk
# Datos de latitud y longitud
data = {
    'Comunidad': ['Andalucía', 'Aragón', 'Asturias', 'Baleares', 'Canarias', 'Cantabria', 'Castilla y León',
                  'Castilla-La Mancha', 'Cataluña', 'Extremadura', 'Galicia', 'La Rioja', 'Madrid', 'Murcia', 'Navarra',
                  'País Vasco', 'Valencia'],
    'Latitud': [37.3833, 41.6561, 43.3614, 39.5342, 28.2916, 43.4634, 41.8333, 39.8628, 41.5912, 39.4762, 42.5751,
                42.2871, 40.4168, 37.9922, 42.6954, 43.2627, 39.4699],
    'Longitud': [-5.9833, -0.8773, -5.8593, 2.8577, -16.6291, -3.8044, -4.8333, -4.0273, 1.5209, -6.3703, -8.1339,
                 -2.5396, -3.7038, -1.1307, -1.6761, -2.9253, -0.3763]
}
df = pd.DataFrame(data)
# Temperaturas medias mensuales por comunidad
temperaturas = {
    'Andalucía': [12.5, 13.2, 15.8, 18.6, 22.4, 27.9, 33.0, 33.2, 29.0, 23.9, 17.5, 13.4],
    'Aragón': [5.2, 6.3, 9.1, 12.0, 15.5, 20.7, 25.2, 25.1, 21.4, 16.5, 10.9, 6.8],
    'Asturias': [6.8, 7.3, 8.5, 10.2, 13.4, 17.1, 20.2, 21.0, 19.0, 14.3, 10.0, 7.1],
    'Baleares': [13.6, 14.2, 15.8, 18.3, 21.2, 25.1, 28.7, 29.2, 26.7, 22.0, 17.2, 14.1],
    'Canarias': [18.3, 18.9, 20.1, 21.6, 24.1, 27.0, 29.3, 30.4, 29.0, 26.1, 21.7, 19.0],
    'Cantabria': [6.5, 7.2, 8.6, 11.2, 14.5, 18.3, 21.6, 21.8, 19.8, 14.7, 9.7, 6.8],
    'Castilla y León': [4.3, 5.2, 7.4, 9.4, 12.4, 16.3, 20.0, 20.7, 18.1, 12.4, 8.3, 5.1],
    'Castilla-La Mancha': [6.8, 7.5, 10.3, 13.0, 17.1, 22.2, 28.0, 28.5, 24.5, 18.8, 13.0, 8.4],
    'Cataluña': [8.9, 9.2, 11.5, 13.8, 17.4, 21.9, 26.0, 26.0, 23.0, 18.7, 13.1, 9.1],
    'Extremadura': [11.2, 12.3, 15.0, 17.9, 21.4, 27.1, 31.5, 31.6, 28.1, 22.9, 15.8, 11.9],
    'Galicia': [5.4, 6.2, 8.7, 11.5, 14.3, 18.5, 23.1, 23.7, 20.9, 15.5, 9.9, 6.5],
    'La Rioja': [3.6, 4.1, 6.2, 8.5, 11.6, 15.2, 19.3, 19.6, 17.4, 12.3, 7.7, 4.3],
    'Madrid': [6.1, 7.2, 10.1, 13.2, 17.6, 22.9, 28.2, 28.5, 24.1, 18.1, 11.9, 8.0],
    'Murcia': [8.2, 9.5, 11.6, 15.6, 20.2, 25.8, 29.6, 30.0, 26.5, 21.4, 14.8, 10.2],
    'Navarra': [4.8, 5.3, 7.2, 9.5, 12.7, 17.3, 22.7, 23.1, 19.6, 14.3, 10.2, 6.6],
    'País Vasco': [6.0, 6.4, 8.5, 11.3, 14.0, 18.3, 21.9, 22.2, 19.3, 15.1, 10.5, 7.3],
    'Valencia': [10.1, 10.9, 13.4, 16.5, 20.3, 24.6, 29.2, 29.4, 25.7, 20.7, 15.0, 10.7]
}

def asignar_color(temperatura):
    if temperatura < 10:
        return 'blue'
    elif temperatura < 20:
        return 'green'
    elif temperatura < 30:
        return 'orange'
    else:
        return 'red'

# Crear un mapa para cada mes
for mes in range(1, 13):
    # Crear el mapa centrado en España
    m = folium.Map(location=[40.4168, -3.7038], zoom_start=6, tiles='cartodbpositron')
    # Agregar marcadores y popups para cada comunidad
    for index, row in df.iterrows():
        comunidad = row['Comunidad']
        latitud = row['Latitud']
        longitud = row['Longitud']
        temperatura_media = temperaturas[comunidad][mes - 1]
        color = asignar_color(temperatura_media)
        popup_text = f'{comunidad}: {temperatura_media}°C'
        folium.Marker([latitud, longitud], icon=folium.Icon(color=color), popup=popup_text).add_to(m)
    # Agregar heatmap de temperaturas para este mes
    heat_data = [[row['Latitud'], row['Longitud'], temperaturas[row['Comunidad']][mes - 1]] for index, row in
                 df.iterrows()]
    HeatMap(heat_data).add_to(m)
    # Guardar el mapa en un archivo HTML
    m.save(f"mapa_temperaturas_mes_{mes}.html")

# Función para abrir la diapositiva correspondiente al mes
def abrir_diapositiva(mes):
    nombre_archivo = f"mapa_temperaturas_mes_{mes}.html"
    webbrowser.open(nombre_archivo)

# Diccionario con los nombres de los meses
nombres_meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}
# Crear la interfaz gráfica
root = tk.Tk()
root.title("Navegador de Diapositivas")
# Crear botones para cada mes con sus nombres correspondientes
for mes in range(1, 13):
    nombre_mes = nombres_meses[mes]
    boton_mes = tk.Button(root, text=f"{nombre_mes}", command=lambda m=mes: abrir_diapositiva(m))
    boton_mes.pack(pady=5)
root.mainloop()

"""
m.save(r'C:\pablo\example.html')
webbrowser.open(r'C:\pablo\example.html')

"""