import arcpy, os
arcpy.env.overwriteOutput = True

wksp = arcpy.env.workspace = r"C:\Users\ariel\OneDrive\Desktop\GIS4080\Chunn_Ariel_FinalProject"

#list feature classes
featureclasses = arcpy.ListFeatureClasses()
print(featureclasses)

#list rasters
rasters = arcpy.ListRasters()
print(rasters)


#create a file GDB
out_folder_path = r"C:\Users\ariel\OneDrive\Desktop\GIS4080\Chunn_Ariel_FinalProject"
out_name = "PythonFinalProject.gdb"
arcpy.CreateFileGDB_management(out_folder_path, out_name)
print("Created " + out_name + ".")

gdb = r"C:\Users\ariel\OneDrive\Desktop\GIS4080\Chunn_Ariel_FinalProject\PythonFinalProject.gdb"

full_path = os.path.join(wksp, gdb)
print(full_path)

#move rasters into newly created GDB
for r in rasters:
    arcpy.RasterToGeodatabase_conversion(r, r"C:\Users\ariel\OneDrive\Desktop\GIS4080\Chunn_Ariel_FinalProject\PythonFinalProject.gdb")
    print("Copied" + r + "to geodtabase.")

#move feature classes to GDB
in_features = ["n33w105_13_meta.shp", "ned_13arcsec_g.shp"]
out_location =  (r"C:\Users\ariel\OneDrive\Desktop\GIS4080\Chunn_Ariel_FinalProject\PythonFinalProject.gdb")
arcpy.FeatureClassToGeodatabase_conversion(in_features, out_location)
print("Copied " + str(in_features) + " to gdb.")

