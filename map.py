import pandas
import folium

df = pandas.read_csv('volcanoes.txt')
lat = df['LAT']
lon = df['LON']
elv = df['ELEV']
nm = df['NAME']

html = """
        Volcano:<br>
        <a target="_blank" href="http://www.google.com/search?q=%%22%s%%22">%s</a><br>
        Height: %s m
        """

usa_map = folium.Map(location=[40, -100], zoom_start=4, tiles='Stamen Terrain')

for lt, ln, el, name in zip(lat, lon, elv, nm):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=80)
    folium.Marker([lt, ln], popup=folium.Popup(iframe)).add_to(usa_map)

usa_map.save('index.html')
