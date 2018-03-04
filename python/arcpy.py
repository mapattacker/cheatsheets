import arcpy
import os

# -----------------------
# set folder/geodatabase, etc, where your spatial files are stored 
# not necessary but convenient to prevent typing the path out
arcpy.env.workspace = "C:\Users\jake\Documents\ArcGIS\\nearest.gdb\\near_gr"



# list all feature classes in database -----------------------
# also list shapefiles
for i in arcpy.ListFeatureClasses():
    print i



# get unique values from a field -----------------------
def unique(table, field):
    with arcpy.da.SearchCursor(table, [field]) as cursor:
        listset = set([row[0] for row in cursor]) # remove duplicates
        return list(listset)

table = "C:\Users\siyang\Documents\ArcGIS\singapore.gdb\gr\el"
field = 'ED_EC'
print unique(table, field)



# use definition query -----------------------
# function only exist in layer, so have to convert that first
arcpy.MakeFeatureLayer_management(os.path.join(workspace,"pa_main"), 
                                        "pa_main_lyr", 
                                        where_clause=where)



# making output as temporary layers/files -----------------------
# just add "in_memory/layer_name" as the output
arcpy.Buffer_analysis("Roads", "in_memory/Buffers", 1000)
# delete in memory dataset
arcpy.Delete_management("in_memory/join1")



# deleting rows
with arcpy.da.UpdateCursor(os.path.join(workspace,initialname), "OBJECTID") as cursor:
    for row in cursor:
        if row[0] == 1:
            cursor.deleteRow()
print('table created, first redundant row deleted')