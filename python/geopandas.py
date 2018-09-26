# https://github.com/jorisvandenbossche/geopandas-tutorial
# https://github.com/geopandas/geopandas
# http://geopandas.org/index.html

# Installation, create a virtual env
conda create -n geopandas
source activate geopandas  # activate vm
conda install -c conda-forge geopandas
conda install jupyter geopandas # for using within jupyter

source deactivate geopandas # deactivate vm



import geopandas as gpd
%config InlineBackend.figure_format = 'retina'

# READ SHAPEFILE --------------------
df = gpd.read_file(r'ne_110m_admin_0_countries.shp')
df.to_file('new.shp')

# supported export file types
import fiona; fiona.supported_drivers
{'AeronavFAA': 'r',
 'ARCGEN': 'r',
 'BNA': 'raw',
 'DXF': 'raw',
 'OpenFileGDB': 'r',
 'ESRI Shapefile': 'raw',
 'GeoJSON': 'rw',
 'GPKG': 'rw',
 'GPX': 'raw',
 'GPSTrackMaker': 'raw',
 'Idrisi': 'r',
 'MapInfo File': 'raw',
 'DGN': 'raw',
 'PCIDSK': 'r',
 'SEGY': 'r',
 'SUA': 'r'}


# DISPLAY MAP --------------------
    # choose colors
    # https://matplotlib.org/users/colormaps.html
df.plot(figsize=(10,10), cmap='tab20'); #categorical
df2.plot(figsize=(10,10), column='numeric', cmap='YlOrRd'); #chloropeth



# COORDINATE REFERENCE SYSTEM --------------------
# SVY21; epsg=3414
# WGS84; epsg=4326
# Web Mercator; epsg=3857


df.crs
# {'init': 'epsg:4326'}
df_mercator = df.to_crs(epsg=3857) # change CRS to mercator
df_mercator.crs
# {'init': 'epsg:3857', 'no_defs': True}


# CONVERT CSV INTO GEOPANDAS
import geopandas as gpd
from shapely.geometry import Point

geometry = [Point(xy) for xy in zip(df.Lon, df.Lat)]
df = df.drop(['Lon', 'Lat'], axis=1)
crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)



# FILTER, as with pandas --------------------
df[df.SOVEREIGNT=='Australia']


# DISSOLVE --------------------
df2 = df.dissolve(by='CONTINENT')
df2 = df.dissolve(by='CONTINENT', aggfunc='sum') # sum up all continuous columns


# SIMPLE MANIPULATIONS --------------------

# CENTROID
world['centroid_column'] = world.centroid # set centroid column
world = world.set_geometry('centroid_column') # change geometry from polygon to centroid point

# AREA
df2['area'] = df2.area


# JOIN --------------------
# attribute join
# can only use a left join by merge
df.merge(df2, on='iso_a3')

# spatial join
# op can be set to “intersects”, “within” or “contains”
cities_with_country = geopandas.sjoin(cities, countries, how="inner", op='intersects')


# OVERLAY --------------------
geopandas.overlay(df1, df2, how='union')
geopandas.overlay(df1, df2, how='intersection')
geopandas.overlay(df1, df2, how='symmetric_difference')
geopandas.overlay(df1, df2, how='difference')