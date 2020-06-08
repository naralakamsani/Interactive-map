import folium
import pandas


data = pandas.read_csv("Volcanoes.txt")#reads the volcanoes file
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
nam = list(data["NAME"])


html = """<h4>Volcano Name: %s</h4>
Height: %s m 
"""

def color_producer():
    if el < 1000:
        return 'green'
    elif el >= 3000:
        return 'red'
    elif el >= 2000:
        return 'purple'
    elif el >= 1500:
        return 'beige'
    elif el >= 1000:
        return 'blue'


map = folium.Map(location=[38.58, -99.09], zoom_start=3, tiles="stamen toner")

fgv = folium.FeatureGroup(name="Volcanoes")


for lt, ln, el, na in zip(lat, lon, elev, nam):
    iframe = folium.IFrame(html=html % (na, str(el)), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius= 6, popup=folium.Popup(iframe), fill_color=color_producer(),color='grey',fill_opacity=1))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 100000000 else 'red' if 10000000 <= x['properties']['POP2005'] < 200000000 else 'purple'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("mapl.html")
