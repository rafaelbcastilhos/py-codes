# heat graph according to the brazilian population
import folium
import pandas as pd
from folium import plugins

df = pd.read_csv("geolocation_map_br.csv")
# rendering first map
map = folium.Map(location=[-19.916667, -43.933333])

coordinates = []
# displaying the latitude and longitude coordinates
for lat, lng in zip(df.geolocation_lat.values[:18000], df.geolocation_lng.values[:18000]):
    coordinates.append([lat, lng])

map = folium.Map(location=[-15.788497, -47.879873], zoom_start=3.5, tiles="Stamen Toner")

df.geolocation_state.unique()
df2 = df.sample(frac=0.03)
# viewing the most distributed data on the map
for lat, lng in zip(df2.geolocation_lat.values, df2.geolocation_lng.values):
    coordinates.append([lat, lng])

map.add_child(plugins.HeatMap(coordinates))

map.save("heat_zone_map_br_out.html")

