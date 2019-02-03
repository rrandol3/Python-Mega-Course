import folium
import pandas
import webbrowser

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")
fgv = folium.FeatureGroup(name="Volcanoes")
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
def get_icon_color(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"
for lt,ln,el,nm in zip(lat, lon, elev, name):
    iconColor = get_icon_color(el)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup("Name:"+str(nm)+" Elevation:" +str(el), parse_html=True), color=iconColor, fill=True))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")

webbrowser.open_new("Map1.html")

#green el 0 to 2000
#orange el 2000 to 3000
#red el > 3000
