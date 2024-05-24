# get layouts list of current QGIS project
project = QgsProject.instance()                                  
layout_manager = project.layoutManager()
layouts = layout_manager.layouts()

for layout in layouts:
    print(layout.name())