
def Tree_cover_2_Simple_Canopy(value):
    if value >= 30:
        value = 0
    else:
        value = 1
    return value
    
dem_filename = '/S40W080-S30W070_FABDEM_V1-0/clipped.tif'
clip_to_shp ='veg/veg.shp'

max_area=2500**2
max_tolerance=5
min_area=30**2

lloyd_itr = 1
do_smoothing = True
max_smooth_iter = 1
smoothing_scaling_factor = 1.5

simplify=True
simplify_tol=100
simplify_buffer=-200
write_shp=False
write_vtu=True

reuse_mesh = False

MPI_nworkers=8

use_input_prj = False
wkt_out="""PROJCS["WGS 84 / UTM zone 18S",
    GEOGCS["WGS 84",
        DATUM["WGS_1984",
            SPHEROID["WGS 84",6378137,298.257223563,
                AUTHORITY["EPSG","7030"]],
            AUTHORITY["EPSG","6326"]],
        PRIMEM["Greenwich",0,
            AUTHORITY["EPSG","8901"]],
        UNIT["degree",0.0174532925199433,
            AUTHORITY["EPSG","9122"]],
        AUTHORITY["EPSG","4326"]],
    PROJECTION["Transverse_Mercator"],
    PARAMETER["latitude_of_origin",0],
    PARAMETER["central_meridian",-75],
    PARAMETER["scale_factor",0.9996],
    PARAMETER["false_easting",500000],
    PARAMETER["false_northing",10000000],
    UNIT["metre",1,
        AUTHORITY["EPSG","9001"]],
    AXIS["Easting",EAST],
    AXIS["Northing",NORTH],
    AUTHORITY["EPSG","32718"]]
    """
              
parameter_files = { 
'landcover': {'file':'veg/landcover_renegado.tif', 'method':'mode'},

# run windmapper to get these files
'Ninja8_U' : {'file':'windmapper_config/ref-DEM-proj_0_U.tif','method':'mean'}, 
'Ninja8_V' : {'file':'windmapper_config/ref-DEM-proj_0_V.tif','method':'mean'}, 
'Ninja8' : {'file':'windmapper_config/ref-DEM-proj_0_spd_up_1000.tif','method':'mean'}, 
'Ninja1_U' : {'file':'windmapper_config/ref-DEM-proj_45_U.tif','method':'mean'}, 
'Ninja1_V' : {'file':'windmapper_config/ref-DEM-proj_45_V.tif','method':'mean'}, 
'Ninja1' : {'file':'windmapper_config/ref-DEM-proj_45_spd_up_1000.tif','method':'mean'}, 
'Ninja2_U' : {'file':'windmapper_config/ref-DEM-proj_90_U.tif','method':'mean'}, 
'Ninja2_V' : {'file':'windmapper_config/ref-DEM-proj_90_V.tif','method':'mean'}, 
'Ninja2' : {'file':'windmapper_config/ref-DEM-proj_90_spd_up_1000.tif','method':'mean'}, 
'Ninja3_U' : {'file':'windmapper_config/ref-DEM-proj_135_U.tif','method':'mean'}, 
'Ninja3_V' : {'file':'windmapper_config/ref-DEM-proj_135_V.tif','method':'mean'}, 
'Ninja3' : {'file':'windmapper_config/ref-DEM-proj_135_spd_up_1000.tif','method':'mean'}, 
'Ninja4_U' : {'file':'windmapper_config/ref-DEM-proj_180_U.tif','method':'mean'}, 
'Ninja4_V' : {'file':'windmapper_config/ref-DEM-proj_180_V.tif','method':'mean'}, 
'Ninja4' : {'file':'windmapper_config/ref-DEM-proj_180_spd_up_1000.tif','method':'mean'}, 
'Ninja5_U' : {'file':'windmapper_config/ref-DEM-proj_225_U.tif','method':'mean'}, 
'Ninja5_V' : {'file':'windmapper_config/ref-DEM-proj_225_V.tif','method':'mean'}, 
'Ninja5' : {'file':'windmapper_config/ref-DEM-proj_225_spd_up_1000.tif','method':'mean'}, 
'Ninja6_U' : {'file':'windmapper_config/ref-DEM-proj_270_U.tif','method':'mean'}, 
'Ninja6_V' : {'file':'windmapper_config/ref-DEM-proj_270_V.tif','method':'mean'}, 
'Ninja6' : {'file':'windmapper_config/ref-DEM-proj_270_spd_up_1000.tif','method':'mean'}, 
'Ninja7_U' : {'file':'windmapper_config/ref-DEM-proj_315_U.tif','method':'mean'}, 
'Ninja7_V' : {'file':'windmapper_config/ref-DEM-proj_315_V.tif','method':'mean'}, 
'Ninja7' : {'file':'windmapper_config/ref-DEM-proj_315_spd_up_1000.tif','method':'mean'}
}
              