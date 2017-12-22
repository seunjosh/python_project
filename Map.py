import folium
import pandas


#reading the text file with pandas
markerFile = pandas.read_csv("Markers.txt")

#Variable declearation
lat=list(markerFile["LAT"])
lon=list(markerFile["LON"])
elev=list(markerFile["ELEV"])

#Function for color production
def color_chooser(elevation):
    if elevation < 1000:
        return  'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

#map variable  declearation
mapo = folium.Map(location=[38.58, -90.09], zoom_start=5, tiles="cartodbdark_matter")


#feature group for varable for volcanoces
feautGv = folium.FeatureGroup(name="Volcanoes")

#iterating through the latitude, longtitude and Elevation columns in the volcanoes files
for l1, l2, ele in zip(lat, lon, elev):
    feautGv.add_child(folium.Marker(location=[l1, l2],  popup=str(ele)+" m", icon=folium.Icon(color=color_chooser(ele)
  )))

#feature group for varable for population detection
feautGp = folium.FeatureGroup(name="Population")
feautGp.add_child(folium.GeoJson(data=open('world.json',encoding='utf-8-sig' ).read(),  style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 80000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


#Adding map feature to the map menu
mapo.add_child(feautGv)
mapo.add_child(feautGp)
mapo.add_child(folium.LayerControl())

#save and creating the html for map viewing
mapo.save("mapTest1.html")