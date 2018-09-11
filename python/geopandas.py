# https://github.com/jorisvandenbossche/geopandas-tutorial
# https://github.com/geopandas/geopandas
# http://geopandas.org/index.html

# Installation, create a virtual env
conda create -n geopandas
source activate geopandas  # activate vm
conda install -c conda-forge geopandas
conda install jupyter geopandas # for using within jupyter

source deactivate geopandas # deactivate vm



import geopandas
%config InlineBackend.figure_format = 'retina'

# READ SHAPEFILE --------------------
df = geopandas.read_file(r'ne_110m_admin_0_countries.shp')
df.to_file('new.shp')

# DISPLAY MAP --------------------
df.plot(figsize=(10,10));


# COORDINATE REFERENCE SYSTEM --------------------
df.crs
# {'init': 'epsg:4326'}
df_mercator = df.to_crs(epsg=3395) # change CRS to mercator
df_mercator.crs
# {'init': 'epsg:3395', 'no_defs': True}


# FILTER, as with pandas --------------------
df[df.SOVEREIGNT=='Australia']