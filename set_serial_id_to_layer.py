# To be run in QGIS python console
# Edit layer id field, with order of desc_field, then asc_field

layer = QgsProject.instance().mapLayersByName("mesh")[0]

id_field_name = 'id'
desc_field_name = 'desc_field'
asc_field_name = 'asc_field'


def edit_layer_serial(layer,id_field_name,desc_field_name,asc_field_name):
    
    # Start editing the layer
    layer.startEditing()

    # Sort the features based on 'top' in descending order and 'left' in ascending order
    request = QgsFeatureRequest().addOrderBy(desc_field_name, ascending=False).addOrderBy(asc_field_name,ascending=True)
    features = layer.getFeatures(request)

    # Update the 'id' field based on the sorting order
    for idx, feature in enumerate(features, start=1):
        feature.setAttribute(id_field_name, idx)
        layer.updateFeature(feature)

    # Stop editing and save changes
    layer.commitChanges()
    
edit_layer_serial(layer,id_field_name,desc_field_name,asc_field_name)