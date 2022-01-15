#create hillshade
import arcpy, os
from arcpy.sa import *
arcpy.env.overwriteOutput = True
wksp = arcpy.env.workspace = r"C:\Users\ariel\OneDrive\Desktop\GIS4080\Chunn_Ariel_FinalProject"

in_DEM=arcpy.Raster("grdn33w105_13")

az = 315
alti = 45
zFactor = 1

#Hillshade and output
#Hillshade(in_raster, {azimuth}, {altitude}, {model_shadows}, {z-factor})
out_Hill = Hillshade(in_DEM, az, alti, "", zFactor)
out_Hill.save("CarlsbadHS")

print("Created Carlsbad Hillshade")

