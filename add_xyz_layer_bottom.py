def add_xyz_basemap_layer(url: str, layer_name: str) -> QgsRasterLayer:
    """add xyz map from url, at the bottom of layers"""
    url = f"type=xyz&url={url}"
    xyz_layer = QgsRasterLayer(url, layer_name, "wms")
    root = QgsProject.instance().layerTreeRoot()
    root.insertChildNode(-1, QgsLayerTreeLayer(xyz_layer))
    return xyz_layer
    
gsi_std_lyr = add_xyz_basemap_layer(
            "https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png",
            "basemap_standard",
        )

        # basemap: gsi coloured elevation
gsi_relief_lyr = add_xyz_basemap_layer(
            "https://cyberjapandata.gsi.go.jp/xyz/relief/{z}/{x}/{y}.png",
            "basemap_relief",
        )

        # basemap: gsi hillshade
gsi_hillshade_lyr = add_xyz_basemap_layer(
            "https://cyberjapandata.gsi.go.jp/xyz/hillshademap/{z}/{x}/{y}.png",
            "basemap_hillshade",
        )