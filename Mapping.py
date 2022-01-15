import arcpy

aprx = arcpy.mp.ArcGISProject(r"C:\Users\ariel\OneDrive\Documents\ArcGIS\Projects\PythonFinalProject\PythonFinalProject.aprx")

maps = aprx.listMaps()
for m in maps:
    print("Map: " + m.name)
    layers = m.listLayers()
    for lyr in layers:
        print("Layer: " + lyr.name + " " + lyr.dataSource)
del aprx
