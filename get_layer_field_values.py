def get_feature_values_from(layer_name: str, field_name):

    layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    features = layer.getFeatures()

    field_values = [] 
    for feature in features:
        field_values.append(feature.attribute(field_name))
        
    return field_values

field_values = get_feature_values_from("layer_name", "field_name")
print(sorted(field_values))