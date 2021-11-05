import arcpy

arcpy.env.workspace = r"E:\Python\Arc_files\clip"

input="gis_osm_buildings_a_free_1.shp"
clip="Maharashtra.shp"
output="building.shp"
arcpy.Clip_analysis(input,clip,output)

arcpy.PolygonToRaster_conversion(output,"FID","B_raster.img","","",0.002)

msgcount=arcpy.GetMessageCount()
print arcpy.GetMessage(msgcount-1)