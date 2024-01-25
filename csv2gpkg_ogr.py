import subprocess, os

csv_path = r'your\path\your_csv_file.csv'
output_directory  = r"your\path"

cmd = (
            f"ogr2ogr -t_srs EPSG:3857 -f GPKG "
            "-oo X_POSSIBLE_NAMES=経度 -oo Y_POSSIBLE_NAMES=緯度 -nln csv_file"
            f" {os.path.join(output_directory,'csv_file.gpkg')}"
            f" {csv_path} -s_srs EPSG:4326"
        )

print(cmd)
subprocess.run(
            cmd,
            shell=True,
            check=True,
        )