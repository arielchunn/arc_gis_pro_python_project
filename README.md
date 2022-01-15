# ArcGIS Pro Python Project
## Mapping
Created the ArcGIS project using aprx = arcpy.mp.ArcGISProject(), then used aprx.listMaps() and m.listLayers() to access the map ojbect and layers be sure all were included in the mapping project.
## Geodatabase Creation
Created a geodatabase, moved a digital elevation map raster file into the geodatabase. 
## Convert Elevation Map to Feet:
INT() was used to convert the feet raster to a raster with integer data. 
Then inches was converted to feet using Divide().
## Create Hillshade
A hillshade layer was created using the Statistical Analysis expansion. Tradition parameters are azimuth = 315 for the sun's relative positioning, altitude = 45 as the sun's angle above the horizon, and z - factor = 1 was used as the scaling factor for the elevation.

<p align ="center">
  <img width="442" height="405" src = "https://raw.githubusercontent.com/arielchunn/arc_gis_pro_python_project/a0f06d557fa36ae18498446283327c7c0b1943af/RasterPicture/Carlsbad%20raster%20DEM%20.png">
</p>
