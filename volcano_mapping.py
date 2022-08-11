import folium
import pandas as p

data = p.read_csv("Volcanoes.txt")
# data.columns *lists every data column
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
# name = list(data["NAME"])

def colorizer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# html = """<h4>Volcano info:</h4> (To style popup window)
# Height: %s m
# """
#html_link = """
#Volcano name:<br>
#<a href="https://www.google.com/search?q=%%22%s%%22"
#target="_blank">%s</a><br>
#Height: %s m
#"""

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    #iframe = folium.IFrame(html=html_link % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m",
    fill_color=colorizer(el), color='grey', fill=True, fill_opacity=0.7))
# popup=folium.Popup(str(el), parse_html=True) <-fixes quotes(') problem
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("volcano_map.html")