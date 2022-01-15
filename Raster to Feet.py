#convert raster to feet
import arcpy, os
wksp = arcpy.env.workspace= r"C:\Users\ariel\OneDrive\Desktop\GIS4080\Chunn_Ariel_FinalProject"

from arcpy.sa import *

in_rast = r"C:\Users\ariel\OneDrive\Desktop\GIS4080\Chunn_Ariel_FinalProject\grdn33w105_13"
elevInt = Int(in_rast)
elevInt.save("elevInt")
print("Converted raster to integer")

#inches to feet
in_rast = "elevInt"
to_Feet = 12
out_Div = Divide(in_rast, to_Feet)
out_Div.save(r"C:\Users\ariel\OneDrive\Desktop\GIS4080\Chunn_Ariel_FinalProject\PythonFinalProject.gdb\elevation")
print("converted Carlsbad raster to feet")

