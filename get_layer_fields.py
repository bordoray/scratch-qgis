# To be run in QGIS Python Console
target_layer_name = 'some_layer'

# Find the target layer by name
target_layer = QgsProject.instance().mapLayersByName(target_layer_name)[0]

# Check if the layer was found and is valid
if target_layer:
    # Get the list of fields
    fields = target_layer.fields()
    for field in fields:
        print(field.name())