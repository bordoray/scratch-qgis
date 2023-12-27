# To be run in QGIS Python Console
in_shp = r'/path/in_shapefile.shp'
out_shp = r'/path/out_shapefile.shp'

options = f'-lco ENCODING=Shift_JIS' 

processing.run("gdal:convertformat", 
{'INPUT':in_shp,
'CONVERT_ALL_LAYERS':False,
'OPTIONS':options,
'OUTPUT':out_shp})

