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
df.plot(figsize=(10,10));


# COORDINATE REFERENCE SYSTEM --------------------
df.crs
# {'init': 'epsg:4326'}
df_mercator = df.to_crs(epsg=3395) # change CRS to mercator
df_mercator.crs
# {'init': 'epsg:3395', 'no_defs': True}


# CONVERT CSV INTO GEOPANDAS
import geopandas as gpd
from shapely.geometry import Point

geometry = [Point(xy) for xy in zip(df.Lon, df.Lat)]
df = df.drop(['Lon', 'Lat'], axis=1)
crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)


# FILTER, as with pandas --------------------
df[df.SOVEREIGNT=='Australia']