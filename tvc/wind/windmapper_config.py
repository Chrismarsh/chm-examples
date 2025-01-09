# Resolution of WindNinja simulations (in m)
res_wind = 5
MPI_nworkers=4

# Number of wind speed categories (every 360/ncat degrees)
ncat = 8

# Flag to use existing DEM (DEM must be in UTM for WindNinja)
use_existing_dem = True
dem_filename = '/Users/cbm038/Documents/science/model_runs/tvc/OG/data/DEM_TVC_Lakes_2x2m_NAD83_UTM8N_TUPSR50DRIFT.tif'


# Averaging method to compute the transfer function in the downscaling method
#       "mean_tile": the wind speed is average over the whole domain for each WN simulation (as in marsh et al, 2020)
#        "grid": the wind speed is averaged over a squared area of size targer_res (as in Vionnet et al., 2020) 
wind_average = 'mean_tile'

# Target resolution for avegaging (in m)
#targ_res = 1000
