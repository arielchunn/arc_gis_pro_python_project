# ArcGIS Pro Python Project
## Mapping
Created the ArcGIS project using aprx = arcpy.mp.ArcGISProject(), then used aprx.listMaps() and m.listLayers() to access the map object and layers to ensure all were included in the mapping project.
## Geodatabase Creation
Created a geodatabase and moved a raster file into the geodatabase. 
## Convert Elevation Map to Feet:
INT() was used to convert the feet raster to a raster with integer data. 
Divide() was used to convert inches to feet.
## Create Hillshade
A hillshade layer was created using the Statistical Analysis expansion. Tradition parameters used were azimuth = 315 for the sun's relative positioning, altitude = 45 the sun's angle above the horizon, and z - factor = 1 as the scaling factor for the elevation.
The image to the left is the original raster layer, the image the right is the converted DEM raster, and the gray scale image.

<p align ="center">
  <img width="342" height="305" src = "https://github.com/arielchunn/arc_gis_pro_python_project/blob/main/RasterPicture/Original%20Raster.png?raw=true">  <img width="342" height="305" src = "https://raw.githubusercontent.com/arielchunn/arc_gis_pro_python_project/a0f06d557fa36ae18498446283327c7c0b1943af/RasterPicture/Carlsbad%20raster%20DEM%20.png">
</p>
