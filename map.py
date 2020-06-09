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

def elev_color(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'

def pop_color(pop):
    if pop < 10000000:
        return 'green'
    elif pop < 100000000:
        return 'orange'
    else:
        return 'red'

usa_map = folium.Map(location=[40, -100], zoom_start=4, tiles='Stamen Terrain')

fg = folium.FeatureGroup(name='My Map')

for lt, ln, el, name in zip(lat, lon, elv, nm):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=80)
    markers = folium.CircleMarker(
        location = [lt, ln],
        popup=folium.Popup(iframe),
        radius=5,
        stroke=False,
        fill_opacity=0.7,
        fill_color=elev_color(el))
    fg.add_child(markers)

fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
    style_function= lambda x: {'fillColor': pop_color(x['properties']['POP2005'])}))

usa_map.add_child(fg)

usa_map.save('index.html')
