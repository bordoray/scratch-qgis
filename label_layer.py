# To be run in QGIS python console
# Label a layer automatically with specific size 
# ruled to label only >= 0.001 values of target field

layer = QgsProject.instance().mapLayersByName("some_layer")[0]

target_field = 'some_field'

# Create label settings
label_settings = QgsPalLayerSettings()
label_settings.fieldName = f'CASE WHEN "{target_field}" >= 0.001 THEN ROUND("{target_field}",1) ELSE \'\' END'  # Replace with the actual field name for labeling
label_settings.isExpression = True

# Set font properties
text_format = QgsTextFormat()
text_format.setFont(QFont("Arial Narrow", 8))
text_format.setSize(8)

label_settings.setFormat(text_format)

# Apply label settings to the layer
layer.setLabeling(QgsVectorLayerSimpleLabeling(label_settings))
layer.setLabelsEnabled(True)

# layer.setRenderer(renderer)
layer.triggerRepaint()
