import arcpy
import os

arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:/Users/tod10784/Documents/ArcGIS/Projects/MyProject18"
arcpy.FeaturesToJSON_conversion(os.path.join("MyProject18.gdb", "CampusBuildings"), "C:/Work/dev/tuts/geojson/CampusBuildings.geojson", "NOT_FORMATTED",	"Z_VALUES", "M_VALUES", "GEOJSON", "WGS84")