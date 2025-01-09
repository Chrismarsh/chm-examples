import numpy as np
def LAI(value):
    return max(0,-1.0/0.5 * np.log(1-value) )


def Tree_cover_2_Simple_Canopy(value):
    if value >= 30:
        value = 0
    else:
        value = 1
    return value

base_name='tvc'
dem_filename='/Users/cbm038/Documents/science/model_runs/tvc/OG/data/DEM_TVC_Lakes_2x2m_NAD83_UTM8N_TUPSR50DRIFT.tif'
max_area= 300**2
min_area = 2**2
max_tolerance = 0.25

clip_to_shp='/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/shp/user_bbox.shp'

lloyd_itr=1

simplify=True
simplify_tol=50
errormetric='rmse'


wkt_out = 'PROJCS["NAD83 / UTM zone 8N", GEOGCS["NAD83", DATUM["North_American_Datum_1983", SPHEROID["GRS 1980",6378137,298.257222101, AUTHORITY["EPSG","7019"]], TOWGS84[0,0,0,0,0,0,0], AUTHORITY["EPSG","6269"]], PRIMEM["Greenwich",0, AUTHORITY["EPSG","8901"]], UNIT["degree",0.0174532925199433, AUTHORITY["EPSG","9122"]], AUTHORITY["EPSG","4269"]], PROJECTION["Transverse_Mercator"], PARAMETER["latitude_of_origin",0], PARAMETER["central_meridian",-135], PARAMETER["scale_factor",0.9996], PARAMETER["false_easting",500000], PARAMETER["false_northing",0], UNIT["metre",1, AUTHORITY["EPSG","9001"]], AXIS["Easting",EAST], AXIS["Northing",NORTH], AUTHORITY["EPSG","26908"]]'

parameter_files = {
	'LIDAR_SWE': {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/data/M3_LiDAR_Processed_2m_NAD83_UTM8N_TUPSR50DRIFT.tif','method':'mean'},
    'CanopyHeight': {'file': '/Users/cbm038/Documents/science/model_runs/tvc/OG/data/vege_hgt_Filtered_DYNAMIC_2m_NAD83_UTM8N_TUPSR50DRIFT.tif',
                  'method': 'mean',
                  'tolerance':.5},
                  'Ninja8_U' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_0_U.tif','method':'mean'}, 
'Ninja8_V' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_0_V.tif','method':'mean'}, 
'Ninja8' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_0_spd_up_tile.tif','method':'mean'}, 
'Ninja1_U' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_45_U.tif','method':'mean'}, 
'Ninja1_V' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_45_V.tif','method':'mean'}, 
'Ninja1' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_45_spd_up_tile.tif','method':'mean'}, 
'Ninja2_U' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_90_U.tif','method':'mean'}, 
'Ninja2_V' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_90_V.tif','method':'mean'}, 
'Ninja2' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_90_spd_up_tile.tif','method':'mean'}, 
'Ninja3_U' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_135_U.tif','method':'mean'}, 
'Ninja3_V' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_135_V.tif','method':'mean'}, 
'Ninja3' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_135_spd_up_tile.tif','method':'mean'}, 
'Ninja4_U' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_180_U.tif','method':'mean'}, 
'Ninja4_V' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_180_V.tif','method':'mean'}, 
'Ninja4' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_180_spd_up_tile.tif','method':'mean'}, 
'Ninja5_U' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_225_U.tif','method':'mean'}, 
'Ninja5_V' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_225_V.tif','method':'mean'}, 
'Ninja5' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_225_spd_up_tile.tif','method':'mean'}, 
'Ninja6_U' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_270_U.tif','method':'mean'}, 
'Ninja6_V' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_270_V.tif','method':'mean'}, 
'Ninja6' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_270_spd_up_tile.tif','method':'mean'}, 
'Ninja7_U' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_315_U.tif','method':'mean'}, 
'Ninja7_V' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_315_V.tif','method':'mean'}, 
'Ninja7' : {'file':'/Users/cbm038/Documents/science/model_runs/tvc/OG/wind/windmapper_config/ref-DEM-proj_315_spd_up_tile.tif','method':'mean'}, 
                  }
