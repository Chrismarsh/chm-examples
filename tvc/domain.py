import importlib.machinery
import os
import subprocess
import shutil

# Load in configuration file as module
# X = importlib.machinery.SourceFileLoader('config', os.path.join(os.getcwd(),'config.py'))
# X = X.load_module()

windmapper_config = """
# Configuration file for windmapper when a DEM is downloaded from the SRTM 30m archive

# Resolution of WindNinja simulations (in m)
res_wind = 5

# Number of wind speed categories (every 360/ncat degrees)
ncat = 16

# Flag to use existing DEM (DEM must be in UTM for WindNinja)
use_existing_dem = True
dem_filename = 'DEM_TVC_Lakes_2x2m_NAD83_UTM8N_TUPSR50DRIFT.tif'


# Averaging method to compute the transfer function in the downscaling method
#       "mean_tile": the wind speed is average over the whole domain for each WN simulation (as in marsh et al, 2020)
#        "grid": the wind speed is averaged over a squared area of size targer_res (as in Vionnet et al., 2020) 
wind_average = 'mean_tile'

# Target resolution for avegaging (in m)
#targ_res = 1000

""" #% (X.lat[0], X.lat[1], X.lon[0], X.lon[1] )

with open('windmapper_config.py', 'w') as file:
    file.write(windmapper_config)

subprocess.check_call(['windmapper.py windmapper_config.py'], shell=True)

subprocess.check_call(['windmapper2mesher.py windmapper_config'], shell=True)
with open('config_WN.txt','r') as file:
    WN_output=""" """
    for f in file.readlines():
        WN_output = WN_output + f

WN_output = WN_output[:-3]
mesher_config = """
import numpy as np
def LAI(value):
    return max(0,-1.0/0.5 * np.log(1-value) )


def Tree_cover_2_Simple_Canopy(value):
    if value >= 30:
        value = 0
    else:
        value = 1
    return value
    
dem_filename='windmapper_config/ref-DEM-proj.tif'
clip_to_shp ='windmapper_config/shp/user_bbox.shp'

max_area=300**2
max_tolerance=0.25
min_area=2**2

lloyd_itr = 1
#do_smoothing = True
#max_smooth_iter = 1
#smoothing_scaling_factor = 1

simplify=True
simplify_tol=50
#simplify_buffer=-200
write_shp=False
write_vtu=True

use_input_prj = True
wkt_out = 'PROJCS["NAD83 / UTM zone 8N", GEOGCS["NAD83", DATUM["North_American_Datum_1983", SPHEROID["GRS 1980",6378137,298.257222101, AUTHORITY["EPSG","7019"]], TOWGS84[0,0,0,0,0,0,0], AUTHORITY["EPSG","6269"]], PRIMEM["Greenwich",0, AUTHORITY["EPSG","8901"]], UNIT["degree",0.0174532925199433, AUTHORITY["EPSG","9122"]], AUTHORITY["EPSG","4269"]], PROJECTION["Transverse_Mercator"], PARAMETER["latitude_of_origin",0], PARAMETER["central_meridian",-135], PARAMETER["scale_factor",0.9996], PARAMETER["false_easting",500000], PARAMETER["false_northing",0], UNIT["metre",1, AUTHORITY["EPSG","9001"]], AXIS["Easting",EAST], AXIS["Northing",NORTH], AUTHORITY["EPSG","26908"]]'

# wkt_out = "PROJCS[\\"North_America_Albers_Equal_Area_Conic\\"," \\
#               "     GEOGCS[\\"GCS_North_American_1983\\"," \\
#               "         DATUM[\\"North_American_Datum_1983\\"," \\
#               "             SPHEROID[\\"GRS_1980\\",6378137,298.257222101]]," \\
#               "         PRIMEM[\\"Greenwich\\",0]," \\
#               "         UNIT[\\"Degree\\",0.017453292519943295]]," \\
#               "     PROJECTION[\\"Albers_Conic_Equal_Area\\"]," \\
#               "     PARAMETER[\\"False_Easting\\",0]," \\
#               "     PARAMETER[\\"False_Northing\\",0]," \\
#               "     PARAMETER[\\"longitude_of_center\\",-96]," \\
#               "     PARAMETER[\\"Standard_Parallel_1\\",20]," \\
#               "     PARAMETER[\\"Standard_Parallel_2\\",60]," \\
#               "     PARAMETER[\\"latitude_of_center\\",40]," \\
#               "     UNIT[\\"Meter\\",1]," \\
#               "     AUTHORITY[\\"EPSG\\",\\"102008\\"]]" 
              
parameter_files = { 
    'LIDAR': {'file':'M3_LiDAR_Processed_2m_NAD83_UTM8N_TUPSR50DRIFT.tif','method':'mean'},
    'CanopyHeight': {'file': 'vege_hgt_Filtered_DYNAMIC_2m_NAD83_UTM8N_TUPSR50DRIFT.tif',
                  'method': 'mean',
                  'tolerance':.5},
                   %s }
              """ % WN_output

with open('mesher_config.py', 'w') as file:
    file.write(mesher_config)

subprocess.check_call(['mesher.py mesher_config.py'], shell=True)

os.remove('config_WN.txt')
