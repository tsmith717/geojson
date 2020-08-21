import arcpy
import os

# Get the input feature class name.
fc = arcpy.GetParameterAsText(0)

arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:/Users/tod10784/Documents/ArcGIS/Projects/MyProject18"
arcpy.FeaturesToJSON_conversion(os.path.join("MyProject18.gdb", fc), 
                            "C:/Work/dev/tuts/geojson/" + fc + ".geojson", 
                            "NOT_FORMATTED", "Z_VALUES", "M_VALUES", "GEOJSON", "WGS84")