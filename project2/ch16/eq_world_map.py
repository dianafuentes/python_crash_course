import json

from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline

#Explore the structure of the data 
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f: 
  all_eq_data = json.load(f) 

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_text = [], [], [], []
for eq_dict in all_eq_dicts:
  mag = eq_dict['properties']['mag']
  lon= eq_dict['geometry']['coordinates'][0]
  lat = eq_dict['geometry']['coordinates'][1]
  title = eq_dict['properties']['title']
  mags.append(mag)
  lons.append(lon)
  lats.append(lat)
  hover_text.append(title)
print(mags[:10])
print(lons[:5])
print(lats[:5]) 

#map the earthquakes 
#this is a simpler way to define data
#data = [Scattergeo(lon=lons, lat=lats)]
# But this is a better way when wanting to customize the presentation
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
      'size': [5*mag for mag in mags],
      'color': mags,
      'colorscale': 'Viridis',
      'reversescale': True, 
      'colorbar': {'title': 'Magnitude'},
    
    },
 }]

my_layout = Layout(title= 'Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename= 'global_earthquakes.html')