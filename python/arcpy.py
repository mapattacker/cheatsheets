import arcpy
import os

# set folder/geodatabase, etc, where your spatial files are stored
# not necessary but convenient to prevent typing the path out
arcpy.env.workspace = "C:\Users\jake\Documents\ArcGIS\\nearest.gdb\\near_gr"


# list all feature classes in database
# also list shapefiles
for i in arcpy.ListFeatureClasses():
    print i


# get unique values from a field
def unique(table, field):
    with arcpy.da.SearchCursor(table, [field]) as cursor:
        listset = set([row[0] for row in cursor]) # remove duplicates
        return list(listset)

table = "C:\Users\siyang\Documents\ArcGIS\singapore.gdb\gr\el"
field = 'ED_EC'
print unique(table, field)