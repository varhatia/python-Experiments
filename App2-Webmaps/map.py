import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = data["LAT"]
lon = data["LON"]
name = data["NAME"]
elv = data["ELEV"]

def color_producer(el):
    if el < 1000:
        return 'green'
    elif 1000 <= el < 3000:
        return 'orange'
    else:
        return 'red'

html = """<h4>Volcano information </h4>
Name: %s
Height: %s m
"""

map=folium.Map(location=[58, -99], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Volcanoes Map")

for lt, ln, nm, el in zip(lat,lon, name, elv):
    iframe = folium.IFrame(html=html % (nm, str(el)), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(el))))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), 
style_function=lambda x: {'fillcolour' : 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map.html")