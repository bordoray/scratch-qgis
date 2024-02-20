project = QgsProject.instance()
layout_template_path = r'C:\path\template.qpt'
with open(layout_template_path, 'r') as f:
    xml_content = f.read()

# Create a QDomDocument from the XML content
doc = QDomDocument()
doc.setContent(xml_content)
composition = QgsPrintLayout(project)
composition.loadFromTemplate(doc, QgsReadWriteContext())

template_name = composition.name()
manager = project.layoutManager()
project.layoutManager().addLayout(composition)
layout = manager.layoutByName(template_name)

# retrieve map item and set extent
map_item = layout.itemById("layout_item_map")
lyr = QgsProject.instance().mapLayersByName('layer_used_to_map_extent')[0]
map_item.zoomToExtent(lyr.extent())

# retrieve text object and set text
txt_title_item = layout.itemById("map_title")
txt_title_item.setText(some_title")

# Export
exporter = QgsLayoutExporter(layout)
pdf_path = r"C:\output\testpdf.pdf"
exporter.exportToPdf(pdf_path, QgsLayoutExporter.PdfExportSettings())

