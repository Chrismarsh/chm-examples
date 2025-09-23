def make_landcover(land,water):
    outtype = land

    if water != 1 or land == 0:
        outtype = 18

    return outtype

# water mask == 1 => land
def make_CanopyHeight(lai, cheight):
    outtype = cheight

    if lai <0.5:
        outtype = 0 # no lai => no height

    return outtype

# water mask == 1 => land
def make_LAI(lai, water):
    outtype = lai

    if water != 1:
        outtype = 0 # no lai on water

    return outtype

# water mask == 1 => land
def water(w):
    out = 1
    if w != 1:
        out = 0

    return out
    
dem_filename='fortress-fabdem.tif'
# clip_to_shp ='windmapper_config/shp/user_bbox.shp'

max_area=2500**2
max_tolerance=10
min_area=30**2

lloyd_itr = 2
do_smoothing = True
max_smooth_iter = 1
smoothing_scaling_factor = 1

simplify=True
simplify_tol=100
simplify_buffer=-200
write_shp=True
write_vtu=True

MPI_nworkers = 1
MPI_exec_str = 'python '

use_input_prj = False
wkt_out = "PROJCS[\"North_America_Albers_Equal_Area_Conic\"," \
              "     GEOGCS[\"GCS_North_American_1983\"," \
              "         DATUM[\"North_American_Datum_1983\"," \
              "             SPHEROID[\"GRS_1980\",6378137,298.257222101]]," \
              "         PRIMEM[\"Greenwich\",0]," \
              "         UNIT[\"Degree\",0.017453292519943295]]," \
              "     PROJECTION[\"Albers_Conic_Equal_Area\"]," \
              "     PARAMETER[\"False_Easting\",0]," \
              "     PARAMETER[\"False_Northing\",0]," \
              "     PARAMETER[\"longitude_of_center\",-96]," \
              "     PARAMETER[\"Standard_Parallel_1\",20]," \
              "     PARAMETER[\"Standard_Parallel_2\",60]," \
              "     PARAMETER[\"latitude_of_center\",40]," \
              "     UNIT[\"Meter\",1]," \
              "     AUTHORITY[\"EPSG\",\"102008\"]]" 
              
parameter_files = {
    # 'Ninja8_U' : {'file':'windmapper_config/ref-DEM-proj_0_U.tif','method':'mean'}, 
    # 'Ninja8_V' : {'file':'windmapper_config/ref-DEM-proj_0_V.tif','method':'mean'}, 
    # 'Ninja8' : {'file':'windmapper_config/ref-DEM-proj_0_spd_up_1000.tif','method':'mean'}, 
    # 'Ninja1_U' : {'file':'windmapper_config/ref-DEM-proj_45_U.tif','method':'mean'}, 
    # 'Ninja1_V' : {'file':'windmapper_config/ref-DEM-proj_45_V.tif','method':'mean'}, 
    # 'Ninja1' : {'file':'windmapper_config/ref-DEM-proj_45_spd_up_1000.tif','method':'mean'}, 
    # 'Ninja2_U' : {'file':'windmapper_config/ref-DEM-proj_90_U.tif','method':'mean'}, 
    # 'Ninja2_V' : {'file':'windmapper_config/ref-DEM-proj_90_V.tif','method':'mean'}, 
    # 'Ninja2' : {'file':'windmapper_config/ref-DEM-proj_90_spd_up_1000.tif','method':'mean'}, 
    # 'Ninja3_U' : {'file':'windmapper_config/ref-DEM-proj_135_U.tif','method':'mean'}, 
    # 'Ninja3_V' : {'file':'windmapper_config/ref-DEM-proj_135_V.tif','method':'mean'}, 
    # 'Ninja3' : {'file':'windmapper_config/ref-DEM-proj_135_spd_up_1000.tif','method':'mean'}, 
    # 'Ninja4_U' : {'file':'windmapper_config/ref-DEM-proj_180_U.tif','method':'mean'}, 
    # 'Ninja4_V' : {'file':'windmapper_config/ref-DEM-proj_180_V.tif','method':'mean'}, 
    # 'Ninja4' : {'file':'windmapper_config/ref-DEM-proj_180_spd_up_1000.tif','method':'mean'}, 
    # 'Ninja5_U' : {'file':'windmapper_config/ref-DEM-proj_225_U.tif','method':'mean'}, 
    # 'Ninja5_V' : {'file':'windmapper_config/ref-DEM-proj_225_V.tif','method':'mean'}, 
    # 'Ninja5' : {'file':'windmapper_config/ref-DEM-proj_225_spd_up_1000.tif','method':'mean'}, 
    # 'Ninja6_U' : {'file':'windmapper_config/ref-DEM-proj_270_U.tif','method':'mean'}, 
    # 'Ninja6_V' : {'file':'windmapper_config/ref-DEM-proj_270_V.tif','method':'mean'}, 
    # 'Ninja6' : {'file':'windmapper_config/ref-DEM-proj_270_spd_up_1000.tif','method':'mean'}, 
    # 'Ninja7_U' : {'file':'windmapper_config/ref-DEM-proj_315_U.tif','method':'mean'}, 
    # 'Ninja7_V' : {'file':'windmapper_config/ref-DEM-proj_315_V.tif','method':'mean'}, 
    # 'Ninja7' : {'file':'windmapper_config/ref-DEM-proj_315_spd_up_1000.tif','method':'mean'}, 
    # 'watermask' : {'file':'water_mask/Hansen_GFC-2019-v1.7-datamask.vrt', 'method':'mode', 'classifier':water, 'tolerance':0.43},

    'landcover': {'file':'landcover.tif', 'method':'mode'},

    'CanopyHeight' : {'file': ['lai.tif','canopyheight.tif'],
                      'method':['mean','mean'],
                      'classifier':make_CanopyHeight},

    'LAI': {'file':'lai.tif', 'method':'mean'}
}